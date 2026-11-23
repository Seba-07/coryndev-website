#!/usr/bin/env python3
"""Contenido de las paginas de caso y de productos propios.

Para agregar un caso nuevo, sumalo a CASOS y corre:  python3 build_site.py
Los productos de CORYN van en PRODUCTOS: usan la misma plantilla, pero la
ficha dice "Producto propio" y nunca "Cliente". No mezclarlos con CASOS.
La estructura y el diseno de la pagina viven en build_site.py / site_shell.py.

Claves opcionales de cada entrada:
  etiqueta   nombre que va en las migas y en el <title> (por defecto, titulo).
             Sirve cuando un mismo cliente tiene dos casos.
  ficha      filas de la ficha lateral [(rotulo, valor), ...].
  boton      (texto, url) del boton de la ficha; None = sin boton.
  figuras    {indice de bloque: (src, alt, pie, ancho, alto)}: imagenes que
             van despues de ese bloque. La figura principal va tras el bloque 0.
  figura     None = todavia no hay captura: se muestra un recuadro pendiente.
  figura_plana  True = sin la barra de navegador (capturas de una app).
  testimonio (cita, firma) al final del cuerpo; con PENDIENTE mientras no llegue.
"""

PENDIENTE = '<span class="pendiente">por confirmar</span>'

# Pie comun a las pantallas del sistema de bySIMMED. Son recreaciones con
# datos inventados: nunca se publica una captura con datos reales del cliente.
EJEMPLO = 'Pantalla con datos de ejemplo.'

CASOS = [
 {
  'slug': 'bysimmed-sistema',
  'titulo': 'bySIMMED',
  'etiqueta': 'bySIMMED · Sistema de gestión',
  'sector': 'Salud',
  'tipo': 'Sistema de gestión',
  'meta_desc': 'Caso CORYN: sistema de gestión para bySIMMED que lee los correos con '
               'órdenes de compra, facturas y pagos, arma cotizaciones y sigue cada '
               'venta hasta el cobro.',
  'h1': 'Un fabricante chileno con las ventas repartidas en el correo',
  'lead': 'bySIMMED fabrica simuladores médicos y vende a centros de formación '
          'clínica en varios países. Cotizaciones, órdenes de compra, facturas y '
          'pagos llegaban por correo, y saber en qué iba cada venta era cosa de '
          'buscar en la bandeja.',
  'ficha': [('Cliente', 'bySIMMED'), ('Sector', 'Salud'),
            ('Tipo de proyecto', 'Sistema de gestión'), ('Estado', 'En uso')],
  'boton': ('¿Tu empresa trabaja así?', 'correo.html'),
  'figura': 'assets/bysimmed-bandeja.webp',
  'figura_alt': 'Inicio de administración del sistema de bySIMMED, con los correos del '
                'día ya leídos: una orden de compra, una factura, un pago y un despacho '
                'esperando confirmación',
  'figura_pie': 'El inicio de administración: lo que llegó por correo ya está leído y '
                'cada cosa espera un clic. ' + EJEMPLO,
  'ancho': 1400, 'alto': 875,
  'figuras': {
   1: ('assets/bysimmed-venta.webp',
       'Una venta en el sistema de bySIMMED, con su avance de la cotización al cobro',
       'Una venta de punta a punta: cotización, orden de compra, fabricación, despacho, '
       'factura y cobro. ' + EJEMPLO, 1400, 875),
  },
  'bloques': [
   ('El problema',
    ['<p>Todo pasaba por el correo. Ahí llegaban los pedidos de precio, las órdenes '
     'de compra de los clientes, las facturas de los proveedores, los avisos de pago '
     'y los de despacho.</p>',
     '<p>Para saber si una venta ya tenía orden de compra, si estaba facturada o si '
     'la habían pagado, había que buscar el correo y cruzarlo a mano. Una factura '
     'vencida o una cotización sin respuesta no avisaban solas: había que acordarse.</p>']),
   ('Qué construimos',
    ['<p>Un sistema de gestión hecho a la medida de cómo trabaja bySIMMED, que parte '
     'por el correo:</p>',
     '<ul>'
     '<li>Lee los correos que llegan —órdenes de compra, facturas de proveedores, '
     'pagos y despachos— y deja anotado lo que dicen. Una persona confirma con un clic.</li>'
     '<li>Cuando un cliente pide precio por correo, deja la cotización armada con el '
     'catálogo y la lista de precios, y sugiere la respuesta.</li>'
     '<li>Cada venta se sigue en una sola pantalla: cotización, orden de compra, '
     'fabricación, despacho, factura y cobro.</li>'
     '<li>Muestra lo que falta cobrar y deja escrito el correo de cobranza.</li>'
     '<li>Avisa cuando un insumo baja del mínimo y prepara el pedido de compra.</li>'
     '</ul>']),
   ('Las decisiones que importaron',
    ['<p>Nada sale sin que alguien lo mire. El sistema lee, anota y redacta; una '
     'persona revisa y aprueba. Un correo de cobro o de seguimiento sale solo '
     'únicamente si administración enciende esa regla.</p>',
     '<p>Lo que no sabe, no lo inventa. Si un correo pide un modelo que no está en el '
     'catálogo, la cotización lo dice en vez de adivinar un precio. Si una respuesta '
     'necesita un dato que el sistema no tiene, lo deja marcado para completarlo.</p>',
     '<p>El taller y la oficina miran lo mismo. Producción ve sus pedidos en un '
     'calendario y avanza cada unidad; administración ve en qué va cada venta sin '
     'tener que preguntar.</p>']),
  ],
  'testimonio': (PENDIENTE + ' Testimonio de bySIMMED sobre el sistema.',
                 PENDIENTE + ' Nombre y cargo'),
 },
 {
  'slug': 'bysimmed',
  'titulo': 'bySIMMED',
  'etiqueta': 'bySIMMED · Sitio web',
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
]


# Productos de CORYN. No son trabajos para clientes: se cuentan por lo que le
# sirve a una pyme (leer documentos con IA, cobrar en linea), no por tecnologia.
PRODUCTOS = [
 {
  'slug': 'enumera',
  'titulo': 'Enumera',
  'sector': 'Educación',
  'tipo': 'Clases en línea',
  'meta_desc': 'Enumera, producto propio de CORYN: clases de matemáticas en línea que '
               'corrigen con IA la foto del cuaderno y cobran solas, en pesos o en dólares.',
  'h1': 'Una academia en línea que corrige el cuaderno con una foto y cobra sola',
  'lead': 'Enumera es un producto propio de CORYN: clases de matemáticas para la '
          'universidad. El alumno resuelve a mano, sube la foto y recibe la corrección '
          'paso a paso. Paga en la misma página, en pesos o en dólares.',
  'ficha': [('Producto', 'Enumera'), ('Hecho por', 'CORYN, producto propio'),
            ('Qué hace', 'Clases y corrección con IA'),
            ('Cobro', 'En línea, en pesos y en dólares'), ('Estado', 'En línea')],
  'boton': ('academiaenumera.com', 'https://academiaenumera.com/'),
  'figura': 'assets/enumera-portada.webp',
  'figura_alt': 'Portada de academiaenumera.com',
  'figura_pie': 'La portada de Enumera. Captura del sitio público.',
  'ancho': 1400, 'alto': 875,
  'figuras': {
   1: ('assets/enumera-correccion.webp',
       'Corrección de un ejercicio escrito a mano: la foto del cuaderno y, al lado, '
       'qué estuvo bien, qué estuvo mal y qué faltó',
       'La corrección por foto: lee lo escrito a mano y lo revisa paso por paso. '
       'Captura del sitio público.', 1400, 875),
   2: ('assets/enumera-planes.webp',
       'Página de planes de Enumera, con precios en pesos y la opción de verlos en dólares',
       'Los planes, con el pago en la misma página, en pesos o en dólares. '
       'Captura del sitio público.', 1400, 875),
  },
  'bloques': [
   ('Qué es',
    ['<p>Enumera enseña matemáticas para las pruebas de la universidad, con clases '
     'cortas y ejercicios como los de la prueba. Funciona en el navegador del celular '
     'o del computador, sin instalar nada.</p>',
     '<p>Lo hicimos para nosotros, y está en línea: cualquiera puede entrar y '
     'probarlo.</p>']),
   ('Lee lo escrito a mano',
    ['<p>El alumno resuelve en su cuaderno, como en la prueba, y le saca una foto. '
     'La IA lee lo que escribió y le dice qué está bien, qué está mal y qué le '
     'faltó, paso por paso.</p>',
     '<p>Es el mismo tipo de lectura que usa el '
     '<a href="caso-bysimmed-sistema.html">sistema de bySIMMED</a> para sacar los '
     'datos de una orden de compra que llega en PDF.</p>']),
   ('Cobra en línea, en pesos y en dólares',
    ['<p>Los planes se pagan en la misma página. En Chile, con tarjeta en Mercado '
     'Pago; desde otro país, en dólares. El acceso queda activo apenas se paga, sin '
     'que nadie tenga que hacer nada.</p>']),
   ('Lo que le sirve a tu empresa',
    ['<p>Las dos piezas difíciles de Enumera son las mismas que pide una empresa:</p>',
     '<ul>'
     '<li><b>Leer documentos con IA.</b> Pasar una foto o un PDF a datos ordenados, '
     'sin tipearlos: una orden de compra, una factura, una guía de despacho.</li>'
     '<li><b>Cobrar en línea.</b> Planes, pago con tarjeta y acceso que se activa '
     'solo. Sirve igual para un servicio, una suscripción o una reserva.</li>'
     '<li><b>Cobrar fuera de Chile.</b> Precios en dólares para quien paga desde '
     'otro país.</li>'
     '</ul>']),
  ],
 },
 {
  'slug': 'precioradar',
  'titulo': 'PrecioRadar',
  'sector': 'Consumo',
  'tipo': 'App para Android',
  'meta_desc': 'PrecioRadar, producto propio de CORYN: app que lee boletas de '
               'supermercado con IA y compara precios entre cinco cadenas.',
  'h1': 'Una app que lee boletas de supermercado y compara precios entre cinco cadenas',
  'lead': 'PrecioRadar es un producto propio de CORYN, publicado en Google Play. '
          'Lee la foto de la boleta y compara el precio de cada producto entre cinco '
          'cadenas de supermercados.',
  'ficha': [('Producto', 'PrecioRadar'), ('Hecho por', 'CORYN, producto propio'),
            ('Qué hace', 'Lee boletas y compara precios'),
            ('Estado', 'En Google Play')],
  'boton': ('Ver en Google Play',
            'https://play.google.com/store/apps/details?id=com.precioradar'),
  'figura': 'assets/precioradar-capturas.webp',
  'figura_alt': 'Tres pantallas de PrecioRadar: escanear la boleta, el gasto del mes por '
                'supermercado y la comparación de una lista entre supermercados',
  'figura_pie': 'Escanear la boleta, ver el gasto del mes y comparar supermercados. '
                'Imágenes de la ficha en Google Play.',
  'figura_plana': True,
  'ancho': 1400, 'alto': 875,
  'bloques': [
   ('Qué hace',
    ['<p>Le sacas una foto a la boleta del supermercado y la app la lee: productos, '
     'precios y local. Con eso muestra cuánto gastas al mes, en qué, y qué precios '
     'de lo que compras subieron.</p>',
     '<p>Además compara el precio de cada producto entre cinco cadenas de '
     'supermercados, para saber dónde conviene comprar.</p>']),
   ('Lo que le sirve a tu empresa',
    ['<p>Una boleta es un documento desordenado: cada cadena la imprime distinto, '
     'con sus propias abreviaturas, y la foto casi nunca sale perfecta. Leerla bien '
     'es el mismo problema que leer una factura de proveedor o una guía de despacho.</p>',
     '<ul>'
     '<li><b>Leer documentos con IA.</b> Pasar de una foto a datos ordenados, sin '
     'tipearlos.</li>'
     '<li><b>Comparar precios de varias fuentes.</b> Lo mismo que necesita quien le '
     'compra a varios proveedores y quiere saber cuál le conviene.</li>'
     '</ul>']),
   ('Por qué lo mostramos',
    ['<p>Porque está publicado y cualquiera lo puede instalar y probar. Es la forma '
     'más directa de mostrar lo que sabemos hacer.</p>']),
  ],
 },
]
