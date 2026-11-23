---
name: CORYN — Oficina ordenada
description: Hojas blancas sobre un escritorio gris frío; lo desordenado termina ordenado en un sistema hecho a tu medida.
colors:
  escritorio: "#eceff5"
  escritorio-2: "#e1e6ef"
  hoja: "#ffffff"
  tinta: "#0a1730"
  tinta-2: "#34435f"
  tinta-3: "#5a6782"
  linea: "#d3dae6"
  linea-suave: "#e7ecf3"
  pieza: "#1f5fe0"
  pieza-hondo: "#1648b8"
  pieza-suave: "#e0e9fd"
  pieza-tinta: "#123a8f"
  postit: "#ffe57f"
  wa: "#25c45e"
  wa-claro: "#33d26c"
  wa-tinta: "#032912"
  noche: "#0a1730"
  noche-2: "#13254a"
  en-noche: "#c9d5ee"
  en-noche-2: "#91a4ca"
  en-pieza: "#eaf0ff"
typography:
  display:
    fontFamily: "Bricolage Grotesque, Schibsted Grotesk, system-ui, sans-serif"
    fontSize: "clamp(2.6rem, 1.3rem + 4.7vw, 5.6rem)"
    fontWeight: 800
    lineHeight: 0.97
    letterSpacing: "-0.038em"
  headline:
    fontFamily: "Bricolage Grotesque, Schibsted Grotesk, system-ui, sans-serif"
    fontSize: "clamp(2rem, 1.15rem + 2.9vw, 3.6rem)"
    fontWeight: 800
    lineHeight: 1.02
    letterSpacing: "-0.032em"
  title:
    fontFamily: "Bricolage Grotesque, Schibsted Grotesk, system-ui, sans-serif"
    fontSize: "1.375rem"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.02em"
  body:
    fontFamily: "Schibsted Grotesk, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.58
    letterSpacing: "0em"
  lead:
    fontFamily: "Schibsted Grotesk, system-ui, sans-serif"
    fontSize: "clamp(1.1rem, 1rem + .45vw, 1.32rem)"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "0em"
  label:
    fontFamily: "Schibsted Grotesk, system-ui, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0em"
  mano:
    fontFamily: "Caveat, Bradley Hand, Segoe Print, cursive"
    fontSize: "1.62rem"
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: "-0.005em"
rounded:
  hoja: "4px"
  folio: "2px"
  campo: "8px"
  timbre: "9px"
  boton: "12px"
  chip: "999px"
spacing:
  xs: "8px"
  sm: "14px"
  md: "24px"
  lg: "44px"
  xl: "72px"
  seccion: "clamp(84px, 9vw, 136px)"
components:
  button-wa:
    backgroundColor: "{colors.wa}"
    textColor: "{colors.wa-tinta}"
    rounded: "{rounded.boton}"
    padding: "0 26px"
    height: "54px"
  button-wa-hover:
    backgroundColor: "{colors.wa-claro}"
  button-pieza:
    backgroundColor: "{colors.pieza}"
    textColor: "{colors.hoja}"
    rounded: "{rounded.boton}"
    padding: "0 26px"
    height: "54px"
  button-pieza-hover:
    backgroundColor: "{colors.pieza-hondo}"
  button-blanco:
    backgroundColor: "{colors.hoja}"
    textColor: "{colors.tinta}"
    rounded: "{rounded.boton}"
    padding: "0 26px"
    height: "54px"
  hoja:
    backgroundColor: "{colors.hoja}"
    textColor: "{colors.tinta}"
    rounded: "{rounded.hoja}"
  folio:
    textColor: "{colors.pieza}"
    rounded: "{rounded.folio}"
    padding: "0.25em 0.6em"
  postit:
    backgroundColor: "{colors.postit}"
    textColor: "{colors.tinta}"
    typography: "{typography.mano}"
    padding: "18px"
  estado-ok:
    backgroundColor: "{colors.pieza-suave}"
    textColor: "{colors.pieza-tinta}"
    rounded: "{rounded.chip}"
  campo:
    backgroundColor: "{colors.escritorio}"
    textColor: "{colors.tinta}"
    rounded: "{rounded.campo}"
    padding: "13px 14px"
---

## Overview

Mundo "Oficina ordenada": el sitio es un escritorio de oficina chilena. El fondo
es gris frío (escritorio), el contenido vive en hojas blancas de esquina viva, la
tinta es el azul marino del logo y el azul de la pieza marca lo que ya está en
orden: folios, timbres y lo que el sistema leyó. El amarillo del post-it es el
único color que no viene del logo y se usa solo para el desorden de hoy.

Una idea por sección, siempre con un gráfico propio (la bandeja que se lee sola,
la línea de una venta, post-its sobre el escritorio, una cotización, timbres).
Modo Persuade: la acción es escribir por WhatsApp. El logo (C + pieza, #0a1730 y
#1f5fe0) es marca registrada y no se rediseña.

## Colors

- **escritorio** es el fondo de página; **hoja** es la superficie de todo bloque
  de contenido con sombra de papel.
- **tinta**, **tinta-2** y **tinta-3** son texto principal, secundario y apagado;
  todos pasan 4.5:1 sobre escritorio y hoja.
- **pieza** es el único acento: botones secundarios, folios, timbres, resaltado
  de lectura, estaciones encendidas, el punto final de los títulos. Sus matices
  **pieza-suave** (fondo de lo leído o anotado) y **pieza-tinta** (texto sobre
  ese fondo).
- **noche** pinta las bandas oscuras (la prueba de bySIMMED, el cierre, el pie);
  el texto secundario ahí es **en-noche** / **en-noche-2**, nunca gris.
- **pieza** a página completa pinta el bloque del precio; el texto secundario ahí
  es **en-pieza**.
- **wa** solo en botones de WhatsApp, con texto **wa-tinta** (contraste 6.9:1).
- **postit** solo en notas de desorden (antes). Nunca en botones ni fondos.

## Typography

- Titulares en **Bricolage Grotesque** 800 con tracking negativo; el tamaño
  óptico lo resuelve el navegador. El display (h1) llega a 5.6rem.
- Texto en **Schibsted Grotesk** 400/600, 17 px en celular y 18 px desde 900 px,
  medida máxima ~66ch.
- **Caveat** solo dentro de post-its.
- Sin etiquetas sobre los títulos: el título carga solo. Las etiquetas de
  documento (folio, "Datos de ejemplo") viven dentro de los objetos, no sobre
  secciones.
- El punto final de un h1 se dibuja como la pieza del logo (`.punto`).
- Sin números tabulares: en esta letra separan el punto de miles.

## Layout

- Contenedor `min(1200px, 100% - 40px)`; secciones con padding vertical
  `clamp(84px, 9vw, 136px)`.
- Ritmo de fondos: escritorio, banda noche, escritorio, hoja, campo pieza,
  escritorio, cierre noche. Nunca dos bandas oscuras seguidas.
- Grillas de dos columnas desde 960–1040 px; todo apila en una sola columna
  debajo, sin desborde horizontal a 390 px.
- Cabecera de página interior: h1 + bajada, y a la derecha el gráfico de la
  página cuando lo tiene.

## Elevation & Depth

Profundidad de papel sobre escritorio, siempre con desplazamiento y desenfoque:
`--sombra-hoja` para hojas y `--sombra-alta` para fotos, videos y la cotización.
Las hojas se inclinan levemente (entre -1.4° y 1°) como papeles puestos a mano.
Sin halos de color ni sombras duras.

## Shapes

Esquinas casi vivas: hoja 4 px, folio 2 px. Botones 12 px, campos 8 px, estados
en píldora. El timbre lleva doble borde y una máscara de ruido que imita la tinta
de goma. Los marcadores de la línea de venta son cuadrados que giran a rombo al
encenderse.

## Components

- **Hoja** (`.hoja`, `.hoja-barra`): papel con barra de título; contiene tablas,
  formularios, cotizaciones y capturas.
- **Folio** (`.folio`): recuadro azul como el de una factura. Solo dentro de
  documentos.
- **Timbre** (`.timbre`, `.timbre-chico`): promesas estampadas en azul.
- **Post-it** (`.postit` > `.postit-papel`): el papel se mueve al pasar el
  cursor, el enlace no.
- **Escena** (`site/_escena.html`): bandeja de entrada + hoja de ventas, con
  datos de ejemplo y la etiqueta `.ejemplo`.
- **Línea de venta** (`.linea-venta` / `.estacion`) y **etapas** (`.etapas`):
  la misma gramática de estaciones que se encienden con el scroll.
- **Cotización** (`site/_estimador.html`): el estimador como documento, sobre el
  campo azul.
- **Marco de video** (`.marco-video`): video mudo en loop dentro de un marco de
  papel, con póster.
- **Cierre** (`S.cierre()`): un solo cierre para todo el sitio, con la C y la
  pieza que encaja.

## Do's and Don'ts

- Do: una idea por sección, con su gráfico; el texto, lo mínimo.
- Do: toda pantalla de un cliente con datos inventados y la etiqueta "Datos de
  ejemplo".
- Do: movimiento con significado y ya visible sin JavaScript: la lectura de la
  bandeja, hojas que se posan, timbres que estampan, post-its que se pegan, la
  línea que avanza. Con menos movimiento pedido, todo queda en su estado final y
  los videos no se reproducen.
- Don't: etiquetas o kickers sobre los títulos.
- Don't: barras de color a un costado de un recuadro (usar borde completo o
  tinte).
- Don't: tarjetas iguales de ícono + título + texto como estructura de página.
- Don't: repetir un tema en dos páginas: los problemas viven en Qué resolvemos,
  el cobro en Precios, las etapas en Proceso; el inicio resume y enlaza.
- Don't: el amarillo del post-it fuera de las notas de desorden.
