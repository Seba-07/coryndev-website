#!/usr/bin/env python3
"""Arma las paginas del sitio (v2) desde site/*.body.html + site_shell.py.

Uso:  python3 build_site.py

Cada pagina se escribe en site/<slug>.body.html y aqui se declara su titulo,
descripcion y cierre. La cabecera, la navegacion y el pie viven una sola vez
en site_shell.py.

Los marcadores <span class="pendiente"> senalan datos que faltan por confirmar;
para encontrarlos todos:  grep -rn 'class="pendiente"' *.html
"""
import pathlib

import site_shell as S
from casos_data import CASOS

RAIZ = pathlib.Path(__file__).parent
CUERPOS = RAIZ / 'site'
SALIDA = RAIZ

# Marcadores que pueden usarse dentro de los .body.html
FICHAS = {
    '{CHECK}': S.CHECK,
    '{CHECK_G}': '<svg viewBox="0 0 24 24"><path d="M12 3.2 20 7v6c0 4.2-3.3 7-8 7.8C7.3 20 4 17.2 4 13V7z"/><path d="m9.2 12.2 2 2 3.6-4"/></svg>',
    '{CRUZ_G}': '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16.2v.01"/></svg>',
    '{CRUZ}': S.CRUZ,
    '{FLECHA}': S.FLECHA,
    '{PENDIENTE}': S.PENDIENTE,
    '{WA}': S.WA,
    '{WA_SVG}': S.WA_SVG,
    '{WA_ETIQUETA}': S.WA_ETIQUETA,
    '{WA_NUM}': S.WA_NUM,
    '{EMAIL}': S.EMAIL,
    '{BACKEND}': S.BACKEND,
}

JS_FORMULARIO = '''<script>
  (function () {
    var form = document.getElementById('contactForm');
    var aviso = document.getElementById('formAviso');
    if (!form) return;

    var mostrar = function (tipo, texto) {
      aviso.className = 'aviso ' + tipo;
      aviso.textContent = texto;
    };

    var refFirma = function () {
      var r = window.CORYN && window.CORYN.ref;
      return r ? '\\n\\n---\\nLlegó con el código de referido: ' + r : '';
    };

    form.addEventListener('submit', async function (e) {
      e.preventDefault();
      if (!form.checkValidity()) {
        mostrar('error', 'Revisa los campos obligatorios antes de enviar.');
        form.reportValidity();
        return;
      }

      var boton = form.querySelector('button[type="submit"]');
      var textoOriginal = boton.textContent;
      boton.disabled = true;
      boton.textContent = 'Enviando...';
      aviso.className = 'aviso';

      try {
        var resp = await fetch('%(backend)s', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            name: form.name.value.trim(),
            email: form.email.value.trim(),
            phone: form.phone.value.trim(),
            // El referido viaja tambien dentro del mensaje: el backend vive
            // aparte y si ignora el campo nuevo, el dato se perderia igual.
            message: form.message.value.trim() + refFirma(),
            ref: (window.CORYN && window.CORYN.ref) || ''
          })
        });
        var data = await resp.json();
        if (resp.ok && data.success) {
          form.reset();
          mostrar('ok', 'Listo, recibimos tu mensaje. Te respondemos en menos de 24 horas.');
        } else {
          throw new Error('respuesta no exitosa');
        }
      } catch (err) {
        mostrar('error',
          'No pudimos enviar el mensaje. Escríbenos por WhatsApp ' +
          'o a %(email)s y lo resolvemos por ahí.');
      } finally {
        boton.disabled = false;
        boton.textContent = textoOriginal;
      }
    });
  })();
</script>''' % {'backend': S.BACKEND, 'email': S.EMAIL}


# slug, titulo, descripcion, clave de menu, (titulo cabecera, bajada, eyebrow), cierre
PAGINAS = [
    dict(
        slug='index',
        titulo='Desarrollo de software a medida para pymes | CORYN',
        desc='Sistemas de gestión, sitios web, tiendas y apps a medida para pymes '
             'chilenas. Desde $129.000, con precio cerrado antes de empezar. '
             'Primera reunión sin costo.',
        activa='inicio',
        cabecera=None,
        preload=('assets/real-planilla.webp',),
        cierre=('Conversemos 30 minutos, sin costo.',
                'Cuéntanos tu situación y te decimos con honestidad qué se puede '
                'resolver con software, qué conviene priorizar y cuánto costaría '
                'hacerlo bien.'),
    ),
    dict(
        slug='servicios',
        titulo='Servicios: sistemas, webs, tiendas y apps a medida | CORYN',
        desc='Páginas web, sistemas de gestión, aplicaciones móviles, tiendas online '
             'e integraciones. Con el alcance, los plazos y los límites de cada uno.',
        activa='servicios',
        cabecera=('Lo que hacemos, dicho en concreto',
                  'Seis servicios, con lo que incluye cada uno, lo que no incluye y '
                  'cuánto suele demorar. Sin letra chica.',
                  'Servicios'),
        cierre=('¿Cuál de estos se parece a tu problema?',
                'Si ninguno calza del todo, escríbenos igual. La mayoría de los '
                'proyectos empieza con alguien que no sabía en qué categoría entraba.'),
    ),
    dict(
        slug='privacidad',
        titulo='Política de privacidad | CORYN',
        desc='Qué datos recoge coryndev.com, para qué los usamos y con quién se '
             'comparten. Sin cookies de publicidad ni seguimiento entre sitios.',
        activa='',
        clase_body='pg-oscura',
        cabecera=('Política de privacidad',
                  'Qué datos recoge este sitio, para qué los usamos y con quién '
                  'se comparten. En castellano, no en jerga legal.',
                  'Legal'),
        cierre=('¿Alguna duda sobre tus datos?',
                'Escríbenos y te respondemos. Puedes pedirnos qué tenemos tuyo, '
                'que lo corrijamos o que lo borremos, sin dar explicaciones.'),
    ),
    dict(
        slug='que-resolvemos',
        titulo='Qué resolvemos: seis problemas de pyme | CORYN',
        desc='Operación en planillas, no aparecer en Google, responder lo mismo por '
             'WhatsApp, agendar por teléfono. Qué le cuesta cada uno a tu negocio '
             'y qué construimos.',
        activa='problemas',
        clase_body='pg-oscura',
        cabecera=('Cuál de estas se parece a tu semana',
                  'Seis situaciones que vemos una y otra vez en pymes chilenas. '
                  'Reconocer la tuya suele ser más útil que saber qué sistema pedir.',
                  'Qué resolvemos'),
        cierre=('¿Reconociste alguna?',
                'Cuéntanos cuál y te decimos con honestidad qué se puede resolver, qué '
                'conviene priorizar y cuánto costaría hacerlo bien.'),
    ),
    dict(
        slug='proceso',
        titulo='Proceso — Cómo trabajamos, etapa por etapa | CORYN',
        desc='Las cinco etapas de un proyecto con CORYN: nos conocemos, diseñamos, '
             'construimos, probamos y te acompañamos. Qué esperar en cada una.',
        activa='proceso',
        cabecera=('Cómo trabajamos, etapa por etapa',
                  'Un proceso definido, para que en cada momento sepas qué está '
                  'pasando, qué viene después y qué se espera de ti.',
                  'Proceso'),
        cierre=('Empecemos por la etapa 1.',
                'Media hora de conversación, sin costo y sin compromiso. Al final '
                'te decimos con honestidad si podemos ayudarte.'),
    ),
    dict(
        slug='nosotros',
        clase_body='pg-oscura',
        titulo='Nosotros — Quiénes están detrás de CORYN',
        desc='Estudio chileno de desarrollo de software a medida. Hablas directamente '
             'con quien programa tu proyecto, sin intermediarios ni vendedores.',
        activa='nosotros',
        cabecera=('Hablas con quien programa',
                  'Literalmente. No es una frase de marketing: quien toma la reunión '
                  'de levantamiento es quien escribe el código y responde el soporte.',
                  'Nosotros'),
        cierre=('Conversemos 30 minutos, sin costo.',
                'Sin vendedores de por medio. La primera conversación es directamente '
                'con quien va a construir tu proyecto.'),
    ),
    dict(
        slug='404',
        titulo='Página no encontrada | CORYN',
        desc='La dirección que buscas no existe o cambió de lugar.',
        activa='',
        cabecera=('Esta página no existe',
                  'La dirección que escribiste no está o cambió de lugar. '
                  'Nada grave: desde aquí se llega a todo lo demás.',
                  'Error 404'),
        cierre=None,
    ),
    dict(
        slug='contacto',
        clase_body='pg-oscura',
        titulo='Contacto — Conversemos sobre tu proyecto | CORYN',
        desc='Escríbenos y conversemos sobre tu proyecto. Primera reunión sin costo y '
             'respuesta en menos de 24 horas hábiles. También por WhatsApp.',
        activa='',
        cabecera=('Conversemos sobre tu proyecto',
                  'La primera reunión es sin costo y sin compromiso. Cuéntanos qué '
                  'te está complicando y te decimos con honestidad qué se puede hacer.',
                  'Contacto'),
        cierre=('¿Prefieres escribir por WhatsApp?',
                'Es la vía más rápida y respondemos el mismo día. Si es fuera de '
                'horario, deja el mensaje igual y lo vemos a primera hora.'),
        js_extra=JS_FORMULARIO,
    ),
]


# ---------- datos estructurados por pagina ----------

def migas_ld(camino):
    """BreadcrumbList a partir de la ruta visible.

    camino: [(nombre, href|None), ...] en el mismo orden que las migas que ve
    el visitante. Google exige que coincidan; por eso se arman del mismo dato.
    """
    return {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': i, 'name': nom,
             **({'item': f'https://coryndev.com/{href}'} if href else {})}
            for i, (nom, href) in enumerate(camino, 1)
        ],
    }


def faq_ld(cuerpo):
    """FAQPage leida del propio HTML.

    Se extrae de los <details> ya publicados en vez de escribirla aparte: si
    manana cambia una respuesta en la pagina, el dato estructurado cambia con
    ella y no quedan las dos versiones peleando.
    """
    import re, html as _html
    pares = re.findall(
        r'<details[^>]*>\s*<summary[^>]*>(.*?)</summary>(.*?)</details>',
        cuerpo, re.S)
    def limpio(x):
        x = re.sub(r'<[^>]+>', ' ', x)
        return _html.unescape(re.sub(r'\s+', ' ', x)).strip()
    if not pares:
        return None
    return {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        'mainEntity': [
            {'@type': 'Question', 'name': limpio(q),
             'acceptedAnswer': {'@type': 'Answer', 'text': limpio(r)}}
            for q, r in pares
        ],
    }


# Solo lleva precio el servicio que lo publica en la pagina. Declarar en los
# datos estructurados un precio que el visitante no ve es justamente lo que
# Google sanciona, y ademas seria mentir.
SERVICIOS_LD = [
    ('Sistemas de gestión (ERP / CRM)',
     'Inventario, ventas, clientes y cobros en un solo lugar. Se puede partir '
     'por un módulo y crecer desde ahí.', 129000),
    ('Páginas web',
     'Sitios para que te encuentren en Google y sepan a qué te dedicas.', 69000),
    ('Aplicaciones móviles',
     'Apps para iOS y Android, o instalables desde el navegador.', None),
    ('Tiendas online',
     'Catálogo, carro y pago en línea, con el stock siempre al día.', None),
    ('Integraciones y automatizaciones',
     'Conectar sistemas que hoy no se hablan y dejar de copiar datos a mano.', None),
    ('Acompañamiento mensual',
     'Mantención, respaldos, monitoreo y mejoras pequeñas cada mes.', None),
]


def servicios_ld():
    def oferta(nombre, desc, desde):
        s = {
            '@type': 'Service',
            'name': nombre,
            'description': desc,
            'serviceType': nombre,
            'provider': {'@id': 'https://coryndev.com/#coryn'},
            'areaServed': {'@type': 'Country', 'name': 'Chile'},
        }
        if desde:
            s['offers'] = {
                '@type': 'Offer',
                'priceCurrency': 'CLP',
                'priceSpecification': {
                    '@type': 'PriceSpecification',
                    'minPrice': desde,
                    'priceCurrency': 'CLP',
                    'valueAddedTaxIncluded': False,
                },
                'availability': 'https://schema.org/InStock',
                'url': 'https://coryndev.com/servicios.html',
            }
        return s
    return {
        '@context': 'https://schema.org',
        '@type': 'ItemList',
        'name': 'Servicios de CORYN',
        'itemListElement': [
            {'@type': 'ListItem', 'position': i, 'item': oferta(*s)}
            for i, s in enumerate(SERVICIOS_LD, 1)
        ],
    }


def caso_ld(c):
    return {
        '@context': 'https://schema.org',
        '@type': 'CreativeWork',
        'name': f"{c['titulo']} — caso de proyecto",
        'headline': c['h1'],
        'description': c['meta_desc'],
        'url': f"https://coryndev.com/caso-{c['slug']}.html",
        'image': f"https://coryndev.com/{c['figura']}",
        'inLanguage': 'es-CL',
        'creator': {'@id': 'https://coryndev.com/#coryn'},
        'about': {'@type': 'Thing', 'name': c['sector']},
        'genre': c['tipo'],
    }


def aplicar_fichas(txt):
    for k, v in FICHAS.items():
        txt = txt.replace(k, v)
    return txt


# ---------- paginas normales ----------

def construir_paginas():
    for p in PAGINAS:
        cuerpo = aplicar_fichas((CUERPOS / f"{p['slug'].replace('index', 'inicio')}.body.html").read_text())
        partes = []
        if p['cabecera']:
            t, b, e = p['cabecera']
            partes.append(S.cabecera(t, b, e))
        partes.append(cuerpo)
        if p['cierre']:
            partes.append(S._cierre(*p['cierre'],
                                    clase_cierre=' claro' if p['slug'] == 'index' else ''))
        ld = []
        if p['slug'] not in ('index', '404'):
            ld.append(migas_ld([('Inicio', 'index.html'),
                                (p['cabecera'][2] or p['titulo'], None)]))
        if p['slug'] == 'contacto':
            faq = faq_ld(cuerpo)
            if faq:
                ld.append(faq)
        if p['slug'] == 'servicios':
            ld.append(servicios_ld())

        html = S.render(
            titulo=p['titulo'], descripcion=p['desc'], cuerpo='\n\n'.join(partes),
            activa=p['activa'], js_extra=p.get('js_extra', ''),
            nav_solida=False,
            canonico='' if p['slug'] == 'index' else f"{p['slug']}.html",
            clase_body=p.get('clase_body', ''),
            ld_extra=ld,
            preload=p.get('preload', ()),
        )
        if p['slug'] == '404':
            # que los buscadores no la guarden como si fuera contenido
            html = html.replace('<meta name="description"',
                                '<meta name="robots" content="noindex">\n<meta name="description"')
        destino = SALIDA / f"{p['slug']}.html"
        destino.write_text(html)
        yield destino


# ---------- paginas de caso ----------

def ficha_caso(c):
    filas = [('Cliente', c['titulo']),
             ('Sector', c['sector']),
             ('Tipo de proyecto', c['tipo']),
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


def cuerpo_caso(c):
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


def construir_casos():
    for c in CASOS:
        camino = [('Inicio', 'index.html'), ('Proyectos', 'nosotros.html#recorrido'),
                  (c['titulo'], None)]
        cabecera = S.cabecera(
            c['h1'], c['lead'], f"{c['sector']} &middot; {c['tipo']}", migas=camino)
        cuerpo = f'''<section>
  <div class="wrap caso-grid">
    <article class="caso-body">
{cuerpo_caso(c)}
    </article>
{ficha_caso(c)}
  </div>
</section>'''
        cierre = S._cierre(
            'Conversemos 30 minutos, sin costo.',
            'Cuéntanos tu situación y te decimos con honestidad qué se puede resolver '
            'con software, qué conviene priorizar y cuánto costaría hacerlo bien.',
            boton_extra='<a class="btn btn-ghost" href="nosotros.html#recorrido">Ver otros proyectos</a>')
        html = S.render(
            titulo=f"{c['titulo']} — Caso de proyecto | CORYN",
            descripcion=c['meta_desc'],
            cuerpo='\n\n'.join([cabecera, cuerpo, cierre]),
            activa='', og_img=c['figura'], og_tipo='article',
            canonico=f"caso-{c['slug']}.html",
            ld_extra=[migas_ld(camino), caso_ld(c)],
            preload=(c['figura'],))
        destino = SALIDA / f"caso-{c['slug']}.html"
        destino.write_text(html)
        yield destino


def _ultimo_cambio(*fuentes):
    """Fecha del ultimo commit que toco el contenido de la pagina.

    Se mira la fuente, no el HTML generado: el HTML se reescribe entero en
    cada build y un <lastmod> que cambia sin que cambie el contenido es ruido
    que los buscadores terminan ignorando.
    """
    import subprocess, datetime
    fechas = []
    for f in fuentes:
        ruta = RAIZ / f
        if not ruta.exists():
            continue
        try:
            r = subprocess.run(['git', 'log', '-1', '--format=%cs', '--', str(f)],
                               cwd=RAIZ, capture_output=True, text=True, timeout=10)
            if r.returncode == 0 and r.stdout.strip():
                fechas.append(r.stdout.strip())
                continue
        except Exception:
            pass
        fechas.append(datetime.date.fromtimestamp(ruta.stat().st_mtime).isoformat())
    return max(fechas) if fechas else None


def construir_sitemap():
    """Un <url> por pagina publica. La 404 queda fuera: existe para
    responder, no para aparecer en buscadores."""
    urls = [('https://coryndev.com/', _ultimo_cambio('site/inicio.body.html'))]
    urls += [(f"https://coryndev.com/{p['slug']}.html",
              _ultimo_cambio(f"site/{p['slug']}.body.html"))
             for p in PAGINAS if p['slug'] not in ('index', '404')]
    urls += [(f"https://coryndev.com/caso-{c['slug']}.html",
              _ultimo_cambio('casos_data.py')) for c in CASOS]
    cuerpo = '\n'.join(
        f'  <url><loc>{u}</loc>' + (f'<lastmod>{d}</lastmod>' if d else '') + '</url>'
        for u, d in urls)
    destino = SALIDA / 'sitemap.xml'
    destino.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f'{cuerpo}\n</urlset>\n')
    # Sin Disallow a proposito. Las paginas que no queremos en el indice
    # (legales de apps, 404, redirecciones) llevan <meta robots="noindex">, y
    # para obedecerlo el buscador necesita poder entrar a leerlo. Bloquearlas
    # aqui ademas dejaria fuera al robot y la URL podria indexarse igual.
    (SALIDA / 'robots.txt').write_text(
        'User-agent: *\n'
        'Allow: /\n\n'
        'Sitemap: https://coryndev.com/sitemap.xml\n')
    return destino, len(urls)


if __name__ == '__main__':
    total = 0
    for destino in list(construir_paginas()) + list(construir_casos()):
        n = destino.stat().st_size
        total += n
        print(f'  {destino.name:26s} {n // 1024:>3} KB')
    print(f'  {"":26s} {total // 1024:>3} KB en total')

    _, n = construir_sitemap()
    print(f'  sitemap.xml con {n} URLs + robots.txt')

    pendientes = sum(p.read_text().count('class="pendiente"')
                     for p in SALIDA.glob('*.html'))
    if pendientes:
        print(f'\n  {pendientes} dato(s) por confirmar. Para ubicarlos:')
        print("    grep -rn 'class=\"pendiente\"' *.html")
