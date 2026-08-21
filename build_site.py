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
    '{CRUZ}': S.CRUZ,
    '{FLECHA}': S.FLECHA,
    '{PENDIENTE}': S.PENDIENTE,
    '{WA}': S.WA,
    '{WA_SVG}': S.WA_SVG,
    '{TELEFONO}': S.TELEFONO,
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
            message: form.message.value.trim()
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
          'No pudimos enviar el mensaje. Escríbenos por WhatsApp al %(tel)s ' +
          'o a %(email)s y lo resolvemos por ahí.');
      } finally {
        boton.disabled = false;
        boton.textContent = textoOriginal;
      }
    });
  })();
</script>''' % {'backend': S.BACKEND, 'tel': S.TELEFONO, 'email': S.EMAIL}


# slug, titulo, descripcion, clave de menu, (titulo cabecera, bajada, eyebrow), cierre
PAGINAS = [
    dict(
        slug='index',
        titulo='CORYN — Software a medida para empresas en Chile',
        desc='Desarrollamos sistemas de gestión, aplicaciones móviles y sitios web a '
             'medida. Experiencia en salud, aviación, inmobiliario y retail. '
             'Primera reunión sin costo.',
        activa='inicio',
        cabecera=None,
        cierre=('Conversemos 30 minutos, sin costo.',
                'Cuéntanos tu situación y te decimos con honestidad qué se puede '
                'resolver con software, qué conviene priorizar y cuánto costaría '
                'hacerlo bien.'),
    ),
    dict(
        slug='servicios',
        titulo='Servicios — Qué desarrollamos y qué no | CORYN',
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
        slug='proceso',
        titulo='Proceso — Cómo trabajamos, etapa por etapa | CORYN',
        desc='Las cinco etapas de un proyecto con CORYN: qué hacemos nosotros y qué '
             'necesitamos de ti en cada una.',
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
        slug='productos',
        titulo='PrecioRadar — Nuestro producto propio | CORYN',
        desc='PrecioRadar es la aplicación móvil que desarrollamos como producto '
             'propio: lectura automática de boletas y comparación de precios.',
        activa='productos',
        cabecera=('No solo desarrollamos para otros',
                  'PrecioRadar es producto nuestro. Lo llevamos de la idea a las '
                  'tiendas de aplicaciones, y todo lo que aprendimos ahí lo usamos '
                  'en los proyectos de clientes.',
                  'Producto propio'),
        cierre=('¿Tienes una idea de producto?',
                'Convertir una idea en un producto publicado es un camino que ya '
                'recorrimos completo. Conversemos sobre el tuyo.'),
    ),
    dict(
        slug='nosotros',
        titulo='Nosotros — Quiénes están detrás de CORYN',
        desc='Somos un estudio pequeño de desarrollo de software en Chile. Hablas '
             'directamente con quien programa tu proyecto.',
        activa='nosotros',
        cabecera=('Hablas con quien programa',
                  'Somos un equipo chico y no pretendemos parecer más grandes. Esa '
                  'es justamente la razón por la que nuestros clientes se quedan.',
                  'Nosotros'),
        cierre=('Conversemos 30 minutos, sin costo.',
                'Sin vendedores de por medio. La primera conversación es con quien '
                'va a trabajar en tu proyecto.'),
    ),
    dict(
        slug='contacto',
        titulo='Contacto — Conversemos sobre tu proyecto | CORYN',
        desc='Escríbenos y conversemos sobre tu proyecto. Primera reunión sin costo, '
             'respuesta en menos de 24 horas.',
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
            partes.append(S._cierre(*p['cierre']))
        html = S.render(
            titulo=p['titulo'], descripcion=p['desc'], cuerpo='\n\n'.join(partes),
            activa=p['activa'], js_extra=p.get('js_extra', ''),
            nav_solida=False,
        )
        destino = SALIDA / f"{p['slug']}.html"
        destino.write_text(html)
        yield destino


# ---------- paginas de caso ----------

def ficha_caso(c):
    filas = [('Cliente', 'Producto propio de CORYN' if c['slug'] == 'precioradar' else c['titulo']),
             ('Sector', c['sector']),
             ('Tipo de proyecto', c['tipo']),
             ('Año', S.PENDIENTE),
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
        cabecera = S.cabecera(
            c['h1'], c['lead'], f"{c['sector']} &middot; {c['tipo']}",
            migas=[('Inicio', 'index.html'), ('Casos', 'index.html#casos'),
                   (c['titulo'], None)])
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
            boton_extra='<a class="btn btn-ghost" href="index.html#casos">Ver otros casos</a>')
        html = S.render(
            titulo=f"{c['titulo']} — Caso de proyecto | CORYN",
            descripcion=c['meta_desc'],
            cuerpo='\n\n'.join([cabecera, cuerpo, cierre]),
            activa='casos', og_img=c['figura'], og_tipo='article')
        destino = SALIDA / f"caso-{c['slug']}.html"
        destino.write_text(html)
        yield destino


if __name__ == '__main__':
    total = 0
    for destino in list(construir_paginas()) + list(construir_casos()):
        n = destino.stat().st_size
        total += n
        print(f'  {destino.name:26s} {n // 1024:>3} KB')
    print(f'  {"":26s} {total // 1024:>3} KB en total')

    pendientes = sum(p.read_text().count('class="pendiente"')
                     for p in SALIDA.glob('*.html'))
    if pendientes:
        print(f'\n  {pendientes} dato(s) por confirmar. Para ubicarlos:')
        print("    grep -rn 'class=\"pendiente\"' *.html")
