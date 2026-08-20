# Material de difusión — CORYN

Genera el flyer comercial en PDF (2 páginas A4) + JPG/PNG de la página 1
para compartir por WhatsApp.

## Uso

```bash
python3 marketing/build.py --ref SOCIO01 --nombre "Nombre Apellido" --fono "+56 9 1234 5678"
```

| Flag | Qué hace |
|---|---|
| `--ref` | Código de referido. Aparece impreso en el flyer y viaja dentro del QR y del link a la web. |
| `--nombre` | Nombre del referidor, se imprime en la franja inferior. Si se omite, sale un texto genérico. |
| `--fono` | Teléfono del referidor (opcional), junto al nombre. |

Sale en `marketing/out/`:

- `flyer-coryn-<ref>.pdf` — documento completo, para adjuntar o imprimir.
- `flyer-coryn-<ref>-p1.jpg` — página 1 como imagen, para mandar por WhatsApp.
- `flyer-coryn-<ref>-p1.png` — misma imagen sin compresión.
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
