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
from urllib.parse import quote

import site_shell as S
from casos_data import CASOS, PRODUCTOS

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
    '{CITA_IVONNE}': S.CITA_IVONNE,
    '{FIRMA_IVONNE}': S.FIRMA_IVONNE,
    '{WA}': S.WA,
    '{WA_SVG}': S.WA_SVG,
    '{WA_ETIQUETA}': S.WA_ETIQUETA,
    '{WA_NUM}': S.WA_NUM,
    '{EMAIL}': S.EMAIL,
    '{BACKEND}': S.BACKEND,
    # El de correo.html dice de que pagina viene, para saber que el mensaje
    # llego por ese enlace y no por el sitio.
    '{WA_CORREO}': f'https://wa.me/{S.WA_NUM}?text=' + quote(
        'Hola CORYN, vi la página sobre el correo. En mi empresa las cotizaciones '
        'y órdenes de compra llegan por correo. ¿Podemos conversarlo?', safe=''),
    # El de mercado-publico.html pide la demo con una orden de la empresa; el
    # codigo ?ref= del mensaje se agrega al final y dice quien es.
    '{WA_MP}': f'https://wa.me/{S.WA_NUM}?text=' + quote(
        'Hola CORYN, quiero ver una de mis órdenes de compra de Mercado Público '
        'anotada en el sistema.', safe=''),
}

# mercado-publico.html. Cuatro piezas, todas con salida digna si algo falla:
# la cuenta de horas, la pantalla que cambia de estado al recorrer la vida de
# una orden, el boton fijo del celular y la demostracion de la portada (esta
# ultima solo con GSAP y si la persona no pidio menos movimiento).
JS_MP = '''<script>
document.addEventListener('DOMContentLoaded', function () {
  var d = document, raiz = d.documentElement;
  var quieto = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- cuanto tiempo devuelve ---------- */
  (function () {
    var chips = [].slice.call(d.querySelectorAll('.lp-chips button'));
    if (!chips.length) return;
    var num = d.getElementById('horas-n'), frase = d.getElementById('horas-frase'),
        dias = d.getElementById('horas-dias'), wa = d.getElementById('horas-wa');
    var bloques = [], mostrado = { v: +num.textContent };
    for (var i = 0; i < 7; i++) { var b = d.createElement('i'); dias.appendChild(b); bloques.push(b); }
    function pinta (ordenes, animar) {
      var horas = Math.round(ordenes * 10 / 60), jornadas = horas / 8;
      bloques.forEach(function (b, i) {
        b.style.setProperty('--lleno', Math.max(0, Math.min(1, jornadas - i)).toFixed(2));
      });
      var enteros = Math.floor(jornadas), resto = jornadas - enteros;
      frase.textContent = jornadas < 1
        ? 'Son pocas horas, pero cada orden olvidada es un despacho atrasado o un cobro que se pasa.'
        : (resto >= 0.2 ? 'Más de ' : 'Unos ') + enteros + (enteros === 1 ? ' día' : ' días') +
          ' de trabajo que nadie tendría que pasar copiando órdenes.';
      if (animar && window.gsap && !quieto) {
        window.gsap.to(mostrado, { v: horas, duration: 0.6, ease: 'power2.out', overwrite: true,
          onUpdate: function () { num.textContent = Math.round(mostrado.v); } });
      } else { mostrado.v = horas; num.textContent = horas; }
      // El mensaje de WhatsApp lleva el numero elegido. El codigo ?ref= se agrega
      // al hacer clic (sitio.js), asi que aqui el enlace se rearma limpio.
      if (wa) wa.href = wa.href.split('?')[0] + '?text=' + encodeURIComponent(
        'Hola CORYN, me llegan unas ' + ordenes + ' órdenes de compra de Mercado Público al mes. ' +
        'Quiero ver una de mis órdenes anotada en el sistema.');
    }
    function elige (b, animar) {
      chips.forEach(function (x) {
        x.setAttribute('aria-checked', x === b ? 'true' : 'false');
        x.tabIndex = x === b ? 0 : -1;
      });
      pinta(+b.getAttribute('data-n'), animar);
      if (animar && window.CORYN && window.CORYN.marca) window.CORYN.marca('calculadora', { ordenes: +b.getAttribute('data-n') });
    }
    chips.forEach(function (b, i) {
      b.addEventListener('click', function () { elige(b, true); });
      b.addEventListener('keydown', function (e) {
        var k = e.key, j = (k === 'ArrowRight' || k === 'ArrowDown') ? i + 1
                         : (k === 'ArrowLeft' || k === 'ArrowUp') ? i - 1 : -1;
        if (j < 0 || j >= chips.length) return;
        e.preventDefault(); chips[j].focus(); elige(chips[j], true);
      });
    });
    elige(chips.filter(function (b) { return b.getAttribute('aria-checked') === 'true'; })[0] || chips[0], false);
  })();

  /* ---------- la vida de una orden ---------- */
  (function () {
    var orden = d.querySelector('.lp-orden'), fija = d.querySelector('.lp-fija'),
        pasos = [].slice.call(d.querySelectorAll('.lp-paso'));
    if (!orden || !fija || !pasos.length) return;
    raiz.classList.add('js-vida');
    var pendiente = false, actual = 0;
    function mide () {
      pendiente = false;
      var alto = window.innerHeight;
      // En el celular la pantalla queda fija arriba: el paso activo es el que se
      // lee en el espacio que queda debajo de ella.
      var foco = window.innerWidth < 900 ? (Math.min(fija.getBoundingClientRect().bottom, alto) + alto) / 2 : alto / 2;
      var mejor = 0, dist = Infinity;
      pasos.forEach(function (p, i) {
        var r = p.getBoundingClientRect(), x = Math.abs((r.top + r.bottom) / 2 - foco);
        if (x < dist) { dist = x; mejor = i; }
      });
      if (mejor + 1 === actual) return;
      actual = mejor + 1;
      orden.setAttribute('data-paso', actual);
      pasos.forEach(function (p, i) { p.classList.toggle('activo', i === mejor); });
    }
    function pide () { if (!pendiente) { pendiente = true; requestAnimationFrame(mide); } }
    window.addEventListener('scroll', pide, { passive: true });
    window.addEventListener('resize', pide);
    mide();
  })();

  /* ---------- el boton que acompana en el celular ----------
     Se retira donde ya hay un boton a la vista (la cuenta, la oferta) y mientras
     se lee la secuencia de la orden, que necesita el alto completo. */
  (function () {
    var barra = d.querySelector('.lp-barra');
    if (!barra || !('IntersectionObserver' in window)) return;
    var motivos = {};
    function pone () {
      var fuera = false;
      for (var k in motivos) if (motivos[k]) fuera = true;
      barra.classList.toggle('fuera', fuera);
    }
    function mira (clave, sel, opciones, hastaElFinal) {
      var el = d.querySelector(sel);
      if (!el) return;
      new IntersectionObserver(function (es) {
        var e = es[0];
        motivos[clave] = e.isIntersecting || (hastaElFinal && e.boundingClientRect.top < 0);
        pone();
      }, opciones || {}).observe(el);
    }
    mira('oferta', '.lp-oferta', { rootMargin: '0px 0px -25% 0px' }, true);
    mira('cuenta', '#horas-wa');
    mira('vida', '.lp-vida-grid', { rootMargin: '-45% 0px -45% 0px' });
  })();

  /* ---------- la portada: la orden entra sola ----------
     Llega el aviso de una orden, el sistema lo lee (resaltado azul), los datos
     viajan a la hoja y la fila queda anotada. Tres ordenes y se repite; se
     detiene fuera de pantalla. Sin esto, la hoja se ve completa. */
  (function () {
    var demo = d.querySelector('.lp-demo');
    if (!demo) return;
    if (quieto || !window.gsap || !window.ScrollTrigger || !raiz.classList.contains('mov')) { demo.classList.add('quieta'); return; }
    try {
    var gsap = window.gsap, ST = window.ScrollTrigger;
    var aviso = demo.querySelector('.lp-aviso'), barra = aviso.querySelector('.lectura'),
        filas = [].slice.call(demo.querySelectorAll('.lp-fila')),
        cuenta = demo.querySelector('.lp-cuenta'), sello = demo.querySelector('.lp-sello'),
        nuevas = demo.querySelector('.lp-nuevas'), campo = {};
    function anota (n) {
      cuenta.textContent = base + n;
      if (nuevas) nuevas.textContent = n === 0 ? 'Sin órdenes nuevas todavía' : n === 1 ? '1 orden nueva hoy' : n + ' órdenes nuevas hoy';
    }
    ['oc', 'org', 'total', 'prod'].forEach(function (k) { campo[k] = aviso.querySelector('[data-campo="' + k + '"]'); });
    var base = parseInt(cuenta.textContent, 10) - filas.length;
    var viajes = [0, 1, 2].map(function () {
      var s = d.createElement('span');
      s.className = 'viaje'; s.setAttribute('aria-hidden', 'true');
      demo.appendChild(s);
      return s;
    });

    function carga (i) {
      ['oc', 'org', 'total', 'prod'].forEach(function (k) { campo[k].textContent = filas[i].getAttribute('data-' + k); });
      aviso.classList.remove('leido');
    }
    function reinicia () {
      filas.forEach(function (f) {
        f.classList.remove('llena', 'recien');
        [].forEach.call(f.cells, function (c) { c.classList.remove('puesto'); });
      });
      anota(0);
      gsap.set(sello, { opacity: 0 });
    }
    function vuela (i, k, n) {
      var destino = filas[i].querySelector('[data-celda="' + k + '"]');
      if (!destino || !destino.offsetParent) return;   // columna oculta en el celular
      var v = viajes[n], r0 = demo.getBoundingClientRect(),
          a = campo[k].getBoundingClientRect(), b = destino.getBoundingClientRect();
      v.textContent = campo[k].textContent;
      var hasta = k === 'total' ? b.right - r0.left - v.offsetWidth - 8 : b.left - r0.left + 4;
      gsap.timeline()
        .fromTo(v, { x: a.left - r0.left, y: a.top - r0.top - 3, opacity: 0, scale: 0.9 },
                   { opacity: 1, scale: 1, duration: 0.16, ease: 'power2.out' })
        .to(v, { x: hasta, y: b.top - r0.top + 3, duration: 0.62, ease: 'power3.inOut' })
        .call(function () { destino.classList.add('puesto'); })
        .to(v, { opacity: 0, duration: 0.18 });
    }

    var paso = 3.1, tl = gsap.timeline({ repeat: -1, paused: true });
    tl.call(reinicia, null, 0);
    filas.forEach(function (f, i) {
      var t = 0.25 + i * paso;
      tl.call(carga, [i], t)
        .fromTo(aviso, { x: 0, y: -30, rotation: -5, opacity: 0 },
                       { x: 0, y: 0, rotation: -1.4, opacity: 1, duration: 0.7, ease: 'expo.out' }, t + 0.02)
        .fromTo(barra, { scaleX: 0, opacity: 1 }, { scaleX: 1, duration: 0.55, ease: 'power2.inOut' }, t + 0.7)
        .call(function () { aviso.classList.add('leido'); }, null, t + 1.25)
        .to(barra, { opacity: 0, duration: 0.25 }, t + 1.27)
        .call(vuela, [i, 'org', 0], t + 1.35)
        .call(vuela, [i, 'oc', 1], t + 1.5)
        .call(vuela, [i, 'total', 2], t + 1.65)
        .call(function () {
          [].forEach.call(f.cells, function (c) { c.classList.add('puesto'); });
          f.classList.add('llena', 'recien');
          anota(i + 1);
          gsap.fromTo(cuenta.parentNode, { scale: 1.18 }, { scale: 1, duration: 0.45, ease: 'expo.out' });
          setTimeout(function () { f.classList.remove('recien'); }, 900);
        }, null, t + 2.5);
      // El ultimo aviso se queda a la vista, ya leido, hasta que el ciclo vuelve a empezar.
      if (i < filas.length - 1) tl.to(aviso, { x: -26, opacity: 0, duration: 0.3, ease: 'power2.in' }, t + 2.7);
    });
    var fin = 0.25 + filas.length * paso;
    tl.fromTo(sello, { opacity: 0, scale: 1.5, rotation: -6 },
                     { opacity: 1, scale: 1, rotation: -6, duration: 0.28, ease: 'power3.in' }, fin)
      .to(aviso, { x: -26, opacity: 0, duration: 0.3, ease: 'power2.in' }, fin + 2.9)
      .to(sello, { opacity: 0, duration: 0.3 }, fin + 2.9);

    demo.classList.add('viva');
    reinicia();
    ST.create({
      trigger: demo, start: 'top bottom', end: 'bottom top',
      onToggle: function (s) { if (s.isActive && !d.hidden) tl.play(); else tl.pause(); }
    });
    d.addEventListener('visibilitychange', function () {
      if (d.hidden) tl.pause(); else if (ST.isInViewport(demo)) tl.play();
    });
    } catch (err) { demo.classList.remove('viva'); demo.classList.add('quieta'); }
  })();
});
</script>'''

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


# Cada pagina: titulo y descripcion para buscadores, la clave del menu, su
# cabecera (titulo, bajada, nombre para las migas y, si tiene, su grafico) y
# su cierre. El cierre es el mismo en todo el sitio; cierre=False lo quita y un
# dict cambia sus textos.
PAGINAS = [
    dict(
        slug='index',
        titulo='Desarrollo de software a medida para pymes | CORYN',
        desc='Sistemas de gestión, sitios web, tiendas y apps a medida para pymes '
             'chilenas. Desde $149.000, con precio cerrado antes de empezar. '
             'Primera reunión sin costo.',
        activa='inicio',
        cabecera=None,
    ),
    dict(
        slug='precios',
        titulo='Precios de software a medida en Chile, publicados | CORYN',
        desc='Cuánto cuesta un sistema de gestión, un sitio web, una tienda online o '
             'una app con CORYN: puesta en marcha desde $149.000 y acompañamiento '
             'desde 0,5 UF al mes. Precio cerrado antes de empezar.',
        activa='precios',
        cabecera=dict(titulo='Los precios, publicados.',
                      bajada='Casi nadie en el rubro los muestra. Acá están: lo que cuesta '
                             'partir, lo que cuesta cada mes y qué incluye.',
                      nombre='Precios'),
    ),
    dict(
        slug='servicios',
        titulo='Servicios: sistemas, webs, tiendas y apps a medida | CORYN',
        desc='Páginas web, sistemas de gestión, aplicaciones móviles, tiendas online '
             'e integraciones. Con el alcance, los plazos y los límites de cada uno.',
        activa='servicios',
        cabecera=dict(titulo='Lo que hacemos, dicho en concreto.',
                      bajada='Seis servicios, con lo que incluye cada uno, lo que no '
                             'incluye y cuánto suele demorar.',
                      nombre='Servicios'),
    ),
    dict(
        slug='privacidad',
        titulo='Política de privacidad | CORYN',
        desc='Qué datos recoge coryndev.com, para qué los usamos y con quién se '
             'comparten. Sin cookies de publicidad ni seguimiento entre sitios.',
        activa='',
        cabecera=dict(titulo='Política de privacidad.',
                      bajada='Qué datos recoge este sitio, para qué los usamos y con quién '
                             'se comparten. En castellano, no en jerga legal.',
                      nombre='Legal'),
        cierre=dict(titulo='¿Alguna duda sobre tus datos?',
                    texto='Escríbenos y te respondemos. Puedes pedirnos qué tenemos tuyo, '
                          'que lo corrijamos o que lo borremos, sin dar explicaciones.',
                    secundario=f'<a class="enlace enlace-claro" href="mailto:{S.EMAIL}">{S.EMAIL}</a>'),
    ),
    dict(
        slug='que-resolvemos',
        titulo='Qué resolvemos: seis problemas de pyme | CORYN',
        desc='Operación en planillas, no aparecer en Google, responder lo mismo por '
             'WhatsApp, agendar por teléfono. Qué le cuesta cada uno a tu negocio '
             'y qué construimos.',
        activa='problemas',
        cabecera=dict(titulo='¿Cuál de estas se parece a tu semana?',
                      bajada='Seis situaciones que vemos una y otra vez en pymes chilenas. '
                             'Reconocer la tuya sirve más que saber qué sistema pedir.',
                      nombre='Qué resolvemos'),
    ),
    dict(
        slug='proceso',
        titulo='Proceso — Cómo trabajamos, etapa por etapa | CORYN',
        desc='Las cinco etapas de un proyecto con CORYN: nos conocemos, diseñamos, '
             'construimos, probamos y te acompañamos. Qué esperar en cada una.',
        activa='proceso',
        cabecera=dict(titulo='Cómo trabajamos, etapa por etapa.',
                      bajada='Cinco etapas. Las dos primeras son sin costo y sirven para '
                             'decidir si vale la pena seguir.',
                      nombre='Proceso'),
    ),
    dict(
        slug='nosotros',
        titulo='Nosotros — Quiénes están detrás de CORYN',
        desc='Estudio chileno de desarrollo de software a medida. Hablas directamente '
             'con quien programa tu proyecto, sin intermediarios ni vendedores.',
        activa='nosotros',
        cabecera=dict(titulo='Hablas con quien programa.',
                      bajada='Quien toma la primera reunión es quien escribe el código y '
                             'responde cuando algo falla. Sin ejecutivos de cuenta de por medio.',
                      nombre='Nosotros',
                      visual=S.video('vid-programando', '1/1')),
    ),
    dict(
        slug='404',
        titulo='Página no encontrada | CORYN',
        desc='La dirección que buscas no existe o cambió de lugar.',
        activa='',
        cabecera=dict(titulo='Esta página no existe.',
                      bajada='La dirección que escribiste no está o cambió de lugar. Desde '
                             'aquí se llega a todo lo demás.',
                      nombre='Error 404'),
        cierre=False,
    ),
    dict(
        slug='contacto',
        titulo='Contacto — Conversemos sobre tu proyecto | CORYN',
        desc='Escríbenos y conversemos sobre tu proyecto. Primera reunión sin costo y '
             'respuesta en menos de 24 horas hábiles. También por WhatsApp.',
        activa='',
        cabecera=dict(titulo='Conversemos sobre tu proyecto.',
                      bajada='Cuéntanos qué te está complicando. No necesitas tener '
                             'claro qué sistema quieres.',
                      nombre='Contacto'),
        cierre=False,
        js_extra=JS_FORMULARIO,
    ),
    dict(
        # Pagina para enlazar en mensajes uno a uno. Fuera del menu y con un
        # solo boton: cabecera solo con la marca y sin el cierre de siempre.
        slug='correo',
        titulo='Si todo te llega por correo: un sistema que lo anota solo | CORYN',
        desc='Cotizaciones, órdenes de compra y facturas que llegan por correo y se '
             'copian a mano. Lo que hicimos para bySIMMED, desde $390.000 y 1 UF al mes.',
        activa='',
        landing=True,
        og_img='assets/og-correo.jpg',
        cabecera=dict(titulo='Todo te llega por correo, y todo se copia a mano.',
                      bajada='Cotizaciones, órdenes de compra, facturas, avisos de pago. Si '
                             'hoy alguien los pasa uno por uno a una planilla, mira cómo lo '
                             'resolvimos en una empresa como la tuya.',
                      nombre='Para empresas que trabajan por correo',
                      acciones='<a class="enlace" href="#precio">Ver cuánto cuesta {FLECHA}</a>'),
        cierre=False,
    ),
    dict(
        # La pagina de venta para proveedores del Estado: la enlazan los mensajes.
        # Fuera del menu, con su propia portada (la demostracion viva), un pie
        # minimo y un solo pedido: ver una de tus ordenes.
        slug='mercado-publico',
        titulo='Órdenes de compra de Mercado Público, anotadas solas | CORYN',
        desc='Para proveedores del Estado: un sistema con IA que lee las órdenes de '
             'compra de Mercado Público y avisa qué falta despachar, facturar y cobrar. '
             'Tú solo revisas y apruebas. Lo que hicimos para bySIMMED.',
        activa='',
        landing=True,
        pie_minimo=True,
        og_img='assets/og-mercado-publico.jpg',
        cabecera=None,
        nombre='Para proveedores del Estado',
        cierre=False,
        js_extra=JS_MP,
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
     'por un módulo y crecer desde ahí.', 390000),
    ('Páginas web',
     'Sitios para que te encuentren en Google y sepan a qué te dedicas.', 149000),
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


def caso_ld(c, propio=False):
    pre = 'producto' if propio else 'caso'
    d = {
        '@context': 'https://schema.org',
        '@type': 'CreativeWork',
        'name': f"{c.get('etiqueta', c['titulo'])} — "
                + ('producto propio de CORYN' if propio else 'caso de proyecto'),
        'headline': c['h1'],
        'description': c['meta_desc'],
        'url': f"https://coryndev.com/{pre}-{c['slug']}.html",
        'inLanguage': 'es-CL',
        'creator': {'@id': 'https://coryndev.com/#coryn'},
        'about': {'@type': 'Thing', 'name': c['sector']},
        'genre': c['tipo'],
    }
    if c.get('figura'):
        d['image'] = f"https://coryndev.com/{c['figura']}"
    return d


def _tipos():
    """Los tipos de proyecto con su precio de partida, leidos del arreglo TIPOS
    del estimador: los montos viven en un solo lugar."""
    import re
    fuente = (CUERPOS / '_estimador.html').read_text()
    tipos = re.findall(r"id:\s*'(\w+)',\s*nom:\s*'([^']+)',\s*sub:\s*'[^']*',\s*base:\s*(\d+),\s*uf:\s*([\d.]+)", fuente)
    if len(tipos) < 4:
        raise SystemExit('No se pudieron leer los precios de site/_estimador.html.')
    salida = []
    for id_, nom, base, uf in tipos:
        plata = f"${int(base):,}".replace(',', '.')
        uf_txt = uf.replace('.', ',') if '.' in uf else uf
        salida.append(dict(id=id_, nom=nom, base=int(base), plata=plata, uf=uf_txt))
    return salida


def lista_precios():
    """La lista corta de precios del inicio."""
    filas = [f'        <li><span>{t["nom"]}</span><b>desde {t["plata"]}</b><small>+ {t["uf"]} UF al mes</small></li>'
             for t in sorted(_tipos(), key=lambda x: x['base'])]
    return '\n'.join(filas)


# Que cubre cada precio de partida. Es un alcance chico a proposito: lo justo
# para empezar a usarlo. Lo demas se cotiza y se cierra por escrito.
ALCANCES = {
    'sistema': (
        ['Un primer módulo completo, hecho a tu medida: inventario, pedidos, clientes o cobranza.',
         'Hasta 10 usuarios, cada uno con su clave y lo que le toca ver.',
         'Tus datos de hoy, cargados desde tus planillas.',
         'Un panel con los números que tú decides mirar, y exportar a Excel.',
         'Funciona en el computador y en el celular, con respaldo diario.',
         'Dos sesiones de capacitación con tu equipo.'],
        'más módulos, conexiones con otros sistemas (correo, SII, banco, pasarela de pago) '
        'y ordenar datos históricos desordenados.'),
    'web': (
        ['Un sitio de hasta 4 páginas: inicio, lo que vendes, quiénes son y contacto.',
         'Diseño propio, adaptado a celular.',
         'Botón de WhatsApp y un formulario que llega a tu correo.',
         'Lo básico para aparecer en Google, y te ayudamos a dejar lista tu ficha de Google Maps.',
         'Publicación con dominio y certificado de seguridad.'],
        'más páginas, tienda o pagos en línea, redactar todos los textos y fotos profesionales.'),
    'tienda': (
        ['Catálogo con categorías, filtros y buscador, con hasta 100 productos cargados por nosotros.',
         'Carro y pago en línea con Mercado Pago, Webpay o Flow. El convenio lo firmas tú.',
         'Stock que se descuenta con cada venta, y correos de confirmación y de despacho.',
         'Despacho con tarifas por comuna, o retiro en tu local.',
         'Un panel para que agregues y edites productos y veas los pedidos.'],
        'cargar más productos por ti, conectar con tu sistema de inventario o con un courier, '
        'y fotos o descripciones de productos.'),
    'app': (
        ['Una app que se instala desde el navegador en iPhone y Android, sin pasar por las tiendas.',
         'Hasta dos funciones principales, por ejemplo registrar visitas y pedidos, con hasta 10 usuarios.',
         'Funciona sin señal y se sincroniza cuando vuelve.',
         'Usa la cámara y la ubicación del teléfono, y avisa con notificaciones.',
         'Un panel web para revisar lo que registra tu equipo.'],
        'publicarla en App Store y Google Play, más funciones y conexiones con otros sistemas.'),
}


def partidas():
    """Que incluye cada precio de partida, en el orden del estimador."""
    bloques = []
    for t in _tipos():
        incluye, aparte = ALCANCES[t['id']]
        li = '\n'.join(f'            <li>{S.CHECK}<span>{x}</span></li>' for x in incluye)
        bloques.append(f'''      <article class="hoja partida posar" id="incluye-{t['id']}">
        <div class="hoja-barra"><span>{t['nom']}</span><span class="folio">desde {t['plata']}</span></div>
        <div class="partida-cuerpo">
          <ul class="lista-check">
{li}
          </ul>
          <p class="partida-aparte"><b>Se cotiza aparte:</b> {aparte}</p>
          <p class="partida-mes">Más {t['uf']} UF al mes de acompañamiento.</p>
        </div>
      </article>''')
    return '\n'.join(bloques)


def aplicar_fichas(txt):
    # El estimador vive en su propio archivo y lo usan dos paginas; va primero
    # porque dentro trae fichas ({WA}, {WA_NUM}) que se resuelven en el bucle.
    txt = txt.replace('{ESTIMADOR}', (CUERPOS / '_estimador.html').read_text())
    txt = txt.replace('{ESCENA}', (CUERPOS / '_escena.html').read_text())
    if '{LISTA_PRECIOS}' in txt:
        txt = txt.replace('{LISTA_PRECIOS}', lista_precios())
    if '{PARTIDAS}' in txt:
        txt = txt.replace('{PARTIDAS}', partidas())
    for k, v in FICHAS.items():
        txt = txt.replace(k, v)
    return txt


# ---------- paginas normales ----------

def construir_paginas():
    for p in PAGINAS:
        cuerpo = aplicar_fichas((CUERPOS / f"{p['slug'].replace('index', 'inicio')}.body.html").read_text())
        partes = []
        c = p['cabecera']
        if c:
            partes.append(S.cabecera(c['titulo'], c['bajada'],
                                     visual=aplicar_fichas(c.get('visual', '')),
                                     acciones=aplicar_fichas(c.get('acciones', ''))))
        partes.append(cuerpo)
        cierre = p.get('cierre', {})
        if cierre is not False:
            partes.append(S.cierre(**cierre))
        ld = []
        if p['slug'] not in ('index', '404'):
            ld.append(migas_ld([('Inicio', 'index.html'), ((c or p)['nombre'], None)]))
        if p['slug'] in ('contacto', 'precios'):
            faq = faq_ld(cuerpo)
            if faq:
                ld.append(faq)
        if p['slug'] == 'servicios':
            ld.append(servicios_ld())

        html = S.render(
            titulo=p['titulo'], descripcion=p['desc'], cuerpo='\n\n'.join(partes),
            activa=p['activa'], js_extra=p.get('js_extra', ''),
            canonico='' if p['slug'] == 'index' else f"{p['slug']}.html",
            clase_body=p.get('clase_body', ''),
            ld_extra=ld,
            preload=p.get('preload', ()),
            og_img=p.get('og_img', 'assets/og.jpg'),
            landing=p.get('landing', False),
            pie_minimo=p.get('pie_minimo', False),
        )
        if p['slug'] == '404':
            # que los buscadores no la guarden como si fuera contenido
            html = html.replace('<meta name="description"',
                                '<meta name="robots" content="noindex">\n<meta name="description"')
        destino = SALIDA / f"{p['slug']}.html"
        destino.write_text(html)
        yield destino


# ---------- paginas de caso y de productos propios ----------

def ficha_caso(c, propio=False):
    filas = c.get('ficha') or [('Cliente', c['titulo']),
                               ('Sector', c['sector']),
                               ('Tipo de proyecto', c['tipo']),
                               ('Estado', 'En línea')]
    dl = '\n'.join(f'        <div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in filas)
    boton = c.get('boton', (c.get('sitio'), c.get('sitio_url')))
    enlace = ''
    if boton and boton[1]:
        externo = ' target="_blank" rel="noopener"' if boton[1].startswith('http') else ''
        enlace = f'\n      <a class="btn btn-pieza" href="{boton[1]}"{externo}>{boton[0]}</a>'
    titulo = 'Ficha del producto' if propio else 'Ficha del proyecto'
    folio = 'Producto propio' if propio else c['sector']
    return f'''    <aside class="ficha hoja">
      <div class="hoja-barra"><span>{titulo}</span><span class="folio">{folio}</span></div>
      <dl>
{dl}
      </dl>{enlace}
    </aside>'''


def figura_html(src, alt, pie, ancho, alto, plana=False):
    if not src:
        # Todavia no hay captura: se deja el hueco a la vista, con el mismo
        # marcador que el resto de los datos por confirmar.
        return f'''        <figure>
          <div class="hoja captura-pendiente"><p>{S.PENDIENTE} {pie}</p></div>
        </figure>'''
    # Las capturas de una app no van en una hoja: no son un documento.
    marco = 'captura-plana' if plana else 'hoja'
    return f'''        <figure class="posar">
          <div class="{marco}"><img src="{src}" alt="{alt}" width="{ancho}" height="{alto}" loading="lazy"></div>
          <figcaption>{pie}</figcaption>
        </figure>'''


def cuerpo_caso(c):
    extra = c.get('figuras', {})
    out = []
    for i, (titulo, parrafos) in enumerate(c['bloques']):
        out.append(f'        <h2>{titulo}</h2>')
        out.extend('        ' + p for p in parrafos)
        if i == 0 and not c.get('portada'):
            fig = figura_html(c['figura'], c['figura_alt'], c['figura_pie'],
                              c['ancho'], c['alto'], c.get('figura_plana', False))
            # la primera imagen se ve sin desplazar: ni carga diferida ni entrada
            out.append(fig.replace(' loading="lazy"', '', 1).replace(' class="posar"', '', 1))
        if i in extra:
            out.append(figura_html(*extra[i]))
    if c.get('testimonio') and not c.get('pantallas'):
        cita, firma = c['testimonio']
        out.append(f'''        <figure class="cita">
          <blockquote><p>{cita}</p></blockquote>
          <figcaption>{firma}</figcaption>
        </figure>''')
    return '\n'.join(out)


def portada_caso(c):
    """La figura principal en grande bajo el titulo, con su version de celular."""
    src, src_movil, alto_movil, alt, pie = c['portada']
    return f'''<section class="mp-pantalla">
  <div class="wrap">
    <figure>
      <div class="hoja">
        <picture>
          <source media="(max-width: 640px)" srcset="{src_movil}" width="860" height="{alto_movil}">
          <img src="{src}" width="{c['ancho']}" height="{c['alto']}" alt="{alt}">
        </picture>
      </div>
      <figcaption><span class="ejemplo">{pie}</span></figcaption>
    </figure>
  </div>
</section>'''


def pantallas_caso(c):
    """Que construimos (una pantalla por funcion), las decisiones y la cita."""
    filas = '\n'.join(f'''      <div class="funcion">
        <div class="funcion-texto">
          <h3>{titulo}</h3>
          <p>{texto}</p>
        </div>
        <figure class="posar">
          <div class="hoja"><img src="{src}" width="860" height="{alto}" loading="lazy" alt="{alt}"></div>
          <figcaption><span class="ejemplo">Datos de ejemplo</span></figcaption>
        </figure>
      </div>''' for titulo, texto, src, alto, alt in c['pantallas'])
    partes = [f'''<section class="seccion" style="padding-top:0">
  <div class="wrap">
    <div class="cabeza-seccion">
      <h2>Qué construimos</h2>
      <p class="bajada">{c.get('intro_pantallas', '')}</p>
    </div>
    <div class="funciones">
{filas}
    </div>
  </div>
</section>''']
    tarjetas = '\n'.join(f'''      <div class="decision hoja posar">
        <h3>{t}</h3>
        <p>{x}</p>
      </div>''' for t, x in c.get('decisiones', []))
    cita = ''
    if c.get('testimonio'):
        texto, firma = c['testimonio']
        cita = f'''
    <figure class="cita">
      <blockquote><p>{texto}</p></blockquote>
      <figcaption>{firma}</figcaption>
    </figure>'''
    partes.append(f'''<section class="seccion decisiones-caso" style="padding-top:0">
  <div class="wrap">
    <div class="cabeza-seccion">
      <h2>Las decisiones que importaron</h2>
    </div>
    <div class="decisiones">
{tarjetas}
    </div>{cita}
  </div>
</section>''')
    return '\n\n'.join(partes)


def construir_casos():
    lotes = [(c, False) for c in CASOS] + [(c, True) for c in PRODUCTOS]
    for c, propio in lotes:
        nombre = c.get('etiqueta', c['titulo'])
        if propio:
            pre = 'producto'
            camino = [('Inicio', 'index.html'),
                      ('Productos propios', 'nosotros.html#productos'), (nombre, None)]
            titulo = f"{nombre} — Producto propio | CORYN"
            cierre = S.cierre(
                titulo='Lo mismo, en tu empresa.',
                texto='Leer documentos con IA y cobrar en línea no son cosas de empresas '
                      'grandes. Cuéntanos qué te llega por correo o en papel y te decimos '
                      'cómo se resolvería.',
                secundario='<a class="enlace enlace-claro" href="correo.html">Si todo te llega por correo</a>')
        else:
            pre = 'caso'
            camino = [('Inicio', 'index.html'), ('Proyectos', 'nosotros.html#recorrido'),
                      (nombre, None)]
            titulo = f"{nombre} — Caso de proyecto | CORYN"
            cierre = S.cierre(
                secundario='<a class="enlace enlace-claro" href="nosotros.html#recorrido">Ver otros proyectos</a>')
        cabecera = S.cabecera(c['h1'], c['lead'], migas=camino)
        cuerpo = f'''<section class="seccion" style="padding-top:0">
  <div class="wrap caso-grid">
    <article class="caso-body">
{cuerpo_caso(c)}
    </article>
{ficha_caso(c, propio)}
  </div>
</section>'''
        partes = [cabecera]
        if c.get('portada'):
            partes.append(portada_caso(c))
        partes.append(cuerpo)
        if c.get('pantallas'):
            partes.append(pantallas_caso(c))
        partes.append(cierre)
        # Con portada no se precarga: en el celular se baja otra imagen.
        precarga = (c['figura'],) if c['figura'] and not c.get('portada') else ()
        html = S.render(
            titulo=titulo,
            descripcion=c['meta_desc'],
            cuerpo='\n\n'.join(partes),
            activa='', og_img=c['figura'] or 'assets/og.jpg', og_tipo='article',
            canonico=f"{pre}-{c['slug']}.html",
            ld_extra=[migas_ld(camino), caso_ld(c, propio)],
            preload=precarga)
        destino = SALIDA / f"{pre}-{c['slug']}.html"
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
    urls += [(f"https://coryndev.com/producto-{c['slug']}.html",
              _ultimo_cambio('casos_data.py')) for c in PRODUCTOS]
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
