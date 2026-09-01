# Prompts para las fotos que faltan

Hacen falta **seis fotos**, una por caso, para la **lámina 02** de cada carrusel
("lo que te cuesta"). Hoy esa lámina repite la foto de la lámina 01 y se nota.

Las fotos actuales (`assets/real-*.webp`) funcionan porque parecen lo que son:
un negocio chico de verdad. Estas tienen que calzar con esas, si no el carrusel
se parte en dos estilos.

---

## Estilo común (pegar en todos los prompts)

> Documentary photograph of a small family-run business in Chile. Natural window
> light, overcast day, no artificial lighting. Real clutter: worn surfaces,
> stacked paperwork, mismatched objects. Shot on a 35mm lens at f/2.8, shallow
> depth of field, slight background blur. Muted, slightly cool colors, natural
> grain, no color grading. Landscape orientation, 3:2. No people looking at the
> camera, no posed subjects, no faces visible. Candid, unstyled, imperfect.

## Reglas que evitan que se note

- **Nada de texto legible** en pantallas, papeles o carteles. Es donde la IA
  falla más y es lo primero que delata una imagen generada. Si aparece texto,
  que esté fuera de foco.
- **Nada de manos en primer plano.** Los dedos son el otro punto débil. Manos
  parciales, de lejos o cortadas por el encuadre, o ninguna.
- **Nada de caras.** Además de que la IA las arruina, evita el problema de
  publicar la imagen de una persona.
- **Nada de escritorio ordenado ni oficina corporativa.** Ese look de banco de
  imágenes es exactamente lo que quieres evitar.
- Apaisadas (3:2). En la lámina se recortan a 1080x660.

---

## Los seis prompts

### 1. La planilla — el costo: si falta esa persona, se para todo

> [estilo común] A small hardware store back office with an empty chair pulled
> away from a cluttered desk. A closed laptop sits among invoices and a cold cup
> of coffee. Shelves of stock visible out of focus behind. Nobody in the room.
> The feeling is of work interrupted and left unfinished.

### 2. Google — el costo: la venta que nunca supiste que existió

> [estilo común] Interior of a small empty shop seen from behind the counter,
> looking out through the window to the street. Blurred pedestrians walking past
> outside without coming in. Merchandise neatly on shelves, nobody browsing.
> Late afternoon light. A sense of waiting.

### 3. WhatsApp — el costo: cada interrupción corta el trabajo

> [estilo común] A workbench in a small workshop with a half-finished task
> abandoned mid-way: tools set down, packaging partly wrapped. A phone lying
> face-up on the bench, screen glowing with notifications, screen content out of
> focus and unreadable. Nobody present.

### 4. Teléfono — el costo: la hora que no se llenó

> [estilo común] An empty waiting area of a small service business: three or
> four simple chairs, a low table with worn magazines, a reception desk with a
> landline phone. Daylight from a window. Completely empty, mid-morning quiet.

### 5. Cobranza — el costo: la deuda vieja que ya no se cobra

> [estilo común] A stack of aging paper invoices in an overflowing folder on a
> desk, edges yellowed and curling, held with a bulldog clip. A basic calculator
> beside them, a pen. Papers spilling slightly. Shallow focus so no numbers or
> words are readable.

### 6. Pedidos — el costo: la información en tres lugares distintos

> [estilo común] A cramped workshop counter where order information lives in
> three places at once: a spiral notebook open with handwriting, loose printed
> sheets held by a clip, and a phone propped against a box. All slightly out of
> focus so nothing is readable. Cluttered, real, unstaged.

---

## Estado: hechas

Las seis están en `assets/costo-*.webp` y conectadas a la lámina 02.

`posts.py` las resuelve por nombre —`real-planilla` busca `costo-planilla`— y
si alguna faltara se cae a la foto del problema en vez de romper. Para cambiar
una, basta reemplazar el archivo y volver a generar.

---

## Si más adelante quieres reemplazarlas

1. Guardarlas como `assets/costo-planilla.webp`, `costo-google.webp`,
   `costo-whatsapp.webp`, `costo-telefono.webp`, `costo-cobranza.webp`,
   `costo-pedidos.webp` (mismo formato que las demás: WebP, ~1400px de ancho).
2. Avisar, y conecto la lámina 02 a esas fotos en `posts.py`.

---

## Una alternativa que sale mejor

Si en algún momento puedes sacar estas fotos tú mismo con el teléfono —en el
local de un cliente, en tu propio espacio de trabajo, en cualquier negocio
conocido— van a quedar mejor que cualquier prompt. No hace falta equipo: luz de
ventana y no ordenar nada antes de disparar.

Las seis que ya tienes funcionan justamente porque tienen detalles que nadie
inventaría: el post-it doblado, la taza a medio tomar, la mano con la manga
gastada. Eso es lo que una imagen generada no logra, y por eso lo notas a
distancia en otras páginas.
