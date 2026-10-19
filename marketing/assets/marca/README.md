# Marca CORYN: archivos maestros

El logo oficial es el ala de dos trazos con la palabra CORYN debajo. Estos
son los vectores, trazados desde `../mark.png` y `../wordmark.png`, para que
el símbolo sea **el mismo** en todas partes: sitio, íconos, redes, impresión
y el registro de marca.

| Archivo | Para qué |
|---|---|
| `simbolo.svg` | Solo el ala, azul de marca (#0a1730). Favicon, avatar, sello. |
| `palabra.svg` | Solo CORYN. |
| `logo.svg` | Ala + palabra, un color. La versión por defecto. |
| `logo-negro.svg` / `logo-blanco.svg` | Impresión a un color y fondos oscuros. |
| `etiqueta-bn.jpg` | Lo que se entrega a INAPI / SimpleMarca si la marca no reivindica colores. |
| `etiqueta-color.jpg` | Lo mismo, en azul, si se reivindican colores. |

Reglas:
- Bajo 48 px se usa siempre la versión plana. El degradado se pierde y el
  hueco entre los dos trazos se cierra.
- El degradado (`../mark.png`) queda para tamaños grandes en pantalla:
  cabecera del sitio, portadas, historias.
- Los íconos del sitio (`/assets/favicon-48.png`, `icon-192`, `icon-512`,
  `apple-touch-icon.png`) se generan desde `simbolo.svg`: ala blanca sobre
  azul de marca, con 18 % de aire. No se dibujan a mano.
