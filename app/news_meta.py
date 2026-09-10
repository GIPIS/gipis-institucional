"""
Metadatos de novedades: categorías fijas y formatos aceptados.

Las categorías se guardan en la base por clave (News.category) y se
muestran con su etiqueta; la versión en inglés se resuelve con _() en
los templates, así que las traducciones viven en app/i18n.py.
"""

NEWS_CATEGORIES = [
    ('cooperacion-academica', 'Cooperación académica'),
    ('cooperacion-cientifica', 'Cooperación científica'),
    ('vinculacion-transferencia', 'Vinculación y transferencia'),
    ('comunicacion-publica', 'Comunicación pública de la ciencia'),
]

CATEGORY_LABELS = dict(NEWS_CATEGORIES)


def category_label(key):
    """Etiqueta de una categoría; si la clave no es conocida (valores
    cargados antes de fijar las categorías) se muestra tal cual."""
    if not key:
        return None
    return CATEGORY_LABELS.get(key, key)


def is_valid_category(key):
    return key in CATEGORY_LABELS


NEWS_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

NEWS_ATTACHMENT_EXTENSIONS = {
    'pdf', 'doc', 'docx', 'ppt', 'pptx', 'xls', 'xlsx',
    'odt', 'odp', 'ods', 'zip',
}
