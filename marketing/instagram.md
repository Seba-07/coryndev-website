# Instagram — CORYN

Todo lo que hay que configurar y publicar. Las piezas se generan con
`python3 marketing/posts.py` (ver README).

---

## 1. El perfil

| Campo | Qué poner | Límite |
|---|---|---|
| Usuario | `@coryn.studio` (ya creada) | 30 |
| Nombre | `CORYN · Software a medida` | 30 |
| Categoría | Servicio de desarrollo de software | — |
| Tipo de cuenta | **Empresa** (no Creador) | — |
| Foto | `marketing/out/instagram/perfil.png` | — |
| Enlace | `https://coryndev.com/?ref=INSTAGRAM` | — |
| Botón de contacto | Correo: contacto@coryndev.com | — |
| Botón de WhatsApp | Conectar el número | — |

**El campo "Nombre" es el que más rinde y casi nadie usa bien.** El buscador de
Instagram indexa el nombre y el usuario, **no la bio**. Si ahí dice solo
"CORYN", apareces únicamente cuando ya te buscan por marca. Con
`CORYN · Software a medida` apareces también cuando alguien busca "software".
Son 25 caracteres, entra.

**El botón de WhatsApp no publica tu número:** abre la conversación sin
mostrarlo. Es exactamente lo mismo que hicimos en el volante, así que calza con
no exponer el número.

**El enlace lleva `?ref=INSTAGRAM`.** Como el sitio ya registra el referido y lo
pega al mensaje de WhatsApp y al formulario, cada contacto que llegue desde
Instagram te va a llegar marcado. Es la forma de saber, en un par de meses, si
el canal sirve o no.

---

## 2. La bio (máx. 150 caracteres)

**La que recomiendo** — 130 caracteres:

```
Software a la medida de cómo trabaja tu pyme.
Sistemas, sitios, tiendas y apps.
Precio cerrado antes de empezar.
Calcula lo tuyo ↓
```

Por qué esta: dice **qué haces** en la primera línea (que es la única que se ve
sin desplegar), **qué vendes** en la segunda, **la objeción resuelta** en la
tercera, y manda al enlace en la cuarta. Nada de "apasionados por la
tecnología", que no dice nada y lo pone todo el mundo.

**Alternativa más directa al dolor** — 139 caracteres:

```
¿Tu negocio funciona a punta de Excel y WhatsApp?
Construimos el sistema que te ordena la operación.
Pymes de todo Chile.
Calcula lo tuyo ↓
```

Sirve mejor si vas a pautar o si el perfil recibe gente fría, porque parte por
el problema en vez de por lo que vendes. Es la misma lógica del volante.

**No conviene** poner el correo ni el teléfono en la bio: gastan caracteres y ya
están en los botones de contacto, que además son tocables.

---

## 3. Destacadas (highlights)

Las portadas están generadas en `marketing/out/instagram/destacadas/`:

| Portada | Nombre | Contenido |
|---|---|---|
| `que-hacemos.png` | Qué hacemos | **8 historias** en `historias/que-hacemos/` |
| `casos.png` | Casos | **6 historias** en `historias/casos/` |
| `precios.png` | Precios | **5 historias** en `historias/precios/` |
| `proceso.png` | Proceso | **7 historias** en `historias/proceso/` |

```bash
python3 marketing/posts.py --destacadas             # las cuatro tapas
python3 marketing/posts.py --historias que-hacemos  # el contenido de cada una
python3 marketing/posts.py --historias casos
python3 marketing/posts.py --historias precios
python3 marketing/posts.py --historias proceso
```

**Todo sale del sitio, nada está escrito en el generador:** los servicios de
`servicios.body.html`, las etapas de `proceso.body.html`, los precios del
estimador y los casos de `casos_data.py`. Si cambias algo en la web, regeneras
y las historias quedan al día. Y si alguna de esas páginas cambia de
estructura, el generador avisa en vez de producir historias vacías.

**Una destacada son dos cosas:** la **portada** (el círculo del perfil) y el
**contenido** (las historias que se abren al tocarlo). Las tapas solas no
comunican nada: hay que subir las historias y después marcar la portada.

Cómo se sube: publicar las historias en orden, y una vez publicadas crear la
destacada agrupándolas. La portada se elige al final, desde *Editar destacada*.

**Los precios salen del estimador del sitio**, no están escritos en el
generador. Si cambias uno en `site/inicio.body.html`, regeneras y las historias
quedan al día.

**Fondo claro**, a juego con el feed. No blanco puro: el perfil de Instagram ya
es blanco y un círculo blanco desaparecería contra el fondo, así que van sobre
un papel azulado con el símbolo en el azul de marca.

**Por qué símbolos y no fotos.** En el perfil, la portada se ve en un círculo de
unos 64px. A ese tamaño una fotografía se convierte en una mancha: probado,
no se distingue nada. Un símbolo plano sí se lee. Además la portada no lleva
texto, porque Instagram escribe el nombre debajo del círculo.

**El nombre, corto.** Instagram corta los nombres largos de destacada: por eso
"Proceso" y no "Cómo trabajamos", que quedaba justo en el límite.

"Precios" como destacada es raro en el rubro y ahí está la gracia: casi ninguna
agencia los publica, y tú sí. Es coherente con el "sin letra chica" del sitio.

---

## 4. Orden de publicación

Los seis carruseles ya generados, uno cada dos semanas. Este orden parte por los
problemas más transversales y deja los de nicho para después:

| # | Carrusel | Por qué acá |
|---|---|---|
| 1 | `caso-1` Tu operación vive en una planilla | El más universal, y donde más aportas |
| 2 | `caso-2` Te buscan en Google y no apareces | El de entrada más barata ($69.000) |
| 3 | `caso-3` Explicas lo mismo por WhatsApp | El que más se reconoce al toque |
| 4 | `caso-5` No sabes si ganaste hasta fin de mes | Duele y se entiende sin explicar |
| 5 | `caso-4` Todo se agenda por teléfono | Más de nicho: servicios con hora |
| 6 | `caso-6` Los pedidos se pierden | Más de nicho: talleres y producción |

Cada carpeta trae las cuatro imágenes y el `texto.txt` con el pie listo.

**Las cuatro láminas llevan imagen real, y el fondo es claro.** La primera
versión era oscura y de puro texto: se leía como plantilla genérica, que es
justo lo que se reconoce a distancia. Ahora manda la fotografía y el texto va
abajo sobre blanco, que además es lo que mejor se ve en el feed de Instagram.

| Lámina | Imagen |
|---|---|
| 01 · el problema | La foto real del negocio, con el sello "Hoy" |
| 02 · lo que cuesta | Una foto propia del costo: la silla vacía, el local sin nadie |
| 03 · la solución | La captura del sistema, en español y distinta en cada caso |
| 04 · el cierre | Un llamado a la acción propio de cada caso |

**El cierre no se repite.** bySIMMED y AvenProp salen solo en la primera
publicación: si la prueba va en las seis, se gasta. Las otras cierran mostrando
hasta dónde puede llegar ese mismo problema resuelto — del sitio a la app, del
catálogo al reparto, de la cobranza al negocio completo.

Las imágenes salen del propio bloque de `que-resolvemos`, que ya tiene el par
antes/después de cada problema. Si cambias una foto en el sitio, se cambia sola
acá. Nada de fotos de banco ni generadas: son las mismas del sitio, con manos,
mostradores y talleres de verdad.

---

## 5. Sin fotos de personas

Perfil con el símbolo, y contenido de trabajo real. CORYN es una SpA, no un
unipersonal: amarrar la marca a una cara estorba el día que quieras delegar.

Lo que sí conviene mostrar, cuando haya: pantallas de sistemas andando, el antes
y el después de una operación, una función entregada este mes.

---

## 6. Pendientes

1. ~~Agregar el perfil al `sameAs` del sitio.~~ **Hecho:**
   `https://www.instagram.com/coryn.studio/` ya está declarado en
   `site_shell.py`, así Google sabe que el sitio y la cuenta son la misma
   empresa. Cuando exista la ficha de Google, su URL va en esa misma lista.
2. Revisar en dos meses cuántos contactos llegaron con `Ref: INSTAGRAM`.

---

## 7. Sobre el nombre de usuario

La cuenta es `@coryn.studio`, mientras que el dominio y el correo son
**coryndev** (coryndev.com, contacto@coryndev.com). **Queda así:** `@coryndev`
está tomado por un tercero, no se puede unificar. Comprobado.

Como el usuario no dice a qué te dedicas, y "studio" además sugiere estudio
creativo o de diseño, el campo **Nombre** carga con ese trabajo:

    CORYN · Software a medida

Es el que indexa el buscador de Instagram y el que aclara el rubro. Por eso
importa más acá que en una cuenta cuyo usuario ya lo dijera todo.

*(La cuenta `@coryndev` de un tercero hoy está vacía: 0 seguidores. No es un
problema. Si algún día publicara y generara confusión con tu marca, Instagram
tiene un proceso de reclamo, pero exige tener la marca registrada.)*
