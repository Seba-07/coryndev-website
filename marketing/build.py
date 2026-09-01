#!/usr/bin/env python3
"""Genera el flyer de CORYN en PDF + JPG, personalizado por referidor.

El flyer es de una sola hoja: se reparte por WhatsApp como imagen y en un
telefono no se lee nada bajo los 5mm. El detalle completo vive en la web, que
es a donde lleva el QR.

Uso:
  python3 build.py                       # version generica
  python3 build.py --ref TIO01 --nombre "Juan Perez" --fono "+56 9 1234 5678"
"""
import argparse, base64, pathlib, subprocess, urllib.parse

BASE = pathlib.Path(__file__).parent
ASSETS = BASE / "assets"
OUT = BASE / "out"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
WEB = "https://coryndev.com"
WHATSAPP = "56948780902"


def b64(path):
    return base64.b64encode(pathlib.Path(path).read_bytes()).decode()


def qr_svg(data, scale=1):
    import segno
    import io
    buf = io.BytesIO()
    segno.make(data, error="m").save(
        buf, kind="svg", scale=scale, border=0, dark="#0f2557", light=None, xmldecl=False, svgns=True
    )
    return "data:image/svg+xml;base64," + base64.b64encode(buf.getvalue()).decode()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ref", default="WEB", help="código de referido, ej. TIO01")
    ap.add_argument("--nombre", default="", help="nombre del referidor que aparece en el flyer")
    ap.add_argument("--fono", default="", help="teléfono del referidor (opcional)")
    a = ap.parse_args()

    web_link = f"{WEB}/?ref={a.ref}"
    msg = f"Hola CORYN, vi el volante. (Ref: {a.ref})"
    wa_link = f"https://wa.me/{WHATSAPP}?text=" + urllib.parse.quote(msg)

    if a.nombre:
        credito = f"Te compartió esto <b>{a.nombre}</b>"
        credito += f" &middot; {a.fono}" if a.fono else ""
    else:
        credito = "Comparte este documento con quien lo necesite"

    html = (BASE / "flyer.template.html").read_text()
    def img(nombre, ancho=None):
        """Las fotos van incrustadas en el propio PDF: el flyer se reparte por
        WhatsApp y tiene que verse igual sin conexion. Las que salen chicas se
        reducen antes de incrustarlas, si no el archivo se va a los 8 MB."""
        ruta = BASE.parent / "assets" / nombre
        if ancho is None:
            return "data:image/webp;base64," + b64(ruta)
        from PIL import Image
        import io
        im = Image.open(ruta).convert("RGB")
        if im.width > ancho:
            im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "WEBP", quality=82, method=6)
        return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()

    repl = {
        "{{MARK}}": "data:image/png;base64," + b64(ASSETS / "mark.png"),
        "{{FOTO}}": img("real-planilla.webp", 1400),
        "{{QR_WEB}}": qr_svg(web_link),
        "{{QR_WA}}": qr_svg(wa_link),
        "{{REF}}": "" if a.ref == "WEB" else f"Ref: {a.ref}",
        "{{CREDITO}}": credito,
    }
    for k, v in repl.items():
        html = html.replace(k, v)

    OUT.mkdir(exist_ok=True)
    slug = a.ref.lower()
    html_path = OUT / f"flyer-coryn-{slug}.html"
    html_path.write_text(html)

    pdf_path = OUT / f"flyer-coryn-{slug}.pdf"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf_path}", html_path.as_uri()], check=True,
                   capture_output=True)

    # La hoja como imagen, que es como se comparte por WhatsApp
    png_path = OUT / f"flyer-coryn-{slug}.png"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                    "--window-size=794,1123", "--force-device-scale-factor=2",
                    f"--screenshot={png_path}", html_path.as_uri()],
                   check=True, capture_output=True)
    try:
        from PIL import Image
        im = Image.open(png_path).convert("RGB")
        im.save(OUT / f"flyer-coryn-{slug}.jpg", quality=88, optimize=True)
    except ImportError:
        pass

    print(f"OK -> {pdf_path}")
    print(f"OK -> {png_path}")


if __name__ == "__main__":
    main()
