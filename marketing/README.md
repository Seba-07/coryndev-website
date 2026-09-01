# Material de difusión — CORYN

Genera el flyer comercial en PDF (1 página A4) + JPG/PNG para compartir por
WhatsApp.

El volante es deliberadamente de una hoja: se reparte como imagen y en un
teléfono nada bajo los 5mm se lee sin hacer zoom. No intenta contarlo todo,
sino que la persona entre a la web. Por eso el QR lleva a
`coryndev.com/?ref=<código>` y no a WhatsApp: así el referido queda registrado
y la persona cae en el estimador.

**Cualquier cifra que se agregue al volante tiene que estar también en el
sitio.** Los precios y las UF salen del estimador en `site/inicio.body.html`.

## Uso

```bash
python3 marketing/build.py --ref SOCIO01 --nombre "Nombre Apellido" --fono "+56 9 1234 5678"
```

| Flag | Qué hace |
|---|---|
| `--ref` | Código de referido. Aparece impreso en el flyer y viaja dentro del QR, que lleva a `coryndev.com/?ref=<código>`. |
| `--nombre` | Nombre del referidor, se imprime en la franja inferior. Si se omite, sale un texto genérico. |
| `--fono` | Teléfono del referidor (opcional), junto al nombre. |

Sale en `marketing/out/`:

- `flyer-coryn-<ref>.pdf` — para adjuntar o imprimir.
- `flyer-coryn-<ref>.jpg` — la hoja como imagen, para mandar por WhatsApp.
- `flyer-coryn-<ref>.png` — misma imagen sin compresión.
- `flyer-coryn-<ref>.html` — fuente autocontenida (todo embebido en base64).

## Archivos

- `flyer.template.html` — diseño y textos del flyer. Editar aquí para cambiar copy.
- `build.py` — genera QR, reemplaza variables y renderiza con Chrome headless.
- `assets/` — logo recortado con fondo transparente.
- `kit-referidor.md` — guion de mensajes y guía para quien difunde el material.

## Requisitos

- Google Chrome instalado en `/Applications/Google Chrome.app` (renderiza el PDF).
- `pip install segno pillow` (QR e imagen).
- Fuente **Inter** instalada. Sin ella cae a la fuente del sistema y cambia el ancho
  de los textos.

---

## Carruseles de Instagram

```bash
python3 marketing/posts.py            # los seis casos
python3 marketing/posts.py --caso 3   # solo uno
python3 marketing/posts.py --listar   # ver que casos hay
python3 marketing/posts.py --perfil   # foto de perfil, 1080x1080
python3 marketing/posts.py --destacadas  # portadas de destacadas
python3 marketing/posts.py --historias precios   # historias de una destacada
```

Sale en `marketing/out/instagram/caso-<n>/`: cuatro imágenes de 1080x1350 (el
formato que más alto ocupa en el feed) y un `texto.txt` con el pie del post
listo para pegar.

**El copy no se escribe acá.** Se extrae de `site/que-resolvemos.body.html`, que
es donde ya vive redactado. Si cambias un problema en el sitio, se regeneran los
posts y quedan alineados solos. Si alguna vez cambia la estructura de esa
página, `posts.py` avisa en vez de generar piezas vacías.

Las cuatro láminas son: el problema (gancho), lo que te cuesta, cómo queda
resuelto, y el cierre con la marca.

- `post.template.html` — diseño y tamaños de los carruseles.
- `destacada.template.html` — portadas de destacadas.
- `historia.template.html` — historias (1080x1920).
- `ficha-google.md` — contenido para el Perfil de Empresa de Google.
- `instagram.md` — perfil, bio, destacadas y orden de publicación.
