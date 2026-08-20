#!/usr/bin/env python3
"""Genera las paginas de caso a partir de una plantilla comun.

Uso:  python3 build_casos.py
Salida: caso-<slug>.html en la raiz del sitio.

Para agregar un caso nuevo, sumalo a la lista CASOS y vuelve a correrlo.
Los <span class="pendiente"> marcan datos que faltan por confirmar.
"""
import pathlib

WA = ('https://wa.me/56933569725?text='
      'Hola%20CORYN%2C%20me%20interesa%20cotizar%20un%20proyecto.')

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

PENDIENTE = '<span class="pendiente">por confirmar</span>'

CASOS = [
 {
  'slug': 'bysimmed',
  'titulo': 'bySIMMED',
  'sector': 'Salud',
  'tipo': 'Sitio web y catálogo',
  'meta_desc': 'Caso CORYN: sitio web multiidioma y catálogo para bySIMMED, '
               'fabricante chileno de simuladores médicos de alta fidelidad.',
  'h1': 'Un fabricante chileno de simuladores médicos que necesitaba vender fuera de Chile',
  'lead': 'bySIMMED fabrica simuladores de alta fidelidad con tejido real-análogo, '
          'diseñados por médicos especialistas. El producto era bueno; el problema '
          'era que nadie afuera podía verlo.',
  'sitio': 'bysimmed.com',
  'sitio_url': 'https://www.bysimmed.com/es',
  'figura': 'assets/work-bysimmed.webp',
  'figura_alt': 'Portada del sitio de bySIMMED',
  'figura_pie': 'La portada abre con el producto en uso, no con una foto de stock: '
                'es lo que un médico especialista necesita ver primero.',
  'ancho': 1400, 'alto': 875,
  'bloques': [
   ('El problema',
    ['<p>bySIMMED vende a un público muy específico: médicos especialistas y centros '
     'de formación clínica, en varios países. Ese comprador no decide por precio, '
     'decide por detalle técnico — con qué instrumental es compatible, qué '
     'procedimientos permite entrenar, qué tan realista es el tejido.</p>',
     '<p>Nada de eso estaba disponible de forma ordenada, y menos en el idioma del '
     'comprador. Cada consulta terminaba siendo una conversación desde cero.</p>']),
   ('Qué construimos',
    ['<p>Un sitio con catálogo, pensado como herramienta de venta técnica más que '
     'como folleto:</p>',
     '<ul>'
     '<li>Catálogo por líneas de producto, con las especificaciones que el '
     'especialista busca antes de preguntar.</li>'
     '<li>Compatibilidad declarada con el instrumental clínico real que ya usan '
     'en sus centros.</li>'
     '<li>Sitio completo en español, inglés y portugués, para los mercados donde '
     'venden.</li>'
     '<li>Agenda de demostraciones: el paso natural después de revisar el catálogo.</li>'
     '</ul>']),
   ('Las decisiones que importaron',
    ['<p>La portada abre con el producto en uso, en un procedimiento real. Para este '
     'comprador eso comunica más que cualquier titular.</p>',
     '<p>El multiidioma no se resolvió con un traductor automático encima: cada '
     'idioma es una versión propia del sitio, indexable por buscadores, porque '
     'buena parte de estos clientes llegan buscando un procedimiento específico '
     'en su idioma.</p>']),
  ],
 },
 {
  'slug': 'avenprop',
  'titulo': 'AvenProp',
  'sector': 'Inmobiliario',
  'tipo': 'Plataforma web',
  'meta_desc': 'Caso CORYN: plataforma web de corretaje y seguros para AvenProp, '
               'con buscador de propiedades por comuna y tipo.',
  'h1': 'Una corredora que perdía interesados porque sus propiedades vivían en publicaciones sueltas',
  'lead': 'AvenProp compra, vende y arrienda propiedades en Santiago, y además '
          'asegura lo que vale la pena proteger. Dos negocios que se potencian, '
          'repartidos en portales que no controlaban.',
  'sitio': 'avenprop.cl',
  'sitio_url': 'https://avenprop.vercel.app/',
  'figura': 'assets/work-avenprop.webp',
  'figura_alt': 'Portada del sitio de AvenProp con el buscador de propiedades',
  'figura_pie': 'El buscador va inmediatamente bajo la portada: quien llega buscando '
                'casa no debería tener que navegar para empezar.',
  'ancho': 1400, 'alto': 875,
  'bloques': [
   ('El problema',
    ['<p>Publicar en portales inmobiliarios funciona para aparecer, pero el interesado '
     'nunca llega a conocer a la corredora: llega a una ficha, entre decenas de otras '
     'iguales, y el contacto queda del lado del portal.</p>',
     '<p>Además dejaba fuera la mitad del negocio. AvenProp también corre seguros, '
     'y un portal de propiedades no tiene dónde contar eso.</p>']),
   ('Qué construimos',
    ['<p>Una plataforma propia donde las dos líneas conviven:</p>',
     '<ul>'
     '<li>Buscador con filtros por comuna y tipo de propiedad, separado en comprar, '
     'arrendar y asegurar.</li>'
     '<li>Fichas de propiedad con la información que decide una visita: superficie, '
     'dormitorios, valor en UF y ubicación.</li>'
     '<li>Captación de interesados directa, sin intermediario que se quede con el contacto.</li>'
     '<li>Sección de seguros integrada al mismo recorrido, no como un anexo.</li>'
     '</ul>']),
   ('Las decisiones que importaron',
    ['<p>El buscador quedó inmediatamente bajo la portada. Alguien que llega buscando '
     'casa no debería tener que entender la estructura del sitio antes de empezar.</p>',
     '<p>Los tres modos — comprar, arrendar, asegurar — comparten un mismo buscador '
     'en vez de vivir en secciones separadas. Es la forma en que el visitante piensa '
     'su problema, y de paso expone el negocio de seguros a gente que llegó por otra cosa.</p>']),
  ],
 },
 {
  'slug': 'precioradar',
  'titulo': 'PrecioRadar',
  'sector': 'Retail y consumo',
  'tipo': 'Aplicación móvil · Producto propio',
  'meta_desc': 'Caso CORYN: PrecioRadar, aplicación móvil de ahorro con lectura '
               'automática de boletas y comparación de precios entre supermercados.',
  'h1': 'De una idea propia a una aplicación publicada en las tiendas',
  'lead': 'PrecioRadar es producto nuestro, no un encargo. Lo construimos para '
          'resolver algo cotidiano y, de paso, para tener dónde demostrar de qué '
          'somos capaces sin depender del permiso de un cliente.',
  'sitio': 'Ver ficha del producto',
  'sitio_url': 'precioradar.html',
  'figura': 'assets/app-buscar.webp',
  'figura_alt': 'Pantallas de la aplicación PrecioRadar',
  'figura_pie': 'Buscador por categorías y lector de boletas: las dos entradas '
                'principales de la aplicación.',
  'ancho': 520, 'alto': 1035,
  'bloques': [
   ('El problema',
    ['<p>Comparar precios entre supermercados es una tarea que todos saben que '
     'conviene y casi nadie hace, porque el esfuerzo no compensa el ahorro de una '
     'compra individual.</p>',
     '<p>La única forma de que funcione es que registrar lo que compraste no cueste '
     'nada. Si hay que tipear producto por producto, la aplicación se abandona la '
     'segunda semana.</p>']),
   ('Qué construimos',
    ['<p>Una aplicación para iOS y Android donde la boleta hace el trabajo:</p>',
     '<ul>'
     '<li>Lectura automática de boletas desde la cámara: se fotografía y los '
     'productos quedan registrados.</li>'
     '<li>Comparación de precios entre cadenas, organizada por categorías.</li>'
     '<li>Control de gasto mensual, con el detalle de cuánto se llevó cada compra.</li>'
     '<li>Listas de compra y un sistema de puntos que premia registrar las boletas.</li>'
     '</ul>']),
   ('Las decisiones que importaron',
    ['<p>Todo el diseño gira en torno a bajar el costo de registrar. La cámara es una '
     'de las cinco entradas fijas de la aplicación, no una función escondida en un menú.</p>',
     '<p>Los puntos no son un adorno: resuelven el problema real de que el beneficio '
     'de comparar precios aparece recién después de varias compras. Dan una '
     'recompensa inmediata mientras se acumula el historial que hace útil al resto '
     'de la aplicación.</p>',
     '<p>Al ser producto propio, lo llevamos completo: idea, diseño, desarrollo, '
     'publicación en las tiendas y las actualizaciones posteriores.</p>']),
  ],
 },
]


def ficha(c):
    filas = [('Cliente', 'Producto propio de CORYN' if c['slug'] == 'precioradar' else c['titulo']),
             ('Sector', c['sector']),
             ('Tipo de proyecto', c['tipo']),
             ('Año', PENDIENTE),
             ('Estado', 'En línea')]
    dl = '\n'.join(f'        <dt>{k}</dt><dd>{v}</dd>' for k, v in filas)
    externo = ' target="_blank" rel="noopener"' if c['sitio_url'].startswith('http') else ''
    return f'''      <aside class="ficha">
        <h3>Ficha del proyecto</h3>
        <dl>
{dl}
        </dl>
        <a class="btn btn-solid" href="{c['sitio_url']}"{externo}>{c['sitio']}</a>
      </aside>'''


def cuerpo(c):
    out = []
    for i, (titulo, parrafos) in enumerate(c['bloques']):
        out.append(f'        <h2>{titulo}</h2>')
        out.extend('        ' + p for p in parrafos)
        if i == 0:
            out.append(f'''        <figure>
          <div class="browser-lite">
            <div class="bar"><i></i><i></i><i></i></div>
            <img src="{c['figura']}" alt="{c['figura_alt']}" width="{c['ancho']}" height="{c['alto']}">
          </div>
          <figcaption>{c['figura_pie']}</figcaption>
        </figure>''')
    return '\n'.join(out)


PLANTILLA = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{titulo} — Caso de proyecto | CORYN</title>
<meta name="description" content="{meta_desc}">
<link rel="icon" href="assets/mark.webp" type="image/webp">
<meta property="og:type" content="article">
<meta property="og:title" content="{titulo} — Caso de proyecto | CORYN">
<meta property="og:description" content="{meta_desc}">
<meta property="og:image" content="https://coryndev.com/{figura}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<link rel="stylesheet" href="styles-v2.css">
</head>
<body>

<header class="nav solid" id="nav">
  <div class="wrap">
    <a class="brand" href="index-nuevo.html">
      <img src="assets/mark.webp" alt="" width="28" height="26">
      <span>CORYN</span>
    </a>
    <nav class="nav-links">
      <a href="index-nuevo.html#sectores">Sectores</a>
      <a href="index-nuevo.html#casos">Casos</a>
      <a href="index-nuevo.html#cotizar">Cómo cotizamos</a>
      <a href="servicios.html">Servicios</a>
      <a href="por-que-coryn.html">Nosotros</a>
    </nav>
    <a class="btn btn-solid btn-sm" href="contacto.html">Conversemos</a>
  </div>
</header>

<section class="page-head">
  <div class="wrap">
    <p class="crumbs"><a href="index-nuevo.html">Inicio</a> / <a href="index-nuevo.html#casos">Casos</a> / {titulo}</p>
    <p class="eyebrow">{sector} &middot; {tipo}</p>
    <h1>{h1}</h1>
    <p>{lead}</p>
  </div>
</section>

<section>
  <div class="wrap caso-grid">
    <article class="caso-body">
{cuerpo}
    </article>
{ficha}
  </div>
</section>

<section class="close">
  <div class="wrap">
    <p class="eyebrow">¿Tu caso se parece?</p>
    <h2>Conversemos 30 minutos, sin costo.</h2>
    <p>Cuéntanos tu situación y te decimos con honestidad qué se puede resolver
    con software, qué conviene priorizar y cuánto costaría hacerlo bien.</p>
    <div class="actions">
      <a class="btn btn-wa" href="{wa}" target="_blank" rel="noopener">{wa_svg}
        +56 9 3356 9725
      </a>
      <a class="btn btn-ghost" href="index-nuevo.html#casos">Ver otros casos</a>
    </div>
    <div class="lines">
      <a href="mailto:coryn.software@gmail.com">coryn.software@gmail.com</a>
      <a href="https://coryndev.com">coryndev.com</a>
    </div>
  </div>
</section>

<footer class="foot">
  <div class="wrap">
    <div class="cols">
      <div>
        <a class="brand" href="index-nuevo.html">
          <img src="assets/mark.webp" alt="" width="28" height="26">
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
          <li><a href="proceso.html">Proceso</a></li>
          <li><a href="por-que-coryn.html">Nosotros</a></li>
          <li><a href="contacto.html">Contacto</a></li>
        </ul>
      </div>
    </div>
    <div class="base">
      <span>&copy; 2026 CORYN. Todos los derechos reservados.</span>
      <span><a href="precioradar-privacy.html" style="text-decoration:none">Política de privacidad</a></span>
    </div>
  </div>
</footer>

</body>
</html>
'''

if __name__ == '__main__':
    raiz = pathlib.Path(__file__).parent
    for c in CASOS:
        html = PLANTILLA.format(cuerpo=cuerpo(c), ficha=ficha(c),
                                wa=WA, wa_svg=WA_SVG, **c)
        destino = raiz / f"caso-{c['slug']}.html"
        destino.write_text(html)
        print(f'  {destino.name}  ({len(html) // 1024} KB)')
