#!/usr/bin/env python3
"""Cascara comun de las paginas del sitio.

Aqui viven la navegacion, la cabecera de pagina, el cierre y el pie. Los
estilos estan en estilos.css y el codigo comun (menu, referidos, videos y
movimiento) en sitio.js. Cualquier cambio en estas piezas se hace una sola vez
y se propaga al correr build_site.py.
"""

# El numero no se publica como texto: escrito en la pagina lo cosechan los
# robots y termina en listas de spam. Solo viaja dentro del enlace de WhatsApp,
# que es donde hace falta.
WA_NUM = '56948780902'
WA = (f'https://wa.me/{WA_NUM}?text='
      'Hola%20CORYN%2C%20me%20interesa%20cotizar%20un%20proyecto.')
WA_ETIQUETA = 'Conversemos por WhatsApp'
EMAIL = 'contacto@coryndev.com'
BACKEND = 'https://coryn-backend-production.up.railway.app/api/contact'

# Analitica de Vercel: sin cookies y sin identificadores por persona, solo
# cuenta paginas vistas en agregado.
ANALITICA = '<script defer src="/_vercel/insights/script.js"></script>'

# Movimiento: GSAP y ScrollTrigger con version fija. Van con defer y en orden;
# sitio.js los usa si llegaron y, si no, la pagina queda en su estado final.
GSAP = ('<script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/gsap.min.js"></script>\n'
        '<script defer src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.13.0/ScrollTrigger.min.js"></script>')

WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.885-9.885 9.885M20.52 3.449C18.24 1.245 15.24 0 12.045 0 5.463 0 .104 5.359.101 11.945c0 2.096.549 4.14 1.595 5.945L0 24l6.335-1.652a11.93 11.93 0 0 0 5.71 1.454h.006c6.585 0 11.946-5.359 11.949-11.945a11.87 11.87 0 0 0-3.48-8.408"/></svg>'

CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>'
CRUZ = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>'
FLECHA = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
          'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>')

PENDIENTE = '<span class="pendiente">por confirmar</span>'

# Cita de Ivonne Rivera, autorizada para publicarse con nombre y cargo. La usan
# el inicio, correo.html y el caso del sistema: se cambia solo aqui. Si llega un
# testimonio especifico sobre el sistema, reemplaza a este en el caso y en correo.
CITA_IVONNE = ('Llegamos con una idea en la cabeza y salimos con un sistema que hoy '
               'usamos todos los días. Entendieron cómo trabajamos antes de escribir '
               'una sola línea de código.')
FIRMA_IVONNE = 'Ivonne Rivera, gerente de bySIMMED'

# El logo: la C y la pieza que encaja. Trazos del archivo maestro de marca.
C_TRAZO = 'M73.7 69.55A42 42 0 1 1 73.7 14.45L60.11 26.25A24 24 0 1 0 60.11 57.75Z'
P_TRAZO = ('M65.1 33.5H76.9A2.6 2.6 0 0 1 79.5 36.1V47.9A2.6 2.6 0 0 1 76.9 50.5H65.1'
           'A2.6 2.6 0 0 1 62.5 47.9V36.1A2.6 2.6 0 0 1 65.1 33.5Z')


def marca_svg(clase='marca-c'):
    return (f'<svg class="{clase}" viewBox="0 0 79.5 84" aria-hidden="true" focusable="false">'
            f'<path fill="currentColor" d="{C_TRAZO}"/><path fill="#1f5fe0" d="{P_TRAZO}"/></svg>')


MARCA = (f'<a class="marca" href="index.html" aria-label="CORYN, ir al inicio">'
         f'{marca_svg()}<span>CORYN</span></a>')

# (etiqueta, destino, clave para marcar la pagina activa). La marca ya lleva
# al inicio: repetirlo en el menu era un enlace mas que leer.
MENU = [
    ('Servicios', 'servicios.html', 'servicios'),
    ('Qué resolvemos', 'que-resolvemos.html', 'problemas'),
    ('Precios', 'precios.html', 'precios'),
    ('Proceso', 'proceso.html', 'proceso'),
    ('Nosotros', 'nosotros.html', 'nosotros'),
]


def _nav(activa, landing=False):
    if landing:
        # Pagina para enlazar en un mensaje: un solo camino, el boton de
        # WhatsApp del cuerpo. Sin menu ni boton que lo compitan.
        return f'''<header class="nav" id="nav">
  <div class="wrap nav-fila">
    {MARCA}
  </div>
</header>'''
    enlaces = '\n'.join(
        f'      <a href="{href}"{" class=\"activa\" aria-current=\"page\"" if key == activa else ""}>{txt}</a>'
        for txt, href, key in MENU)
    return f'''<header class="nav" id="nav">
  <div class="wrap nav-fila">
    {MARCA}
    <nav class="nav-links" id="navLinks" aria-label="Principal">
{enlaces}
    </nav>
    <div class="nav-der">
      <a class="btn btn-wa btn-chico nav-cta" href="{WA}" target="_blank" rel="noopener" aria-label="Conversemos por WhatsApp">{WA_SVG}<span>Conversemos</span></a>
      <button class="burger" id="burger" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="navLinks"><span></span><span></span></button>
    </div>
  </div>
</header>'''


def cierre(titulo='Cuéntanos qué te está costando tiempo.',
           texto='Media hora, sin costo. Te decimos con honestidad si podemos '
                 'ayudarte y cuánto costaría.',
           secundario='<a class="enlace enlace-claro" href="contacto.html">Prefiero un formulario</a>'):
    """El mismo cierre en todo el sitio: antes cada pagina repetia la oferta
    de la primera reunion con otras palabras."""
    return f'''<section class="cierre">
  <div class="wrap cierre-grid">
    <div>
      <h2>{titulo}</h2>
      <p>{texto}</p>
      <div class="acciones">
        <a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{WA_SVG}{WA_ETIQUETA}</a>
        {secundario}
      </div>
    </div>
    <div class="cierre-marca" aria-hidden="true">
      <svg viewBox="0 0 79.5 84" focusable="false"><path class="c" d="{C_TRAZO}"/><path class="p" d="{P_TRAZO}"/></svg>
    </div>
  </div>
</section>'''


PIE = f'''<footer class="pie">
  <div class="wrap">
    <div class="pie-cols">
      <div class="pie-marca">
        {MARCA}
        <p>Software a medida para negocios que necesitan que la herramienta calce
        con su forma de trabajar.</p>
      </div>
      <div>
        <h4>Casos</h4>
        <ul>
          <li><a href="caso-bysimmed-sistema.html">bySIMMED &middot; sistema</a></li>
          <li><a href="caso-bysimmed.html">bySIMMED &middot; sitio web</a></li>
          <li><a href="caso-avenprop.html">AvenProp</a></li>
        </ul>
        <h4>Productos propios</h4>
        <ul>
          <li><a href="producto-enumera.html">Enumera</a></li>
          <li><a href="producto-precioradar.html">PrecioRadar</a></li>
        </ul>
      </div>
      <div>
        <h4>Empresa</h4>
        <ul>
          <li><a href="servicios.html">Servicios</a></li>
          <li><a href="que-resolvemos.html">Qué resolvemos</a></li>
          <li><a href="precios.html">Precios</a></li>
          <li><a href="proceso.html">Proceso</a></li>
          <li><a href="nosotros.html">Nosotros</a></li>
        </ul>
      </div>
      <div>
        <h4>Contacto</h4>
        <ul>
          <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></li>
          <li><a href="contacto.html">Formulario</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
        <p class="pie-nota">Respondemos en menos de 24 horas h&aacute;biles.</p>
      </div>
    </div>
    <div class="pie-base">
      <span>&copy; 2026 CORYN. Todos los derechos reservados.</span>
      <a href="privacidad.html">Pol&iacute;tica de privacidad</a>
    </div>
  </div>
</footer>'''

# Se pone antes de pintar: si el navegador no pide menos movimiento, marca la
# pagina para que lo que aparece con el scroll arranque escondido. Si sitio.js
# no confirma en 3,5 s (la libreria no cargo, hubo un error), se quita la marca
# y todo queda visible en su estado final.
HEAD_MOV = '''<script>
  (function (d) {
    if (window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    d.documentElement.classList.add('mov');
    setTimeout(function () { if (!window.CORYN_MOV) d.documentElement.classList.remove('mov'); }, 3500);
  })(document);
</script>'''


def _firma(nombre):
    """Huella del contenido de un archivo estatico.

    Se anexa al enlace para que, al cambiarlo, el navegador descargue la
    version nueva en vez de reutilizar la que tenga en cache.
    """
    import hashlib, pathlib as _pl
    f = _pl.Path(__file__).parent / nombre
    if not f.exists():
        return ''
    return hashlib.sha1(f.read_bytes()).hexdigest()[:8]


def _medidas(ruta):
    """Alto y ancho reales de la imagen social, para que WhatsApp y Facebook
    reserven el espacio de la tarjeta sin bajar la imagen primero."""
    import pathlib as _pl
    f = _pl.Path(__file__).parent / ruta
    if not f.exists():
        return 1200, 630
    try:
        from PIL import Image
        with Image.open(f) as im:
            return im.width, im.height
    except Exception:
        return 1200, 630


def video(nombre, proporcion='4/3', clase='marco-video'):
    """Video en loop, mudo y sin controles, en un marco de papel.

    preload="none" y el poster (la misma foto de la que salio el video) hacen
    que no se baje nada hasta que entra en pantalla; sitio.js lo reproduce solo
    mientras se ve y nunca si el navegador pide menos movimiento.
    """
    return f'''<figure class="{clase}" style="--ar:{proporcion}">
  <video class="vid" muted loop playsinline preload="none" poster="assets/{nombre}.webp" aria-hidden="true">
    <source src="assets/{nombre}.webm" type="video/webm">
    <source src="assets/{nombre}.mp4" type="video/mp4">
  </video>
</figure>'''


def render(titulo, descripcion, cuerpo, activa='', og_img='assets/og.jpg',
           og_tipo='website', js_extra='', canonico='', clase_body='',
           ld_extra=(), preload=(), landing=False):
    """Arma una pagina completa a partir del cuerpo.

    canonico:   ruta de la pagina para el <link rel=canonical> ('' = portada).
    clase_body: clase en <body>, para ajustar una pagina entera.
    ld_extra:   datos estructurados propios de la pagina (migas, FAQ, caso).
    preload:    imagenes que conviene pedir antes de que el navegador
                descubra el <img>. Solo la que abre la pagina.
    landing:    cabecera solo con la marca, para paginas que se enlazan en un
                mensaje y tienen un unico boton.
    """
    import json as _json
    bloques_ld = ''.join(
        '<script type="application/ld+json">\n'
        + _json.dumps(d, ensure_ascii=False, indent=2) + '\n</script>\n'
        for d in ld_extra)
    precargas = ''.join(
        f'<link rel="preload" as="image" href="{h}" fetchpriority="high">\n'
        for h in preload)
    og_img_abs = og_img.lstrip('./')
    og_w, og_h = _medidas(og_img_abs)
    url_abs = f'https://coryndev.com/{canonico}'
    clase = f' class="{clase_body}"' if clase_body else ''
    return f'''<!DOCTYPE html>
<html lang="es-CL">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<link rel="canonical" href="{url_abs}">
<meta name="theme-color" content="#eceff5">
<link rel="icon" href="assets/favicon-48.png" type="image/png">
<link rel="icon" href="assets/mark.webp" type="image/webp">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<meta property="og:type" content="{og_tipo}">
<meta property="og:site_name" content="CORYN">
<meta property="og:locale" content="es_CL">
<meta property="og:url" content="{url_abs}">
<meta property="og:title" content="{titulo}">
<meta property="og:description" content="{descripcion}">
<meta property="og:image" content="https://coryndev.com/{og_img_abs}">
<meta property="og:image:width" content="{og_w}">
<meta property="og:image:height" content="{og_h}">
<meta property="og:image:alt" content="CORYN, desarrollo de software a medida en Chile">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{titulo}">
<meta name="twitter:description" content="{descripcion}">
<meta name="twitter:image" content="https://coryndev.com/{og_img_abs}">
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@graph": [
    {{
      "@type": "ProfessionalService",
      "@id": "https://coryndev.com/#coryn",
      "name": "CORYN",
      "description": "Desarrollo de software a medida para pymes en Chile: sistemas de gestión, sitios web, tiendas online, aplicaciones móviles e integraciones.",
      "slogan": "Software a medida de cómo trabajas",
      "url": "https://coryndev.com/",
      "logo": {{
        "@type": "ImageObject",
        "url": "https://coryndev.com/assets/icon-512.png",
        "width": 512,
        "height": 512
      }},
      "image": "https://coryndev.com/assets/og.jpg",
      "email": "contacto@coryndev.com",
      "address": {{ "@type": "PostalAddress", "addressCountry": "CL" }},
      "areaServed": {{ "@type": "Country", "name": "Chile" }},
      "knowsLanguage": "es-CL",
      "currenciesAccepted": "CLP",
      "priceRange": "$$",
      "serviceType": [
        "Desarrollo de software a medida",
        "Sistemas de gestión ERP y CRM",
        "Desarrollo de páginas web",
        "Desarrollo de tiendas online",
        "Desarrollo de aplicaciones móviles",
        "Integraciones y automatizaciones"
      ],
      "contactPoint": {{
        "@type": "ContactPoint",
        "contactType": "ventas",
        "email": "contacto@coryndev.com",
        "areaServed": "CL",
        "availableLanguage": "es"
      }},
      "sameAs": ["https://www.instagram.com/coryn.studio/"]
    }},
    {{
      "@type": "WebSite",
      "@id": "https://coryndev.com/#sitio",
      "url": "https://coryndev.com/",
      "name": "CORYN",
      "inLanguage": "es-CL",
      "publisher": {{ "@id": "https://coryndev.com/#coryn" }}
    }},
    {{
      "@type": "WebPage",
      "@id": "{url_abs}#pagina",
      "url": "{url_abs}",
      "name": "{titulo}",
      "description": "{descripcion}",
      "inLanguage": "es-CL",
      "isPartOf": {{ "@id": "https://coryndev.com/#sitio" }},
      "about": {{ "@id": "https://coryndev.com/#coryn" }}
    }}
  ]
}}
</script>
{bloques_ld}{precargas}<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600..800&family=Caveat:wght@600;700&family=Schibsted+Grotesk:wght@400..700&display=swap">
<link rel="stylesheet" href="estilos.css?v={_firma('estilos.css')}">
{HEAD_MOV}
</head>
<body{clase}>
<a class="saltar" href="#contenido">Saltar al contenido</a>

{_nav(activa, landing)}

<main id="contenido">
{cuerpo}
</main>

{PIE}

{GSAP}
<script defer src="sitio.js?v={_firma('sitio.js')}"></script>
{js_extra}
{ANALITICA}
</body>
</html>
'''


def cabecera(titulo, bajada, migas=None, visual='', acciones=''):
    """Cabecera de pagina interior: el titulo carga solo, sin etiqueta encima.

    migas:    [(nombre, href|None), ...] para las paginas que cuelgan de otra.
    visual:   el grafico de la pagina (video, imagen o pieza propia).
    acciones: botones bajo la bajada.
    """
    # El punto final del titulo es la pieza del logo: un cuadrado azul.
    if titulo.endswith('.'):
        titulo = titulo[:-1] + '<span class="punto">.</span>'
    m = ''
    if migas:
        partes = ' <span aria-hidden="true">/</span> '.join(
            f'<a href="{h}">{t}</a>' if h else f'<span aria-current="page">{t}</span>'
            for t, h in migas)
        m = f'      <nav class="migas" aria-label="Estás en">{partes}</nav>\n'
    clase = 'cabeza-grid con-visual' if visual else 'cabeza-grid'
    v = f'\n    <div class="cabeza-visual">\n{visual}\n    </div>' if visual else ''
    a = f'\n      <div class="acciones">{acciones}</div>' if acciones else ''
    return f'''<section class="cabeza">
  <div class="wrap {clase}">
    <div class="cabeza-texto">
{m}      <h1>{titulo}</h1>
      <p class="bajada">{bajada}</p>{a}
    </div>{v}
  </div>
</section>'''
