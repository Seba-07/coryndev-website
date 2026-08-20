#!/usr/bin/env python3
"""Genera el flyer de CORYN en PDF + JPG, personalizado por referidor.

Uso:
  python3 build.py                       # version generica
  python3 build.py --ref TIO01 --nombre "Juan Perez" --fono "+56 9 1234 5678"
"""
import argparse, base64, pathlib, subprocess, sys, urllib.parse

BASE = pathlib.Path(__file__).parent
ASSETS = BASE / "assets"
OUT = BASE / "out"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
WHATSAPP = "56933569725"
WEB = "https://coryndev.com"


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

    msg = f"Hola CORYN, me interesa cotizar un proyecto. (Ref: {a.ref})"
    wa_link = f"https://wa.me/{WHATSAPP}?text=" + urllib.parse.quote(msg)
    web_link = f"{WEB}/?ref={a.ref}"

    if a.nombre:
        credito = f"Te compartió esto <b>{a.nombre}</b>"
        credito += f" &middot; {a.fono}" if a.fono else ""
    else:
        credito = "Comparte este documento con quien lo necesite"

    html = (BASE / "flyer.template.html").read_text()
    repl = {
        "{{MARK}}": "data:image/png;base64," + b64(ASSETS / "mark.png"),
        "{{QR_WA}}": qr_svg(wa_link),
        "{{QR_WEB}}": qr_svg(web_link),
        "{{REF}}": a.ref,
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

    # Página 1 como imagen para compartir por WhatsApp
    png_path = OUT / f"flyer-coryn-{slug}-p1.png"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                    "--window-size=794,1123", "--force-device-scale-factor=2",
                    f"--screenshot={png_path}", html_path.as_uri()],
                   check=True, capture_output=True)
    try:
        from PIL import Image
        im = Image.open(png_path).convert("RGB")
        im.save(OUT / f"flyer-coryn-{slug}-p1.jpg", quality=88, optimize=True)
    except ImportError:
        pass

    print(f"OK -> {pdf_path}")
    print(f"OK -> {png_path}")


if __name__ == "__main__":
    main()
