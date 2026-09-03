#!/usr/bin/env python3
"""Genera los carruseles de Instagram de CORYN, uno por problema del sitio.

El contenido NO se escribe aqui: se extrae de site/que-resolvemos.body.html,
que es donde ya vive redactado y verificado. Asi el Instagram no se desalinea
del sitio, que es lo que pasa cuando el copy se duplica a mano.

Uso:
  python3 marketing/posts.py              # los seis casos
  python3 marketing/posts.py --caso 1     # solo uno
  python3 marketing/posts.py --listar     # ver que casos hay
"""
import argparse, base64, html, pathlib, re, subprocess

BASE = pathlib.Path(__file__).parent
RAIZ = BASE.parent
ASSETS = BASE / "assets"
OUT = BASE / "out" / "instagram"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ANCHO, ALTO = 1080, 1350


def limpio(x):
    """Texto plano desde el HTML del sitio, con las entidades resueltas."""
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", x))).strip()


def casos():
    """Los seis problemas, leidos del cuerpo de que-resolvemos."""
    fuente = (RAIZ / "site" / "que-resolvemos.body.html").read_text()
    crudos = re.findall(
        r'<img src="(assets/real-[^"]+)"[\s\S]*?'
        r'<img src="(assets/(?:after|demo)-[^"]+)"[\s\S]*?'
        r'<h2>(.*?)</h2>\s*<p class="pb-sintoma">(.*?)</p>'
        r'[\s\S]*?pb-costo">\s*<h3>Lo que te cuesta</h3>\s*<p>(.*?)</p>'
        r'[\s\S]*?pb-sol">\s*<h3>Lo que construimos</h3>\s*<p>(.*?)</p>', fuente)
    if not crudos:
        raise SystemExit("No se pudo leer ningun caso de que-resolvemos.body.html.\n"
                         "Si cambio la estructura de esa pagina, hay que ajustar la "
                         "expresion regular de casos().")
    return [dict(zip(("foto", "captura", "titulo", "sintoma", "cuesta", "solucion"),
                     list(c[:2]) + [limpio(x) for x in c[2:]]))
            for c in crudos]


# Promedio medido de las seis fotos originales (assets/real-*.webp). Las que
# llegaron despues venian mas oscuras y desaturadas, y en fila se notaba que
# eran de dos tandas distintas.
TONO_OBJETIVO = {"luz": 90.4, "contraste": 66.6, "saturacion": 69.5}
TOPE = (0.85, 1.35)   # sin esto una foto muy plana se iria a colores irreales


def armoniza(im):
    """Acerca el tono de una foto al del resto, sin tocar el archivo original."""
    from PIL import ImageStat, ImageEnhance
    acotar = lambda v: max(TOPE[0], min(TOPE[1], v))
    for medir, objetivo, filtro in (
        (lambda i: ImageStat.Stat(i.convert("L")).mean[0], "luz", ImageEnhance.Brightness),
        (lambda i: ImageStat.Stat(i.convert("L")).stddev[0], "contraste", ImageEnhance.Contrast),
        (lambda i: ImageStat.Stat(i.convert("HSV")).mean[1], "saturacion", ImageEnhance.Color),
    ):
        actual = medir(im)
        if actual > 1:
            im = filtro(im).enhance(acotar(TONO_OBJETIVO[objetivo] / actual))
    return im


def img64(ruta_rel, ancho=ANCHO):
    """Imagen incrustada y reducida: el HTML es temporal, pero a tamano
    original Chrome se demora de mas en cada lamina."""
    from PIL import Image
    import io
    im = Image.open(RAIZ / ruta_rel).convert("RGB")
    if "costo-" in str(ruta_rel):
        im = armoniza(im)
    if im.width > ancho:
        im = im.resize((ancho, round(im.height * ancho / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "WEBP", quality=86, method=6)
    return "data:image/webp;base64," + base64.b64encode(buf.getvalue()).decode()


def foto_costo(foto_problema):
    """La foto de la lamina 02, derivada del nombre de la del problema.

    real-planilla.webp -> costo-planilla.webp. Si esa no existe todavia, se cae
    a la del problema en vez de romper el generador."""
    candidata = foto_problema.replace("real-", "costo-")
    return candidata if (RAIZ / candidata).exists() else foto_problema


def bloque_foto(ruta_rel, sello, bien=False, marca=None):
    """La franja superior: la imagen, su sello y la marca.

    En las capturas de sistema el sello va abajo: los paneles llevan su titulo
    arriba a la izquierda y el sello se lo comia."""
    captura = any(x in str(ruta_rel) for x in ("demo-", "after-", "vivo-"))
    clase = "sello bien" if bien else "sello"
    if captura:
        clase += " abajo"
    logo = (f'<div class="marca"><img src="{marca}" alt=""><b>CORYN</b></div>'
            if marca else "")
    return (f'<div class="foto"><img src="{img64(ruta_rel)}" alt="">'
            f'<p class="{clase}"><i></i>{html.escape(sello)}</p>{logo}</div>')


def resalta(titulo):
    """Pinta en cian la ultima mitad del titular, como en el sitio y el volante."""
    palabras = titulo.split()
    if len(palabras) < 4:
        return html.escape(titulo)
    corte = len(palabras) // 2
    return (html.escape(" ".join(palabras[:corte])) +
            " <em>" + html.escape(" ".join(palabras[corte:])) + "</em>")


# El cierre de cada carrusel. Antes era la misma lamina en las seis, con
# bySIMMED y AvenProp repetidos: la prueba se gasta si va en todas. Ahora las
# obras salen solo en la primera y el resto cierra mostrando hasta donde puede
# llegar ese mismo problema resuelto.
CIERRES = {
    "planilla": (None, "Ya lo hicieron", """    <p class="rot">No es promesa</p>
    <h2>Dos que ya<br><em>lo hicieron</em></h2>
    <p class="texto">Así trabajan hoy <b>bySIMMED</b> y <b>AvenProp</b>. En la web
    ves qué tenían antes y qué se construyó, y calculas cuánto costaría el tuyo.
    <b>La primera reunión no tiene costo.</b></p>"""),
    "google": ("assets/demo-app.webp", "Y después", """    <p class="rot">Y después</p>
    <h2>Del sitio<br><em>a la app</em></h2>
    <p class="texto">Se parte por donde más duele y el sistema crece contigo.
    En la web calculas cuánto costaría lo tuyo.
    <b>La primera reunión no tiene costo.</b></p>"""),
    "whatsapp": ("assets/demo-ruta.webp", "Y después", """    <p class="rot">Y después</p>
    <h2>Del catálogo<br><em>al reparto</em></h2>
    <p class="texto">Cuando el cliente ya compra solo, lo siguiente es que el
    pedido llegue. En la web calculas cuánto costaría lo tuyo.
    <b>La primera reunión no tiene costo.</b></p>"""),
    "telefono": ("assets/demo-integra.webp", "Y después", """    <p class="rot">Y después</p>
    <h2>Que la agenda<br><em>hable con el resto</em></h2>
    <p class="texto">Las reservas que entran solas también pueden avisarle a tu
    sistema. En la web calculas cuánto costaría lo tuyo.
    <b>La primera reunión no tiene costo.</b></p>"""),
    "cobranza": ("assets/demo-panel.webp", "Y después", """    <p class="rot">Y después</p>
    <h2>Ver el negocio<br><em>completo</em></h2>
    <p class="texto">Cuando la cobranza está ordenada, recién ahí los números
    sirven para decidir. En la web calculas cuánto costaría lo tuyo.
    <b>La primera reunión no tiene costo.</b></p>"""),
    "pedidos": ("assets/demo-soporte.webp", "Cada mes", """    <p class="rot">Y todos los meses</p>
    <h2>No se entrega<br><em>y se abandona</em></h2>
    <p class="texto">Mantención, respaldos y mejoras cada mes, sin permanencia.
    En la web calculas cuánto costaría lo tuyo.
    <b>La primera reunión no tiene costo.</b></p>"""),
}


def cierre(caso, marca):
    """La lamina 04, distinta para cada caso."""
    llave = pathlib.Path(caso["foto"]).stem.replace("real-", "")
    img, pie, texto = CIERRES.get(llave, CIERRES["planilla"])
    if img is None:
        capa = ('<div class="foto"><div class="obras">'
                f'<div class="obra"><img src="{img64("assets/vivo-bysimmed.webp", 620)}" alt="">'
                '<span>bySIMMED</span></div>'
                f'<div class="obra"><img src="{img64("assets/vivo-avenprop.webp", 620)}" alt="">'
                '<span>AvenProp</span></div></div></div>')
    else:
        capa = bloque_foto(img, pie, bien=True, marca=marca)
    return ("04", "coryndev.com", "Link en la bio", capa, texto)


def laminas(caso, marca):
    """Las cuatro laminas, todas con imagen: la foto del problema, la del costo
    que produce, la captura del sistema resuelto y las dos obras de clientes."""
    e = html.escape
    return [
        ("01", "coryndev.com", "Desliza →",
         bloque_foto(caso["foto"], "Hoy", marca=marca),
         f'''    <p class="rot">Hoy en tu negocio</p>
    <h1>{resalta(caso["titulo"])}</h1>
    <p class="texto">{e(caso["sintoma"])}</p>'''),

        ("02", "coryndev.com", "Desliza →",
         bloque_foto(foto_costo(caso["foto"]), "Lo que te cuesta"),
         f'''    <p class="rot">El precio de dejarlo así</p>
    <h2>Lo que te <em>está costando</em></h2>
    <p class="texto">{e(caso["cuesta"])}</p>'''),

        ("03", "coryndev.com", "Desliza →",
         bloque_foto(caso["captura"], "Con un sistema", bien=True),
         f'''    <p class="rot">Cómo queda resuelto</p>
    <h2>Así se ve <em>funcionando</em></h2>
    <p class="texto">{e(caso["solucion"])}</p>'''),

        cierre(caso, marca),
    ]


# Cuatro portadas de destacadas. Trazo simple y grande, del mismo grosor que
# los iconos del sitio: a 64px lo que se lee es la silueta, nada mas.
DESTACADAS = [
    ("que-hacemos", "Qué hacemos",
     '<svg viewBox="0 0 24 24">'
     '<rect x="3" y="3" width="7.5" height="7.5" rx="1.4"/>'
     '<rect x="13.5" y="3" width="7.5" height="7.5" rx="1.4"/>'
     '<rect x="3" y="13.5" width="7.5" height="7.5" rx="1.4"/>'
     '<rect x="13.5" y="13.5" width="7.5" height="7.5" rx="1.4"/></svg>'),
    ("casos", "Casos",
     '<svg viewBox="0 0 24 24">'
     '<rect x="2.5" y="4" width="19" height="14.5" rx="2"/>'
     '<path d="M2.5 8h19"/><path d="M5.6 6h.01M8 6h.01"/>'
     '<path d="m9 13 2.2 2.2L15.4 11"/></svg>'),
    ("precios", "Precios",
     '<svg viewBox="0 0 24 24">'
     '<path d="M12 3v18"/>'
     '<path d="M16.5 7.2c-.8-1.4-2.5-2.2-4.5-2.2-2.6 0-4.4 1.3-4.4 3.2 0 4.3 9.1 2.3 9.1 7 0 2-2 3.3-4.7 3.3-2.2 0-4-.9-4.8-2.4"/>'
     '</svg>'),
    ("proceso", "Proceso",
     '<svg viewBox="0 0 24 24">'
     '<circle cx="5" cy="18.5" r="2.6"/><circle cx="12" cy="12" r="2.6"/>'
     '<circle cx="19" cy="5.5" r="2.6"/>'
     '<path d="m6.9 16.7 3.2-3M13.9 10.1l3.2-3"/></svg>'),
]


def precios_del_sitio():
    """Los cuatro precios, leidos del estimador del inicio: fuente unica."""
    fuente = (RAIZ / "site" / "inicio.body.html").read_text()
    crudos = re.findall(r"nom: '([^']+)',[\s\S]{0,260}?base: (\d+),\s*uf: ([\d.]+)", fuente)
    if len(crudos) < 4:
        raise SystemExit("No se pudieron leer los precios del estimador de "
                         "site/inicio.body.html. Revisar la expresion regular.")
    return [(n.replace("Un ", "").replace("Una ", "").capitalize(),
             "$" + f"{int(b):,}".replace(",", "."),
             u.replace(".", ",") + " UF") for n, b, u in crudos]


def _tabla_precios():
    """De menor a mayor: el numero mas bajo primero baja la guardia, y una
    columna ordenada se lee de un vistazo. El "desde" va aparte y mas chico
    para que mande la cifra, no la palabra."""
    filas = sorted(precios_del_sitio(),
                   key=lambda p: int(p[1].replace("$", "").replace(".", "")))
    return "".join(f'<tr><td>{n}</td>'
                   f'<td class="n"><i>desde</i>{b}</td></tr>'
                   for n, b, _ in filas)


# Las historias que van dentro de cada destacada. La portada es solo la tapa;
# esto es lo que ve quien toca el circulo.
def _precios():
    return [
        ("Precios", """    <p class="rot">Sin letra chica</p>
    <h1>Los precios,<br><em>publicados</em></h1>
    <p class="texto">Casi nadie en el rubro los muestra. Nosotros sí: acá están,
    y en la web calculas el tuyo en 30 segundos.</p>"""),
        ("Al empezar", """    <p class="rot">Se paga una sola vez</p>
    <h2>Al empezar</h2>
    <table class="tabla">""" + _tabla_precios() + """</table>
    <div class="caja">El precio se <b>cierra por escrito antes de empezar</b>.
    Si tu caso trae más, se cotiza aparte: nada cambia a mitad de camino.</div>"""),
        ("Cada mes", """    <p class="rot">Acompañamiento</p>
    <h2>Y cada mes,<br><em>1 UF</em></h2>
    <p class="texto">1,5 UF si es tienda online o app. Cubre:</p>
    <div class="lista">
      <div><i>&#9679;</i><span>Mantención, respaldos y actualizaciones</span></div>
      <div><i>&#9679;</i><span>Monitoreo, para enterarnos antes que tú</span></div>
      <div><i>&#9679;</i><span>Ajustes y mejoras pequeñas todos los meses</span></div>
      <div><i>&#9679;</i><span>Atención con prioridad ante fallas</span></div>
    </div>"""),
        ("Sin permanencia", """    <p class="rot">Lo que nos obliga</p>
    <h2>Te puedes ir<br><em>cualquier mes</em></h2>
    <p class="texto">Sin multa por salir. El código y los datos son tuyos, a tu
    nombre desde el primer día. Y el mensual <b>se revisa una vez al año</b>,
    nunca por sorpresa.</p>
    <div class="caja">Cobramos poco al empezar y el grueso llega mes a mes:
    <b>necesitamos que el sistema te sirva</b>, o te vas.</div>"""),
        ("Calcula", """    <p class="rot">En la web</p>
    <h2>Calcula lo tuyo<br><em>en 30 segundos</em></h2>
    <p class="texto">Eliges qué necesitas y te dice el precio, con todo lo que
    incluye y lo que no. <b>La primera reunión no tiene costo.</b></p>"""),
    ]


def _casos():
    return [
        ("Casos", """    <p class="rot">Trabajo entregado</p>
    <h1>Dos que ya<br><em>están andando</em></h1>
    <p class="texto">No son maquetas ni ejemplos: son negocios reales que hoy
    trabajan con lo que construimos.</p>"""),
        ("bySIMMED", """    <div class="imagen"><img src="{{IMG:assets/vivo-bysimmed.webp}}" alt=""></div>
    <p class="rot">Salud &middot; Sitio y catálogo</p>
    <h2>bySIMMED</h2>
    <p class="texto">Fabrica simuladores clínicos de alta fidelidad, diseñados
    por médicos, y vende a especialistas en varios países.</p>"""),
        ("bySIMMED", """    <p class="rot">El problema</p>
    <h2>Buen producto,<br><em>sin dónde mostrarlo</em></h2>
    <p class="texto">Su comprador es muy específico: médicos especialistas y
    centros de formación clínica. Ese comprador necesita ver la ficha técnica
    antes de escribir, y no la tenía dónde.</p>
    <div class="caja">Le construimos un sitio con catálogo pensado como
    <b>herramienta de venta técnica</b>, no como folleto.</div>"""),
        ("AvenProp", """    <div class="imagen"><img src="{{IMG:assets/vivo-avenprop.webp}}" alt=""></div>
    <p class="rot">Inmobiliario &middot; Plataforma web</p>
    <h2>AvenProp</h2>
    <p class="texto">Compra, vende y arrienda propiedades en Santiago, y además
    asegura lo que vale la pena proteger.</p>"""),
        ("AvenProp", """    <p class="rot">El problema</p>
    <h2>El portal se<br><em>quedaba el cliente</em></h2>
    <p class="texto">Publicar en portales sirve para aparecer, pero el
    interesado nunca llega a conocer a la corredora: llega a una ficha.</p>
    <div class="caja">Ahora tiene <b>plataforma propia</b>, donde el corretaje y
    los seguros conviven y el interesado llega directo.</div>"""),
        ("Conversemos", """    <p class="rot">Tu caso</p>
    <h2>¿Se parece<br><em>al tuyo?</em></h2>
    <p class="texto">En la web ves los dos casos completos, con qué tenían antes
    y qué se construyó. <b>La primera reunión no tiene costo.</b></p>"""),
    ]


def servicios_del_sitio():
    """Los seis servicios, leidos de servicios.body.html.

    Se parte por bloque de panel en vez de emparejar listas paralelas: hacerlo
    con dos listas dejaba las claves corridas en uno."""
    fuente = (RAIZ / "site" / "servicios.body.html").read_text()
    claves = re.findall(r'<span class="svc-clave">([^<]+)</span>', fuente)
    bloques = re.split(r'<div class="svc-hoja"', fuente)[1:]
    if len(claves) != len(bloques) or not bloques:
        raise SystemExit("La estructura de servicios.body.html cambio: hay "
                         f"{len(claves)} claves y {len(bloques)} paneles.")
    salida = []
    for clave, b in zip(claves, bloques):
        img = re.search(r'<img src="(assets/[^"]+)"', b)
        h2 = re.search(r"<h2>(.*?)</h2>", b)
        res = re.search(r'<p class="svc-resumen">(.*?)</p>', b, re.S)
        salida.append((limpio(h2.group(1)), limpio(clave), limpio(res.group(1)),
                       img.group(1) if img else None))
    return salida


def etapas_del_sitio():
    """Las cinco etapas del proceso, con su resumen y su detalle."""
    fuente = (RAIZ / "site" / "proceso.body.html").read_text()
    resumen = re.findall(
        r'<span class="paso">(\d+)</span>([^<]+)</span>\s*<span class="cu">([^<]+)</span>',
        fuente)
    detalles = []
    for b in re.split(r'<section class="proc-etapa', fuente)[1:]:
        p = re.search(r"<p[^>]*>(.*?)</p>", b, re.S)
        detalles.append(limpio(p.group(1)) if p else "")
    if len(resumen) != len(detalles) or not resumen:
        raise SystemExit("La estructura de proceso.body.html cambio: hay "
                         f"{len(resumen)} etapas y {len(detalles)} detalles.")
    return [(n, limpio(nom), limpio(cu), det)
            for (n, nom, cu), det in zip(resumen, detalles)]


def _recorta(texto, tope=210):
    """La historia no da para parrafos largos: corta en el punto mas cercano."""
    if len(texto) <= tope:
        return texto
    corte = texto.rfind(".", 0, tope)
    return texto[:corte + 1] if corte > tope * 0.55 else texto[:tope].rsplit(" ", 1)[0] + "..."


def _clase_imagen(ruta):
    """Vertical va en marco de telefono; apaisada, en franja a sangre."""
    try:
        from PIL import Image as _I
        with _I.open(RAIZ / ruta) as im:
            vertical = im.size[0] / im.size[1] < 0.8
    except Exception:
        vertical = False
    return "imagen telefono" if vertical else "imagen"



def _reel_precios():
    """Los fotogramas del reel de precios. Los montos salen del estimador del
    sitio, igual que todo lo demas: si cambia alla, cambia aca."""
    fs = [
        """    <h1>¿Cuánto cuesta<br><em>un sistema<br>a medida?</em></h1>""",
        """    <h1>Nadie<br>te lo dice.</h1>
    <p class="sub">Todos escriben <b>"cotízalo con nosotros"</b>. Ahí van los precios.</p>""",
    ]
    for nombre, monto, uf in precios_del_sitio():
        fs.append(f"""    <p class="que">{nombre}</p>
    <p class="monto">{monto}</p>
    <p class="mas">+ {uf} al mes</p>
    <p class="nota">Puesta en marcha. El acompañamiento mensual va aparte
    y no tiene permanencia.</p>""")
    fs.append("""    <h1>Precio cerrado<br><em>antes de<br>empezar.</em></h1>
    <p class="sub">Calcula el tuyo en coryndev.com.
    <b>La primera reunión no tiene costo.</b></p>""")
    return fs


def reel():
    """Los fotogramas del reel, listos para montar en Instagram."""
    plantilla = (BASE / "reel.template.html").read_text()
    marca = "data:image/png;base64," + base64.b64encode(
        (ASSETS / "mark.png").read_bytes()).decode()
    carpeta = OUT / "reel-precios"
    carpeta.mkdir(parents=True, exist_ok=True)
    hechos = []
    for i, contenido in enumerate(_reel_precios(), 1):
        fuente = carpeta / f"{i:02d}.html"
        fuente.write_text(plantilla.replace("{{MARK}}", marca)
                                   .replace("{{CONTENIDO}}", contenido))
        destino = carpeta / f"{i:02d}.png"
        subprocess.run(
            [CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
             "--window-size=1080,1920", "--virtual-time-budget=4000",
             f"--screenshot={destino}", fuente.as_uri()],
            check=True, capture_output=True)
        fuente.unlink()
        hechos.append(destino)
    return hechos


def _que_hacemos():
    laminas = [("Servicios", """    <p class="rot">Lo que hacemos</p>
    <h1>Seis formas<br><em>de ayudarte</em></h1>
    <p class="texto">Con el alcance, el plazo y el precio de cada una. Sin letra
    chica: también decimos lo que no incluye.</p>""")]
    for nombre, clave, resumen, img in servicios_del_sitio():
        imagen = (f'    <div class="{_clase_imagen(img)}">'
                  f'<img src="{{{{IMG:{img}}}}}" alt=""></div>\n'
                  if img else "")
        laminas.append((nombre.split("(")[0].strip(), imagen +
                        f"""    <p class="rot">{html.escape(clave)}</p>
    <h2>{html.escape(nombre)}</h2>
    <p class="texto">{html.escape(_recorta(resumen))}</p>"""))
    laminas.append(("Calcula", """    <p class="rot">En la web</p>
    <h2>¿Cuál se parece<br><em>a lo tuyo?</em></h2>
    <p class="texto">En coryndev.com está el detalle de cada uno: qué incluye,
    qué no incluye y cuánto demora. Y puedes calcular tu precio.
    <b>La primera reunión no tiene costo.</b></p>"""))
    return laminas


def _proceso():
    laminas = [("Proceso", """    <p class="rot">Cómo trabajamos</p>
    <h1>De la primera<br>llamada a la<br><em>mejora del mes 12</em></h1>
    <p class="texto">Cinco etapas. <b>Las dos primeras son sin costo</b> y
    sirven justamente para decidir si vale la pena seguir.</p>""")]
    for n, nombre, cu, detalle in etapas_del_sitio():
        laminas.append((f"Etapa {n}", f"""    <p class="rot">Etapa {n} &middot; {html.escape(cu)}</p>
    <h2>{html.escape(nombre)}</h2>
    <p class="texto">{html.escape(_recorta(detalle))}</p>"""))
    laminas.append(("Partamos", """    <p class="rot">La primera etapa</p>
    <h2>Media hora,<br><em>sin costo</em></h2>
    <p class="texto">Cuéntanos qué te está complicando y te decimos con
    honestidad qué se puede resolver con software y qué conviene priorizar.
    <b>Si no vale la pena, también te lo decimos.</b></p>"""))
    return laminas


HISTORIAS = {"precios": _precios, "casos": _casos,
             "que-hacemos": _que_hacemos, "proceso": _proceso}


def historias(cual):
    """Las historias de una destacada, listas para subir."""
    plantilla = (BASE / "historia.template.html").read_text()
    marca = "data:image/png;base64," + base64.b64encode(
        (ASSETS / "mark.png").read_bytes()).decode()
    carpeta = OUT / "historias" / cual
    carpeta.mkdir(parents=True, exist_ok=True)
    hechas = []
    for i, (pie, contenido) in enumerate(HISTORIAS[cual](), 1):
        for ruta in re.findall(r"\{\{IMG:([^}]+)\}\}", contenido):
            contenido = contenido.replace("{{IMG:" + ruta + "}}", img64(ruta, 900))
        fuente = carpeta / f"{i:02d}.html"
        fuente.write_text(plantilla.replace("{{MARK}}", marca)
                                   .replace("{{PIE}}", pie)
                                   .replace("{{CONTENIDO}}", contenido))
        destino = carpeta / f"{i:02d}.png"
        subprocess.run(
            [CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
             "--window-size=1080,1920", "--virtual-time-budget=4000",
             f"--screenshot={destino}", fuente.as_uri()],
            check=True, capture_output=True)
        fuente.unlink()
        hechas.append(destino)
    return hechas


def portadas_destacadas():
    """Una portada por destacada, lista para subir a Instagram."""
    plantilla = (BASE / "destacada.template.html").read_text()
    carpeta = OUT / "destacadas"
    carpeta.mkdir(parents=True, exist_ok=True)
    hechas = []
    for slug, nombre, svg in DESTACADAS:
        fuente = carpeta / f"{slug}.html"
        fuente.write_text(plantilla.replace("{{SVG}}", svg))
        destino = carpeta / f"{slug}.png"
        subprocess.run(
            [CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
             "--window-size=1080,1920", "--virtual-time-budget=3000",
             f"--screenshot={destino}", fuente.as_uri()],
            check=True, capture_output=True)
        fuente.unlink()
        hechas.append((destino, nombre))
    return hechas


def foto_perfil():
    """Foto de perfil de 1080x1080 con el simbolo centrado y aire alrededor.

    Instagram recorta el perfil en circulo: el mark solo se sale por los bordes
    y el icono con la palabra CORYN queda con el texto cortado. Por eso se arma
    una pieza propia en vez de reutilizar un asset del sitio."""
    from PIL import Image
    lado, noche = 1080, (7, 14, 32)
    simbolo = Image.open(ASSETS / "mark.png").convert("RGBA")
    ancho = int(lado * 0.52)
    alto = round(simbolo.height * ancho / simbolo.width)
    simbolo = simbolo.resize((ancho, alto), Image.LANCZOS)
    lienzo = Image.new("RGB", (lado, lado), noche)
    lienzo.paste(simbolo, ((lado - ancho) // 2, (lado - alto) // 2), simbolo)
    OUT.mkdir(parents=True, exist_ok=True)
    destino = OUT / "perfil.png"
    lienzo.save(destino)
    return destino


def pie_de_texto(caso, n):
    """El texto del post, para pegar en Instagram junto a las imagenes."""
    return "\n".join([
        f"{caso['titulo']}.",
        "",
        caso["sintoma"],
        "",
        f"Lo que te cuesta: {caso['cuesta']}",
        "",
        f"Lo que construimos: {caso['solucion']}",
        "",
        "Software a medida para pymes chilenas. Precio cerrado antes de empezar "
        "y sin permanencia. La primera reunión no tiene costo.",
        "",
        "Escríbenos o mira los casos en coryndev.com (link en la bio).",
        "",
        "#pymeschile #software #transformaciondigital #emprendimientochile "
        "#gestionempresarial #pymes #chile",
    ])


def galeria(generados):
    """Una pagina para revisar todo antes de publicar, servida en local."""
    filas = []
    for n, caso in generados:
        laminas = "".join(
            f'<a href="caso-{n}/{paso}.png" target="_blank">'
            f'<img src="caso-{n}/{paso}.png" alt="Lámina {paso}"></a>'
            for paso in ("01", "02", "03", "04"))
        texto = html.escape((OUT / f"caso-{n}" / "texto.txt").read_text())
        filas.append(f"""<article>
      <h2><span>{n}</span>{html.escape(caso["titulo"])}</h2>
      <div class="tira">{laminas}</div>
      <details><summary>Texto del post</summary><pre>{texto}</pre></details>
    </article>""")

    extras = ""
    if (OUT / "perfil.png").exists():
        extras += '<a href="perfil.png" target="_blank"><img class="redondo" src="perfil.png" alt="Perfil"></a>'
    for slug, nombre, _ in DESTACADAS:
        if (OUT / "destacadas" / f"{slug}.png").exists():
            extras += (f'<a href="destacadas/{slug}.png" target="_blank">'
                       f'<img class="redondo" src="destacadas/{slug}.png" alt="{nombre}">'
                       f'<span>{nombre}</span></a>')

    tiras = ""
    for cual in sorted(HISTORIAS):
        fs = sorted((OUT / "historias" / cual).glob("*.png"))
        if not fs:
            continue
        vistas = "".join(
            f'<a href="historias/{cual}/{f.name}" target="_blank">'
            f'<img src="historias/{cual}/{f.name}" alt=""></a>' for f in fs)
        tiras += (f'<article><h2><span>H</span>Destacada: {cual}</h2>'
                  f'<div class="tira historias">{vistas}</div></article>')

    (OUT / "index.html").write_text(f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CORYN — piezas de Instagram</title>
<style>
  :root{{ --noche:#070e20; --cian:#6fd8ec; --sobre:#c9daf6; }}
  *{{ box-sizing:border-box; }}
  body{{ margin:0; padding:40px 28px 80px; background:var(--noche); color:#fff;
        font:16px/1.5 system-ui,-apple-system,sans-serif; }}
  .wrap{{ max-width:1180px; margin:0 auto; }}
  h1{{ font-size:30px; letter-spacing:-.02em; margin:0 0 6px; }}
  .sub{{ color:var(--sobre); margin:0 0 34px; }}
  h2{{ font-size:19px; margin:0 0 14px; display:flex; align-items:center; gap:12px; }}
  h2 span{{ font:600 13px ui-monospace,monospace; color:var(--noche);
            background:var(--cian); border-radius:99px; padding:3px 10px; }}
  article{{ padding:26px 0; border-top:1px solid rgba(159,186,234,.22); }}
  .tira{{ display:grid; grid-template-columns:repeat(4,1fr); gap:12px; }}
  .tira.historias{{ grid-template-columns:repeat(6,1fr); }}
  .tira img{{ width:100%; border-radius:8px; display:block;
              border:1px solid rgba(159,186,234,.18); }}
  .perfil{{ display:flex; gap:26px; flex-wrap:wrap; align-items:flex-start;
            padding:26px 0 6px; }}
  .perfil a{{ text-align:center; text-decoration:none; color:var(--sobre); font-size:13px; }}
  .redondo{{ width:96px; height:96px; border-radius:50%; object-fit:cover; display:block;
             border:1px solid rgba(159,186,234,.3); margin-bottom:8px; }}
  details{{ margin-top:14px; }}
  summary{{ cursor:pointer; color:var(--cian); font-size:14px; }}
  pre{{ white-space:pre-wrap; background:rgba(255,255,255,.05); padding:16px 18px;
        border-radius:10px; color:var(--sobre); font-size:14px; line-height:1.6;
        border:1px solid rgba(159,186,234,.16); }}
  a img:hover{{ outline:2px solid var(--cian); }}
</style></head>
<body><div class="wrap">
  <h1>Piezas de Instagram</h1>
  <p class="sub">Clic en cualquier imagen para verla a tamaño real.
  Regenerar con <code>python3 marketing/posts.py</code>.</p>
  <div class="perfil">{extras}</div>
  {tiras}
  {"".join(filas)}
</div></body></html>""")
    return OUT / "index.html"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--caso", type=int, help="generar solo este caso (1 a 6)")
    ap.add_argument("--listar", action="store_true", help="ver los casos disponibles")
    ap.add_argument("--perfil", action="store_true", help="generar la foto de perfil")
    ap.add_argument("--destacadas", action="store_true", help="generar las portadas de destacadas")
    ap.add_argument("--historias", choices=sorted(HISTORIAS),
                    help="generar las historias de una destacada")
    ap.add_argument("--reel", action="store_true",
                    help="generar los fotogramas del reel de precios")
    a = ap.parse_args()

    if a.perfil:
        print(f"OK -> {foto_perfil()}")
        return

    if a.reel:
        for r in reel():
            print("OK ->", r)
    if a.historias:
        for r in historias(a.historias):
            print(f"OK -> {r}")
        return

    if a.destacadas:
        for ruta, nombre in portadas_destacadas():
            print(f"OK -> {ruta}  ({nombre})")
        return

    todos = casos()
    if a.listar:
        for i, c in enumerate(todos, 1):
            print(f"  {i}. {c['titulo']}")
        return

    elegidos = [(a.caso, todos[a.caso - 1])] if a.caso else list(enumerate(todos, 1))
    if a.caso and not 1 <= a.caso <= len(todos):
        raise SystemExit(f"El caso debe estar entre 1 y {len(todos)}.")

    plantilla = (BASE / "post.template.html").read_text()
    marca = "data:image/png;base64," + base64.b64encode(
        (ASSETS / "mark.png").read_bytes()).decode()
    OUT.mkdir(parents=True, exist_ok=True)

    for n, caso in elegidos:
        carpeta = OUT / f"caso-{n}"
        carpeta.mkdir(exist_ok=True)
        for paso, pie_izq, pie_der, capa, contenido in laminas(caso, marca):
            doc = (plantilla.replace("{{PIE_IZQ}}", pie_izq)
                            .replace("{{PIE_DER}}", pie_der)
                            .replace("{{FOTO}}", capa)
                            .replace("{{CONTENIDO}}", contenido))
            fuente = carpeta / f"{paso}.html"
            fuente.write_text(doc)
            subprocess.run(
                [CHROME, "--headless", "--disable-gpu", "--hide-scrollbars",
                 f"--window-size={ANCHO},{ALTO}", "--virtual-time-budget=4000",
                 f"--screenshot={carpeta / f'{paso}.png'}", fuente.as_uri()],
                check=True, capture_output=True)
            fuente.unlink()
        (carpeta / "texto.txt").write_text(pie_de_texto(caso, n))
        print(f"OK -> {carpeta}  ({caso['titulo']})")

    print(f"OK -> {galeria(elegidos)}")


if __name__ == "__main__":
    main()
