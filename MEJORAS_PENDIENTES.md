# Mejoras Pendientes — GIPIS

Ideas y funcionalidades a implementar en el futuro.

---

## 🔍 Búsqueda y filtrado de publicaciones — HECHO (2026-08-01)

**Implementado**: página `/investigacion/produccion` con toda la producción agrupada por
sección y filtros en el cliente (texto sobre título/autores, año y sección), más conteo
de citas vía OpenAlex y botón "Citar (BibTeX)" por ítem.

---

## 🗂️ Categorías fijas, galería y adjuntos en novedades — HECHO (2026-09-10)

**Implementado**:
- Categorías predefinidas (`app/news_meta.py`): Cooperación académica, Cooperación
  científica, Vinculación con empresas, Comunicación pública de la ciencia. Se guardan
  por clave en `News.category`, selector en el admin y filtro por categoría en
  `/novedades?categoria=<clave>` (chips arriba del listado). Valores viejos con texto
  libre se siguen mostrando tal cual.
- Galería de fotos por novedad (`NewsImage`: epígrafe ES/EN y orden). La primera es la
  portada de las tarjetas; con más de una, el detalle muestra un carrusel (JS propio,
  flechas, puntos, teclado y swipe). Archivos en `static/img/news/<slug>/`.
- Adjuntos (`NewsAttachment`: PDF, Office, ODF, ZIP) listados al pie del detalle, en
  `static/img/news/<slug>/archivos/`. Límite de subida elevado a 25 MB por envío.
- Fotos entre párrafos: en el contenido, `[foto N]` en una línea aparte inserta la foto N
  de la galería con su epígrafe (se resuelve al mostrar, en `main._render_news_content`).
- Migración `scripts/add_news_media.py` (crea tablas y pasa `news.image` a la galería),
  agregada al entrypoint.

**Ideas para después**: lightbox para ver las fotos en grande sin salir de la página;
alineación de fotos intercaladas (izquierda/derecha); editor con vista previa.

---

## 🔄 Harvesting de novedades desde redes sociales

**Prioridad**: Alta  
**Descripción**: Alimentar automáticamente las tarjetas de Novedades con las publicaciones
del grupo en redes sociales.

**Estado (2026-08-01)**: A la espera de datos de la página de Facebook — Pablo tiene que
consultar con Carlos quién es administrador de facebook.com/GIPISUNPSJB para poder crear
la app de Meta y generar el token. Mientras tanto ya se puede cargar novedades a mano
desde el panel admin (CRUD implementado). El modelo ya tiene `News.source` y la UI
muestra el badge de la red en las novedades harvesteadas.

**Instagram (pedirle también a Carlos)**: la misma app de Meta sirve para leer los posts
de instagram.com/gipis.unp **si la cuenta de Instagram está vinculada como cuenta
profesional a la página de Facebook**. Al hablar con Carlos, confirmar: (1) quién es
admin de la página de Facebook, (2) si la cuenta de Instagram está vinculada a esa
página y quién la administra. Con un solo token se harvestean las dos redes.

- **LinkedIn descartado como fuente**: la API de páginas de empresa (Community Management
  API) requiere una app aprobada por LinkedIn con proceso de revisión, y el scraping va
  contra sus términos de servicio. Los textos de Novedades que prometían "sincronización
  automática desde LinkedIn" se ajustaron; LinkedIn queda como link a la página del grupo.
- **Facebook es la alternativa viable**: el grupo tiene página (facebook.com/GIPISUNPSJB) y
  la Graph API permite a un administrador de la página leer sus propios posts
  (`/{page-id}/posts` con un Page Access Token de larga duración) sin pasar por App Review,
  usando una app propia en modo desarrollo. Requiere que un admin de la página genere el
  token. Los posts traen texto, fecha, imagen (`full_picture`) y link (`permalink_url`).

---

## 📈 Google Search Console — HECHO (2026-08-01)

**Configurado**: propiedad `https://gipis.unp.edu.ar` verificada (archivo
`google69166b95c779df06.html` servido por una ruta permanente — no borrar) y
sitemap enviado, con 19 páginas descubiertas. En el camino se corrigió que las
URLs generadas fueran https (ProxyFix en Flask + trustedIPs en Traefik).

---

## 📶 Monitoreo de uptime — HECHO (2026-08-01)

**Configurado**: monitor HTTP(s) de UptimeRobot sobre `https://gipis.unp.edu.ar`
cada 5 minutos, con alerta por email.

---

## 📄 Paginación de novedades — HECHO (2026-08-01)

**Implementado**: 9 novedades por página con pager (Anterior/Siguiente y números),
usando `.paginate()` de Flask-SQLAlchemy.

---

## 📊 ORCID Integration — HECHO (2026-07-31)

**Implementado**: Los miembros pueden cargar su ORCID iD en el perfil (validado con
checksum, se muestra en su página pública) e importar sus trabajos públicos desde
"Mi Producción" con pantalla de revisión (mismo patrón que SIGEVA). Cliente de la API
pública en `app/orcid.py` (sin dependencias nuevas, `urllib`). Los trabajos importados
quedan con `source='orcid'` y se pueden compartir a la página de Investigación.
