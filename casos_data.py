#!/usr/bin/env python3
"""Contenido de las paginas de caso.

Para agregar un caso nuevo, sumalo a CASOS y corre:  python3 build_site.py
La estructura y el diseno de la pagina viven en build_site.py / site_shell.py.
"""

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
