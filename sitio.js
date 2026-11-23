/* CORYN — codigo comun del sitio.
   Menu, referidos, videos, antes/despues y movimiento. Todo lo que se ve en
   la pagina esta visible sin este archivo: aqui solo se le agrega vida. */
(function () {
  'use strict';

  var d = document;
  var raiz = d.documentElement;
  var quieto = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- barra de navegacion ---------- */
  var nav = d.getElementById('nav');
  if (nav) {
    var borde = function () { nav.classList.toggle('con-borde', window.scrollY > 8); };
    borde();
    window.addEventListener('scroll', borde, { passive: true });
  }

  var burger = d.getElementById('burger');
  var links = d.getElementById('navLinks');
  if (burger && links) {
    var cierra = function () {
      d.body.classList.remove('menu-abierto');
      burger.setAttribute('aria-expanded', 'false');
      burger.setAttribute('aria-label', 'Abrir menú');
    };
    burger.addEventListener('click', function () {
      var abierto = d.body.classList.toggle('menu-abierto');
      burger.setAttribute('aria-expanded', abierto ? 'true' : 'false');
      burger.setAttribute('aria-label', abierto ? 'Cerrar menú' : 'Abrir menú');
    });
    links.addEventListener('click', function (e) { if (e.target.tagName === 'A') cierra(); });
    d.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && d.body.classList.contains('menu-abierto')) { cierra(); burger.focus(); }
    });
  }

  /* ---------- codigo de referido ----------
     Llega en la URL desde el QR del volante o desde el link que comparte un
     referidor. Se guarda 30 dias y se agrega al mensaje de WhatsApp en el
     momento del clic, asi se sabe quien trajo a la persona. */
  window.CORYN = window.CORYN || {};
  (function () {
    var CLAVE = 'coryn_ref', DIAS = 30;
    function limpio (v) { return (v || '').trim().slice(0, 24).replace(/[^A-Za-z0-9_-]/g, ''); }
    function guardado () {
      try {
        var x = JSON.parse(localStorage.getItem(CLAVE) || 'null');
        if (x && x.ref && Date.now() < x.vence) return x.ref;
        if (x) localStorage.removeItem(CLAVE);
      } catch (e) { /* modo privado o storage bloqueado */ }
      return '';
    }
    var deUrl = '';
    try { deUrl = limpio(new URLSearchParams(location.search).get('ref')); } catch (e) {}
    if (deUrl) {
      try { localStorage.setItem(CLAVE, JSON.stringify({ ref: deUrl, vence: Date.now() + DIAS * 864e5 })); } catch (e) {}
    }
    var ref = deUrl || guardado();
    window.CORYN.ref = ref;
    if (!ref) return;
    try {
      window.va = window.va || function () { (window.vaq = window.vaq || []).push(arguments); };
      window.va('event', { name: 'referido', data: { ref: ref } });
    } catch (e) {}
    d.addEventListener('click', function (e) {
      var el = e.target;
      if (el && el.nodeType !== 1) el = el.parentElement;
      var a = el && el.closest ? el.closest('a[href*="wa.me"]') : null;
      if (!a) return;
      var u;
      try { u = new URL(a.href); } catch (err) { return; }
      var t = u.searchParams.get('text') || 'Hola CORYN';
      if (t.indexOf('(Ref:') > -1) return;
      // se rearma a mano: searchParams.set escribe los espacios como "+"
      a.href = u.origin + u.pathname + '?text=' + encodeURIComponent(t + ' (Ref: ' + ref + ')');
    }, true);
  })();

  /* ---------- videos: solo mientras se ven ---------- */
  var videos = [].slice.call(d.querySelectorAll('video.vid'));
  if (videos.length && !quieto && 'IntersectionObserver' in window) {
    var ioVid = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        var v = e.target;
        if (e.isIntersecting && !d.hidden) {
          if (v.preload === 'none') v.preload = 'auto';
          var p = v.play();
          if (p && p.catch) p.catch(function () {});
        } else {
          v.pause();
        }
      });
    }, { threshold: 0.25 });
    videos.forEach(function (v) { ioVid.observe(v); });
    d.addEventListener('visibilitychange', function () {
      if (d.hidden) videos.forEach(function (v) { v.pause(); });
    });
  }

  /* ---------- antes / despues ---------- */
  [].forEach.call(d.querySelectorAll('[data-ad]'), function (caja) {
    var botones = caja.querySelectorAll('.ad-botones button');
    [].forEach.call(botones, function (b) {
      b.addEventListener('click', function () {
        caja.classList.toggle('despues', b.dataset.v === 'despues');
        [].forEach.call(botones, function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      });
    });
  });

  /* ---------- movimiento ---------- */
  function suelta () { raiz.classList.remove('mov'); }

  if (quieto || !raiz.classList.contains('mov')) return;
  if (!window.gsap || !window.ScrollTrigger) { suelta(); return; }

  try {
    var gsap = window.gsap;
    gsap.registerPlugin(window.ScrollTrigger);
    var ST = window.ScrollTrigger;
    var ease = 'expo.out';

    // Hojas que se posan sobre el escritorio
    ST.batch('.posar', {
      start: 'top 88%', once: true,
      onEnter: function (els) {
        els.forEach(function (el) { el.classList.remove('posar'); });
        gsap.from(els, { y: 30, rotation: '-=1.6', opacity: 0, duration: 0.95, ease: ease,
          stagger: 0.09, clearProps: 'transform,opacity' });
      }
    });

    // Timbres que estampan
    function estampa (el, retraso) {
      el.classList.remove('estampa');
      gsap.timeline({ delay: retraso || 0 })
        .from(el, { scale: 1.5, opacity: 0, duration: 0.26, ease: 'power3.in' })
        .to(el, { scale: 0.96, duration: 0.07, ease: 'power1.out' })
        .to(el, { scale: 1, duration: 0.22, ease: 'power2.out', clearProps: 'transform,opacity' });
    }
    ST.batch('.timbre.estampa', {
      start: 'top 90%', once: true,
      onEnter: function (els) { els.forEach(function (el, i) { estampa(el, 0.15 + i * 0.22); }); }
    });

    // Post-its que se pegan
    ST.batch('.postit.pegar', {
      start: 'top 90%', once: true,
      onEnter: function (els) {
        var papeles = els.map(function (el) { el.classList.remove('pegar'); return el.querySelector('.postit-papel'); });
        gsap.from(papeles, { y: -18, rotation: '+=8', scale: 1.05, opacity: 0, duration: 0.8,
          ease: ease, stagger: 0.08, clearProps: 'transform,opacity' });
      }
    });

    // La linea de una venta: cada estacion se enciende al pasar
    [].forEach.call(d.querySelectorAll('.linea-venta'), function (ol) {
      var est = ol.querySelectorAll('.estacion');
      ST.create({
        trigger: ol, start: 'top 82%', end: 'top 32%', scrub: 0.6,
        onUpdate: function (s) {
          var p = s.progress;
          ol.style.setProperty('--avance', p.toFixed(3));
          [].forEach.call(est, function (e, i) { e.classList.toggle('on', p >= i / (est.length - 1) - 0.002); });
        }
      });
    });

    // Las etapas del proceso, en la misma gramatica que la linea de la venta
    [].forEach.call(d.querySelectorAll('.etapas'), function (cont) {
      var barra = cont.querySelector('.etapas-avance');
      if (barra) {
        ST.create({
          trigger: cont, start: 'top 60%', end: 'bottom 60%', scrub: 0.6,
          onUpdate: function (s) { barra.style.setProperty('--avance', s.progress.toFixed(3)); }
        });
        barra.style.setProperty('--avance', '0');
      }
      [].forEach.call(cont.querySelectorAll('.etapa'), function (et) {
        ST.create({ trigger: et, start: 'top 62%', onEnter: function () { et.classList.add('on'); },
          onLeaveBack: function () { et.classList.remove('on'); } });
      });
    });

    // El cierre: la pieza encaja en la C
    [].forEach.call(d.querySelectorAll('.cierre-marca'), function (m) {
      var p = m.querySelector('.p');
      ST.create({ trigger: m, start: 'top 80%', once: true, onEnter: function () {
        gsap.fromTo(p, { x: 70, opacity: 0 }, { x: 0, opacity: 1, duration: 1.1, ease: ease, delay: 0.15,
          onComplete: function () { m.classList.add('encajada'); } });
      } });
    });

    escena(gsap, ST);
    window.CORYN_MOV = true;
  } catch (err) {
    suelta();
  }

  /* ---------- la escena de la portada ----------
     Tres correos entran a la bandeja; el sistema los lee (resaltado azul),
     el dato viaja hasta la hoja del sistema y queda anotado. Al terminar, la
     pieza encaja. Se repite mientras se ve y se detiene fuera de pantalla. */
  function escena (gsap, ST) {
    var raizEscena = d.querySelector('.escena');
    if (!raizEscena) return;
    var correos = [].slice.call(raizEscena.querySelectorAll('.correo'));
    var filas = [].slice.call(raizEscena.querySelectorAll('.fila.nueva'));
    var cuenta = raizEscena.querySelector('.cuenta');
    var pieza = raizEscena.querySelector('.pieza-slot i');
    var viaje = d.createElement('span');
    viaje.className = 'viaje';
    viaje.setAttribute('aria-hidden', 'true');
    raizEscena.appendChild(viaje);

    function texto (n) { return n === 1 ? '1 sin leer' : n + ' sin leer'; }

    function reinicia () {
      correos.forEach(function (c) { c.classList.remove('leido'); });
      filas.forEach(function (f) { f.classList.remove('llena', 'recien'); });
      if (cuenta) cuenta.textContent = texto(correos.length);
      gsap.set(pieza, { opacity: 0, y: -26, rotation: -90 });
    }

    function vuela (i) {
      var c = correos[i], f = filas[i];
      var origen = c.querySelector('.cifra') || c;
      var destino = f.querySelector('.col-doc') || f;
      var r0 = raizEscena.getBoundingClientRect();
      var a = origen.getBoundingClientRect(), b = destino.getBoundingClientRect();
      viaje.textContent = origen.getAttribute('data-viaje') || origen.textContent;
      gsap.fromTo(viaje,
        { x: a.left - r0.left, y: a.top - r0.top - 4, opacity: 0, scale: 0.9 },
        { keyframes: [
            { opacity: 1, scale: 1, duration: 0.18, ease: 'power2.out' },
            { x: b.left - r0.left, y: b.top - r0.top - 2, duration: 0.7, ease: 'power3.inOut' },
            { opacity: 0, duration: 0.2 }
          ] });
    }

    var tl = gsap.timeline({ repeat: -1, paused: true, delay: 0.5 });
    tl.call(reinicia, null, 0);
    correos.forEach(function (c, i) {
      var t = 0.7 + i * 2.1;
      var barra = c.querySelector('.lectura');
      tl.fromTo(barra, { scaleX: 0, opacity: 1 }, { scaleX: 1, duration: 0.6, ease: 'power2.inOut' }, t)
        .call(function () {
          c.classList.add('leido');
          if (cuenta) cuenta.textContent = texto(correos.length - i - 1);
        }, null, t + 0.6)
        .to(barra, { opacity: 0, duration: 0.3 }, t + 0.62)
        .call(vuela, [i], t + 0.7)
        .call(function () {
          filas[i].classList.add('llena', 'recien');
          setTimeout(function () { filas[i].classList.remove('recien'); }, 900);
        }, null, t + 1.5);
    });
    var fin = 0.7 + correos.length * 2.1;
    tl.to(pieza, { opacity: 1, y: 0, rotation: 0, duration: 0.7, ease: 'expo.out' }, fin)
      .to({}, { duration: 3.4 }, fin + 0.7);

    reinicia();
    ST.create({
      trigger: raizEscena, start: 'top bottom', end: 'bottom top',
      onToggle: function (s) { if (s.isActive && !d.hidden) tl.play(); else tl.pause(); }
    });
    d.addEventListener('visibilitychange', function () {
      if (d.hidden) tl.pause();
      else if (ST.isInViewport(raizEscena)) tl.play();
    });
  }
})();
