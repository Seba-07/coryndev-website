#!/usr/bin/env python3
"""Cascara comun de las paginas del sitio (v2).

Aqui viven la cabecera, la navegacion y el pie. Cualquier cambio en esos
tres se hace una sola vez y se propaga al correr build_site.py.
"""

# El numero no se publica como texto: escrito en la pagina lo cosechan los
# robots y termina en listas de spam. Solo viaja dentro del enlace de WhatsApp,
# que es donde hace falta.
WA_NUM = '56948780902'
WA = (f'https://wa.me/{WA_NUM}?text='
      'Hola%20CORYN%2C%20me%20interesa%20cotizar%20un%20proyecto.')
WA_ETIQUETA = 'Escríbenos por WhatsApp'
EMAIL = 'contacto@coryndev.com'
BACKEND = 'https://coryn-backend-production.up.railway.app/api/contact'

# Analitica de Vercel: sin cookies y sin identificadores por persona, solo
# cuenta paginas vistas en agregado. Hay que activarla en el panel del proyecto
# (Analytics > Enable); mientras no lo este el script responde 404 y la pagina
# sigue funcionando igual.
ANALITICA = '<script defer src="/_vercel/insights/script.js"></script>'

WA_SVG = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.472 '
          '14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 '
          '1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 '
          '0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 '
          '2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 '
          '1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 '
          '7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 '
          '0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 '
          '9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.885-9.885 9.885M20.52 3.449C18.24 1.245 15.24 0 '
          '12.045 0 5.463 0 .104 5.359.101 11.945c0 2.096.549 4.14 1.595 5.945L0 24l6.335-1.652a11.93 '
          '11.93 0 0 0 5.71 1.454h.006c6.585 0 11.946-5.359 11.949-11.945a11.87 11.87 0 0 0-3.48-8.408"/></svg>')

CHECK = '<svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>'
CRUZ = '<svg viewBox="0 0 24 24"><path d="M18 6 6 18M6 6l12 12"/></svg>'
FLECHA = '<svg viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

PENDIENTE = '<span class="pendiente">por confirmar</span>'

# (etiqueta, destino, clave para marcar la pagina activa)
MENU = [
    ('Inicio', 'index.html', 'inicio'),
    ('Servicios', 'servicios.html', 'servicios'),
    ('Qué resolvemos', 'que-resolvemos.html', 'problemas'),
    ('Proceso', 'proceso.html', 'proceso'),
    ('Nosotros', 'nosotros.html', 'nosotros'),
]


def _nav(activa):
    enlaces = '\n'.join(
        f'        <a href="{href}"{" class=\"activa\"" if key == activa else ""}>{txt}</a>'
        for txt, href, key in MENU)
    return f'''<header class="nav" id="nav">
  <div class="wrap">
    <a class="brand" href="index.html">
      <img src="assets/mark.webp" alt="" width="28" height="26">
      <span>CORYN</span>
    </a>
    <nav class="nav-links" id="navLinks">
{enlaces}
    </nav>
    <div class="nav-right">
      <a class="btn btn-solid btn-sm nav-cta" href="contacto.html">Conversemos</a>
      <button class="burger" id="burger" aria-label="Abrir menú" aria-expanded="false" aria-controls="navLinks">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>'''


def _cierre(titulo, texto, boton_extra='', clase_cierre=''):
    return f'''<section class="close{clase_cierre}">
  <div class="wrap">
    <p class="eyebrow">Siguiente paso</p>
    <h2>{titulo}</h2>
    <p>{texto}</p>
    <div class="actions">
      <a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">{WA_SVG}
        {WA_ETIQUETA}
      </a>
      {boton_extra or '<a class="btn btn-ghost" href="contacto.html">Enviar un mensaje</a>'}
    </div>
    <div class="lines">
      <a href="mailto:{EMAIL}">{EMAIL}</a>
      <a href="https://coryndev.com">coryndev.com</a>
    </div>
  </div>
</section>'''


PIE = f'''<footer class="foot">
  <div class="wrap">
    <div class="cols">
      <div class="foot-marca">
        <a class="brand" href="index.html">
          <img src="assets/mark-claro.webp" alt="" width="28" height="26">
          <span>CORYN</span>
        </a>
        <p>Software 100% personalizado para negocios que necesitan que la
        herramienta calce con su forma de trabajar.</p>
      </div>
      <div>
        <h4>Casos</h4>
        <ul>
          <li><a href="caso-bysimmed.html">bySIMMED</a></li>
          <li><a href="caso-avenprop.html">AvenProp</a></li>
          <li><a href="caso-precioradar.html">PrecioRadar</a></li>
        </ul>
      </div>
      <div>
        <h4>Empresa</h4>
        <ul>
          <li><a href="servicios.html">Servicios</a></li>
          <li><a href="que-resolvemos.html">Qué resolvemos</a></li>
          <li><a href="proceso.html">Proceso</a></li>
          <li><a href="nosotros.html">Nosotros</a></li>
        </ul>
      </div>
      <div>
        <h4>Contacto</h4>
        <ul>
          <li><a href="contacto.html">Enviar un mensaje</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
        <p class="foot-nota">Respondemos en menos de 24 horas h&aacute;biles.</p>
      </div>
    </div>
    <div class="base">
      <span>&copy; 2026 CORYN. Todos los derechos reservados.</span>
      <span><a href="privacidad.html">Pol&iacute;tica de privacidad</a></span>
    </div>
  </div>
</footer>'''

JS_COMUN = '''<script>
  // Fondo de la barra al desplazar
  var nav = document.getElementById('nav');
  if (!nav.classList.contains('solid-fija')) {
    var onScroll = function () { nav.classList.toggle('solid', window.scrollY > 24); };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  // Menu de celular
  var burger = document.getElementById('burger');
  var links = document.getElementById('navLinks');
  burger.addEventListener('click', function () {
    var abierto = document.body.classList.toggle('menu-abierto');
    burger.setAttribute('aria-expanded', abierto ? 'true' : 'false');
    burger.setAttribute('aria-label', abierto ? 'Cerrar menú' : 'Abrir menú');
  });
  links.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') {
      document.body.classList.remove('menu-abierto');
      burger.setAttribute('aria-expanded', 'false');
    }
  });
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && document.body.classList.contains('menu-abierto')) {
      document.body.classList.remove('menu-abierto');
      burger.setAttribute('aria-expanded', 'false');
      burger.focus();
    }
  });

  // Codigo de referido. Llega en la URL desde el QR del volante o desde el link
  // que comparte un referidor. Sin esto el codigo moria en la primera pagina:
  // la persona navegaba, se convencia, apretaba WhatsApp y el mensaje salia sin
  // marca, asi que no habia forma de saber quien la trajo.
  window.CORYN = window.CORYN || {};
  (function () {
    var CLAVE = 'coryn_ref', DIAS = 30;

    // El valor termina dentro de un mensaje de WhatsApp y del formulario, asi
    // que solo se aceptan letras, numeros y guiones.
    function limpio (v) {
      return (v || '').trim().slice(0, 24).replace(/[^A-Za-z0-9_-]/g, '');
    }

    function guardado () {
      try {
        var d = JSON.parse(localStorage.getItem(CLAVE) || 'null');
        if (d && d.ref && Date.now() < d.vence) return d.ref;
        if (d) localStorage.removeItem(CLAVE);
      } catch (e) { /* modo privado, o el navegador bloquea el storage */ }
      return '';
    }

    var deUrl = '';
    try { deUrl = limpio(new URLSearchParams(location.search).get('ref')); } catch (e) {}

    if (deUrl) {
      try {
        localStorage.setItem(CLAVE, JSON.stringify({
          ref: deUrl, vence: Date.now() + DIAS * 864e5
        }));
      } catch (e) {}
    }

    var ref = deUrl || guardado();
    window.CORYN.ref = ref;
    if (!ref) return;

    // Si la analitica esta activa, deja constancia de que la visita llego con
    // codigo. Se encola con el stub que recomienda Vercel porque su script
    // carga con defer y todavia no existe en este punto.
    try {
      window.va = window.va || function () {
        (window.vaq = window.vaq || []).push(arguments);
      };
      window.va('event', { name: 'referido', data: { ref: ref } });
    } catch (e) {}

    // Se marca en el clic y no al cargar la pagina: el estimador rehace su
    // enlace de WhatsApp cada vez que cambias la seleccion, y de esta forma
    // tambien queda marcado sin tener que engancharse a su codigo.
    document.addEventListener('click', function (e) {
      var el = e.target;
      if (el && el.nodeType !== 1) el = el.parentElement;
      var a = el && el.closest ? el.closest('a[href*="wa.me"]') : null;
      if (!a) return;
      var u;
      try { u = new URL(a.href); } catch (err) { return; }
      var t = u.searchParams.get('text') || 'Hola CORYN';
      if (t.indexOf('(Ref:') > -1) return;
      // Se rearma a mano y no con searchParams.set, que escribe los espacios
      // como "+"; el resto del sitio los manda como %20.
      a.href = u.origin + u.pathname + '?text=' +
               encodeURIComponent(t + ' (Ref: ' + ref + ')');
    }, true);
  })();

  // Aparicion progresiva, con red de seguridad si el observer no dispara
  (function () {
    if (!document.documentElement.classList.contains('js-rv')) return;
    var els = document.querySelectorAll('.rv');
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
    els.forEach(function (el, i) {
      el.style.transitionDelay = (Math.min(i % 4, 3) * 60) + 'ms';
      io.observe(el);
    });
    setTimeout(function () {
      els.forEach(function (el) { el.classList.add('in'); });
      io.disconnect();
    }, 2000);
  })();
</script>'''


def _firma_css():
    """Huella del contenido de styles-v2.css.

    Se anexa al enlace de la hoja para que, al cambiar los estilos, el navegador
    descargue la version nueva en vez de reutilizar la que tenga en cache. Sin
    esto un visitante que ya entro antes ve el HTML nuevo con los estilos viejos:
    lo unico que conserva estilo son las secciones que ya existian.
    """
    import hashlib, pathlib as _pl
    hoja = _pl.Path(__file__).parent / 'styles-v2.css'
    if not hoja.exists():
        return ''
    return hashlib.sha1(hoja.read_bytes()).hexdigest()[:8]


def _medidas(ruta):
    """Alto y ancho reales de la imagen social.

    Declararlos deja que Facebook y WhatsApp reserven el espacio de la tarjeta
    sin bajar la imagen primero. Fijarlos a mano seria peor que omitirlos: las
    fichas de caso no usan la og.jpg de 1200x630.
    """
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


def render(titulo, descripcion, cuerpo, activa='', og_img='assets/og.jpg',
           og_tipo='website', js_extra='', nav_solida=False, canonico='',
           clase_body='', ld_extra=(), preload=()):
    """Arma una pagina completa a partir del cuerpo.

    canonico:   ruta de la pagina para el <link rel=canonical> ('' = portada).
    clase_body: clase en <body>, para dar tono a una pagina entera sin tener
                que etiquetar cada seccion a mano.
    ld_extra:   datos estructurados propios de la pagina (migas, FAQ, caso).
                El bloque de empresa va en todas; esto se suma.
    preload:    imagenes que conviene pedir antes de que el navegador
                descubra el <img>. Solo la que abre la pagina: precargar de
                mas retrasa justamente lo que se queria adelantar.
    """
    import json as _json
    bloques_ld = ''.join(
        '<script type="application/ld+json">\n'
        + _json.dumps(d, ensure_ascii=False, indent=2) + '\n</script>\n'
        for d in ld_extra)
    precargas = ''.join(
        f'<link rel="preload" as="image" href="{h}" fetchpriority="high">\n'
        for h in preload)
    firma = _firma_css()
    og_img_abs = og_img.lstrip('./')
    og_w, og_h = _medidas(og_img_abs)
    nav = _nav(activa)
    if nav_solida:
        nav = nav.replace('class="nav" id="nav"', 'class="nav solid solid-fija" id="nav"')
    url_abs = f'https://coryndev.com/{canonico}'
    return f'''<!DOCTYPE html>
<html lang="es-CL">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<link rel="canonical" href="{url_abs}">
<meta name="theme-color" content="#070e20">
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
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="styles-v2.css?v={firma}">
<script>
  if ('IntersectionObserver' in window &&
      !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {{
    document.documentElement.classList.add('js-rv');
  }}
</script>
</head>
<body{" class=\"" + clase_body + "\"" if clase_body else ""}>

{nav}

{cuerpo}

{PIE}

{JS_COMUN}
{js_extra}
{ANALITICA}
</body>
</html>
'''


def cabecera(titulo, bajada, eyebrow='', migas=None):
    """Cabecera oscura de pagina interior."""
    m = ''
    if migas:
        partes = ' / '.join(
            f'<a href="{h}">{t}</a>' if h else t for t, h in migas)
        m = f'    <p class="crumbs">{partes}</p>\n'
    e = f'    <p class="eyebrow">{eyebrow}</p>\n' if eyebrow else ''
    return f'''<section class="page-head">
  <div class="wrap">
{m}{e}    <h1>{titulo}</h1>
    <p>{bajada}</p>
  </div>
</section>'''
