# Marca CORYN: archivos maestros

Logo elegido el 19 de octubre de 2026: una **C** de trazo grueso con una
**pieza** que encaja en su abertura. Es la idea de la empresa en un dibujo:
la pieza que le falta al negocio, a medida, sin sobrar nada. La palabra va
en Bricolage Grotesque 800, la misma tipografía del sitio y del material.

Colores: C y palabra en azul de marca **#0a1730**; pieza en **#1f5fe0**.
Sobre fondo oscuro la C y la palabra pasan a blanco y la pieza sigue azul.

Todos los SVG son puros trazados (sin texto ni fuentes): se abren igual en
cualquier programa.

| Archivo | Para qué |
|---|---|
| `simbolo.svg` | Solo el símbolo, a color. Avatar, favicon, sello. |
| `simbolo-mono.svg` / `-negro.svg` / `-blanco.svg` | Un solo color: timbre, bordado, fondos oscuros. |
| `palabra.svg` | Solo CORYN. |
| `logo-horizontal.svg` | Símbolo a la izquierda, palabra al lado. Cabeceras, firmas, documentos. |
| `logo-vertical.svg` | Símbolo arriba, palabra abajo. Etiqueta, perfil, portadas. |
| `*-mono` / `*-negro` / `*-blanco` | Variantes a un color de ambos lockups. |
| `etiqueta-color.jpg` | **La que se entrega a INAPI / SimpleMarca.** 1200×1200, fondo blanco, a color. |
| `google-logo.jpg` | Logo del Perfil de Empresa en Google: símbolo centrado, cuadrado, fondo blanco. |

Lo que se genera desde aquí (no se dibuja a mano):
- `/assets/favicon-48.png`, `icon-192.png`, `icon-512.png`, `apple-touch-icon.png`:
  fondo azul de marca, C blanca, pieza azul, 17 % de aire.
- `/assets/mark.webp` (cabecera) y `mark-claro.webp` (pie): símbolo a 96 px.
- `../mark.png` (400 px): el símbolo que usan las plantillas de posts,
  historias, reels y volante vía `{{MARK}}`.
- `../logo-full.png`, `../logo-alpha.png`, `../wordmark.png`: lockup
  vertical con y sin fondo, y la palabra sola.
- `/assets/og.jpg`: desde `site/og-card.html`.

Reglas:
- Bajo 20 px la pieza se funde con la C y queda una C con un punto. Sigue
  siendo reconocible; no hace falta una versión especial.
- No se estira, no se rota, no se le cambia el color de la pieza por otro
  que no sea el azul de marca o el mismo color de la C.
