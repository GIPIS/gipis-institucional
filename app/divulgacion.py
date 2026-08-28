"""
Sección Divulgación: registro de temáticas y su estado.

El contenido de cada experiencia vive en su template
(app/templates/pages/divulgacion/<slug>.xhtml); acá solo se define qué
temáticas existen, en qué estado están y qué se muestra en la portada.

Publicar una experiencia nueva = agregar su template y cambiar su
'status' a 'available'. Los títulos y preguntas pasan por _() en los
templates, así que sus traducciones se agregan en app/i18n.py.

status: 'development' (tarjeta visible, sin enlace)
      | 'available'   (tarjeta con acceso "Explorar")
      | 'interactive' (disponible + experiencia interactiva)
"""

TOPICS = [
    {
        'slug': 'comunicaciones-acusticas',
        'icon': 'waves',
        'title': 'Comunicaciones acústicas subacuáticas',
        'question': '¿Cómo se comunican los equipos bajo el agua?',
        'status': 'available',
        # Demostrador físico: URL de la interfaz local que sirve el
        # microcontrolador (solo accesible en la red del demostrador).
        # Con None se muestran las instrucciones sin botón de acceso.
        'demo_url': None,
        # Cierre de la experiencia: próxima temática relacionada.
        'related': {
            'title': 'Posicionamiento acústico',
            'question': '¿Podemos utilizar el sonido para localizar un dispositivo bajo el agua?',
            'status': 'development',
        },
    },
    {
        'slug': 'comunicaciones-iot',
        'icon': 'wifi',
        'title': 'Comunicaciones inalámbricas e IoT',
        'question': '¿Cómo conectamos sensores y dispositivos a distancia?',
        'status': 'development',
    },
    {
        'slug': 'sensores-monitoreo',
        'icon': 'device_thermostat',
        'title': 'Sensores y monitoreo ambiental',
        'question': '¿Cómo medimos lo que ocurre en nuestro ambiente?',
        'status': 'development',
    },
    {
        'slug': 'tecnologias-oceano',
        'icon': 'water',
        'title': 'Tecnologías para observar el océano',
        'question': '¿Cómo podemos conocer lo que ocurre en el mar?',
        'status': 'development',
    },
    {
        'slug': 'observacion-tierra',
        'icon': 'satellite_alt',
        'title': 'Observación de la Tierra',
        'question': '¿Cómo podemos estudiar el territorio y el océano desde el espacio?',
        'status': 'development',
    },
    {
        'slug': 'procesamiento-senales',
        'icon': 'graphic_eq',
        'title': 'Procesamiento digital de señales',
        'question': '¿Cómo extraemos información útil de una señal?',
        'status': 'development',
    },
    {
        'slug': 'sistemas-embebidos',
        'icon': 'memory',
        'title': 'Sistemas embebidos',
        'question': '¿Qué hay detrás de un dispositivo electrónico inteligente?',
        'status': 'development',
    },
    {
        'slug': 'drones-imagenes',
        'icon': 'flight',
        'title': 'Drones y procesamiento de imágenes',
        'question': '¿Qué información podemos obtener observando desde el aire?',
        'status': 'development',
    },
    {
        'slug': 'ia-datos',
        'icon': 'psychology',
        'title': 'Inteligencia Artificial y datos',
        'question': '¿Cómo transformamos datos en información útil?',
        'status': 'development',
    },
]


def get_topic(slug):
    """Buscar una temática por slug; None si no existe."""
    for topic in TOPICS:
        if topic['slug'] == slug:
            return topic
    return None


def available_topics():
    """Temáticas con página propia (para sitemap y enlaces)."""
    return [t for t in TOPICS if t['status'] != 'development']
