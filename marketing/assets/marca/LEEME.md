# Marca CORYN — version plana

Redibujo vectorial del logo de las dos alas. Plano, sin degradados, con
transparencia real. Reemplaza al PNG con degradado, que no servia para los
tamanos donde el logo vive de verdad (favicon, avatar, tapas de destacadas).

## Archivos

| Archivo | Para que |
|---|---|
| `marca.svg` | Dos colores. El uso normal, sobre fondo claro |
| `marca-mono.svg` | Un solo azul. Para cuando el fondo compite o hay que imprimir barato |
| `marca-blanca.svg` | Blanco. Sobre fondos oscuros: pagina de Servicios, volante, sello de los carruseles |
| `marca-512/192/180/48/32.png` | Iconos del sitio, todos con transparencia |
| `marca-perfil-1080.png` | Instagram y Google. Fondo blanco solido a proposito: un PNG transparente se ve negro en esas apps |

## Colores

- Ala superior `#1f5fe0` (el azul de marca, el mismo `--azul` del sitio)
- Ala inferior `#0f2f7a`

## Por que plano

El degradado cian-a-marino se convierte en una mancha bajo los 64px, y la
franja entre las dos alas se cierra. Probado: a 32px la version plana mantiene
las dos formas separadas y el degradado no.

El SVG es la fuente. Si hay que cambiar un color, se cambia ahi y se vuelven a
exportar los PNG; no hay que redibujar nada.
