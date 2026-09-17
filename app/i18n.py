"""
Traducción de la interfaz pública (ES → EN).

El español es el idioma canónico: los templates usan _('texto en español')
y acá se busca la versión en inglés. Si una cadena no está en el
diccionario, se muestra el español tal cual (fallback seguro), así que
agregar textos nuevos nunca rompe nada.

Los nombres de categorías y secciones que vienen de la base también
pasan por _(), por eso figuran acá ('Publicaciones', 'Investigadores', etc.).
"""

LANGUAGES = ('es', 'en')

TRANSLATIONS = {
    # --- Navegación / base ---
    'Inicio': 'Home',
    'Nuestro Equipo': 'Our Team',
    'Investigación': 'Research',
    'Cooperación': 'Cooperation',
    'Novedades': 'News',
    'Contacto': 'Contact',
    'Ingresar': 'Sign in',
    'Acceso miembros': 'Members sign in',
    'Boya oceanográfica del GIPIS fondeada en el mar':
        'GIPIS oceanographic buoy moored at sea',
    'Actividades de divulgación del GIPIS: charlas en aulas, visitas de escuelas, transmisiones y pósters científicos':
        'GIPIS outreach activities: classroom talks, school visits, live streams and scientific posters',
    'La ronda de café y el trabajo en el taller del GIPIS':
        'The coffee round and workshop time at GIPIS',
    'Armado de circuitos electrónicos en el laboratorio del GIPIS':
        'Building electronic circuits at the GIPIS lab',
    'Visitantes llegando a la Facultad de Ingeniería de la UNPSJB':
        'Visitors arriving at the UNPSJB Faculty of Engineering',
    'Fondeo de la boya oceanográfica del GIPIS':
        'Deployment of the GIPIS oceanographic buoy',
    'Fondeo de la boya del GIPIS junto a una embarcación de la Armada Argentina':
        'Deployment of the GIPIS buoy alongside an Argentine Navy boat',
    'Cambiar idioma': 'Change language',
    'Cambiar tema': 'Toggle theme',
    'Grupo': 'Team',
    'Mi Perfil': 'My Profile',
    'Institución': 'Institution',
    'Facultad de Ingeniería': 'Faculty of Engineering',
    'Grupo de Investigación en Procesamiento de la Información y Sensores':
        'Information Processing and Sensors Research Group',
    'Liderando la innovación en el procesamiento de señales y sistemas sensoriales desde la Patagonia para el mundo.':
        'Leading innovation in signal processing and sensor systems from Patagonia to the world.',
    'KM4 Ciudad Universitaria, Comodoro Rivadavia, Chubut':
        'KM4 University Campus, Comodoro Rivadavia, Chubut, Argentina',
    '© 2026 GIPIS | Facultad de Ingeniería | Universidad Nacional de la Patagonia San Juan Bosco':
        '© 2026 GIPIS | Faculty of Engineering | National University of Patagonia San Juan Bosco',

    # --- Home ---
    'GIPIS: Grupo de Investigación en Procesamiento de la Información y Sensores. Investigación de vanguardia en señales digitales, redes de sensores y telecomunicaciones. FI-UNPSJB, Comodoro Rivadavia.':
        'GIPIS: Information Processing and Sensors Research Group. Cutting-edge research in digital signals, sensor networks and telecommunications. FI-UNPSJB, Comodoro Rivadavia.',
    'Universidad Nacional de la Patagonia San Juan Bosco':
        'National University of Patagonia San Juan Bosco',
    'GIPIS: Procesamiento de la Información y Sensores':
        'GIPIS: Information Processing and Sensors',
    'Investigación de vanguardia para la transformación digital y el desarrollo tecnológico regional.':
        'Cutting-edge research for digital transformation and regional technological development.',
    'Explorar Proyectos': 'Explore Projects',
    'Sobre el Grupo': 'About the Group',
    'Fortaleciendo el Sistema Científico-Tecnológico':
        'Strengthening the Scientific and Technological System',
    'Este grupo busca fortalecer la vinculación entre el sistema científico-tecnológico y la estructura productiva en el ámbito de la informática y las telecomunicaciones para afrontar los nuevos desafíos que se proponen con la transformación digital.':
        'This group seeks to strengthen the links between the scientific-technological system and the productive sector in the fields of computer science and telecommunications, in order to meet the new challenges posed by digital transformation.',
    'Nuestras líneas de investigación se centran en el procesamiento digital de señales utilizando sistemas sensoriales desplegados en espacios inteligentes, redes eléctricas y entornos subacuáticos para percibir el estado del entorno y las entidades con las cuales se interactúa.':
        'Our research lines focus on digital signal processing using sensor systems deployed in smart spaces, power grids and underwater environments to perceive the state of the surroundings and the entities they interact with.',
    'Análisis de Datos': 'Data Analysis',
    'Telecomunicaciones': 'Telecommunications',
    'Sensores': 'Sensors',
    'Facultad de Ingeniería UNPSJB': 'Faculty of Engineering, UNPSJB',
    'Novedades Recientes': 'Recent News',
    'Ver todas las noticias': 'View all news',
    'Procesamiento de la Información y Sensores':
        'Information Processing and Sensors',
    'Investigación aplicada en electrónica, sensores y sistemas de información desde la Facultad de Ingeniería de la UNPSJB.':
        'Applied research in electronics, sensors and information systems at the UNPSJB Faculty of Engineering.',
    'Conocé el grupo': 'Meet the group',
    'Nuestra Misión': 'Our Mission',
    'Últimas Novedades': 'Latest News',
    'Ver todas': 'View all',
    'Leer más': 'Read more',
    'Conocé más': 'Learn more',
    'Líneas de Investigación': 'Research Lines',
    'Ver equipo': 'View team',

    # --- Equipo ---
    'Un equipo multidisciplinario de investigadores, docentes y becarios.':
        'A multidisciplinary team of researchers, faculty and fellows.',
    'Conocé al equipo multidisciplinario de investigadores, docentes y becarios del GIPIS. Facultad de Ingeniería, UNPSJB.':
        'Meet the multidisciplinary team of researchers, faculty members and fellows at GIPIS. Faculty of Engineering, UNPSJB.',
    'Contamos con un equipo multidisciplinario de investigadores, docentes y becarios comprometidos con la excelencia académica y la innovación tecnológica en el procesamiento de señales y sistemas sensoriales.':
        'We have a multidisciplinary team of researchers, faculty members and fellows committed to academic excellence and technological innovation in signal processing and sensor systems.',
    'Dirección e Investigación Senior': 'Leadership and Senior Research',
    'Director': 'Director',
    'Datos próximamente disponibles.': 'Information coming soon.',
    'Equipo': 'Team',
    'Miembro del GIPIS, Grupo de Investigación en Procesamiento de la Información y Sensores, UNPSJB.':
        'Member of GIPIS, the Information Processing and Sensors Research Group, UNPSJB.',
    'Ver perfil': 'View profile',
    'Miembro del grupo': 'Group member',
    # Categorías (vienen de la base)
    'Investigadores': 'Researchers',
    'Investigadores Formados': 'Senior Researchers',
    'Investigadores en Formación': 'Researchers in Training',
    'Becarios': 'Fellows',
    'Becarios y Tesistas': 'Fellows and Thesis Students',
    'Colaboradores': 'Collaborators',
    'Personal de Apoyo': 'Support Staff',

    # --- Perfil de miembro ---
    'Publicaciones': 'Publications',
    'Proyectos': 'Projects',
    'Tesis y becarios dirigidos': 'Supervised theses and fellows',
    'Descargar contacto': 'Download contact',
    'Volver al equipo': 'Back to team',
    'Email personal': 'Personal email',
    'Email institucional': 'Institutional email',
    'Teléfono': 'Phone',

    # --- Investigación ---
    'Desarrollamos investigación aplicada en múltiples áreas del procesamiento de señales y sistemas sensoriales.':
        'We carry out applied research across multiple areas of signal processing and sensor systems.',
    'Ver más': 'See more',
    'Ver todos': 'View all',
    'Volver a investigación': 'Back to research',
    # Secciones (vienen de la base)
    'Proyectos de Investigación': 'Research Projects',
    'Transferencias': 'Technology Transfer',
    'Reportes internos': 'Internal Reports',
    'Tesis de maestría': "Master's Theses",
    'Tesis doctorales': 'Doctoral Theses',

    # --- Investigación / Líneas ---
    'Líneas de investigación del GIPIS: procesamiento digital de señales, redes de sensores, telecomunicaciones, sistemas sensoriales y espacios inteligentes.':
        'GIPIS research lines: digital signal processing, sensor networks, telecommunications, sensory systems, and smart environments.',
    'Nuestras actividades de investigación se centran en el desarrollo de soluciones innovadoras mediante el procesamiento de información y el uso avanzado de sensores en diversos entornos.':
        'Our research activities focus on developing innovative solutions through information processing and the advanced use of sensors in a variety of environments.',
    'Saber más': 'Learn more',
    'Procesamiento Digital de Señales': 'Digital Signal Processing',
    'Desarrollo de algoritmos avanzados para el análisis y mejora de señales en diversos contextos, con aplicaciones en biometría y reconocimiento de patrones.':
        'Development of advanced algorithms for signal analysis and enhancement in diverse contexts, with applications in biometrics and pattern recognition.',
    'Redes PLC y Comunicaciones': 'PLC Networks and Communications',
    'Investigación en Power Line Communications (PLC) para la optimización de la transmisión de datos sobre infraestructuras eléctricas existentes.':
        'Research on Power Line Communications (PLC) for optimizing data transmission over existing electrical infrastructure.',
    'Espacios Inteligentes': 'Smart Environments',
    'Implementación de sistemas de sensores interactivos y eficientes en contextos urbanos e inteligentes.':
        'Implementation of interactive, efficient sensor systems in urban and smart contexts.',
    'Sensores Subacuáticos': 'Underwater Sensors',
    'Despliegue y procesamiento de redes de sensores para el monitoreo de entornos marinos y campañas oceanográficas en la Patagonia.':
        'Deployment and processing of sensor networks for monitoring marine environments and oceanographic campaigns in Patagonia.',
    'Sistemas Embebidos y FPGA': 'Embedded Systems and FPGA',
    'Diseño de hardware dedicado para el procesamiento de alta velocidad mediante dispositivos programables para aplicaciones críticas.':
        'Design of dedicated hardware for high-speed processing using programmable devices for critical applications.',
    'Optimización y monitoreo de redes eléctricas inteligentes para mejorar la eficiencia energética y la integración de renovables.':
        'Optimization and monitoring of smart power grids to improve energy efficiency and the integration of renewables.',
    'I+D+i Activo': 'Active R&D&i',
    'Proyectos Activos': 'Active Projects',
    'Los proyectos activos se mostrarán próximamente.': 'Active projects will be published soon.',
    'Línea de investigación del GIPIS.': 'GIPIS research line.',
    'Descripción': 'Description',
    'Esta línea de investigación se enfoca en el desarrollo de soluciones innovadoras mediante técnicas avanzadas de procesamiento de señales y sistemas sensoriales. Nuestro enfoque multidisciplinario permite abordar problemas complejos en diversos contextos.':
        'This research line focuses on developing innovative solutions through advanced signal processing techniques and sensory systems. Our multidisciplinary approach enables us to tackle complex problems in diverse contexts.',
    'Objetivos': 'Objectives',
    'Desarrollar algoritmos y técnicas innovadoras para el procesamiento de señales en tiempo real.':
        'Develop innovative algorithms and techniques for real-time signal processing.',
    'Implementar prototipos funcionales para validar los resultados teóricos.':
        'Implement functional prototypes to validate theoretical results.',
    'Formar recursos humanos especializados en el área.':
        'Train specialized human resources in the field.',
    'Transferir conocimientos y tecnologías al sector productivo.':
        'Transfer knowledge and technologies to the productive sector.',
    'Metodologías': 'Methodologies',
    'Modelado matemático y simulación': 'Mathematical modeling and simulation',
    'Prototipado rápido': 'Rapid prototyping',
    'Validación experimental': 'Experimental validation',
    'Transferencia tecnológica': 'Technology transfer',
    'Tecnologías': 'Technologies',
    'Aplicaciones': 'Applications',
    'Industria': 'Industry',
    'Automatización y control': 'Automation and control',
    'Oceanografía': 'Oceanography',
    'Monitoreo marino': 'Marine monitoring',
    'Energía': 'Energy',
    'Redes inteligentes': 'Smart grids',
    'Volver a Líneas de Investigación': 'Back to Research Lines',

    # --- Divulgación ---
    'Divulgación': 'Outreach',
    'Ciencia y tecnología para explorar': 'Science and technology to explore',
    'Divulgación GIPIS: ciencia y tecnología para explorar. Experiencias y contenidos didácticos sobre las áreas de trabajo del grupo, para estudiantes y la comunidad.':
        'GIPIS Outreach: science and technology to explore. Experiences and educational content about the group’s areas of work, for students and the community.',
    'Un espacio del GIPIS para acercar la ingeniería, la ciencia y la tecnología a estudiantes y a la comunidad.':
        'A GIPIS space to bring engineering, science and technology closer to students and the community.',
    'A través de experiencias, demostraciones y contenidos interactivos buscamos mostrar de manera sencilla cómo funcionan algunas de las tecnologías con las que trabajamos y para qué pueden utilizarse.':
        'Through experiences, demonstrations and interactive content we aim to show in a simple way how some of the technologies we work with function and what they can be used for.',
    'Explorar': 'Explore',
    'En desarrollo': 'In development',
    'Próxima experiencia': 'Next experience',
    'Quiero saber más': 'I want to know more',
    'Tecnología, ciencia e ingeniería desde la Patagonia':
        'Technology, science and engineering from Patagonia',
    'Conocé GIPIS': 'Meet GIPIS',
    'Conocé nuestros proyectos': 'Explore our projects',
    'Volver a Divulgación': 'Back to Outreach',
    # Temáticas (títulos y preguntas de las tarjetas)
    'Comunicaciones acústicas subacuáticas': 'Underwater acoustic communications',
    '¿Cómo se comunican los equipos bajo el agua?': 'How do devices communicate underwater?',
    'Comunicaciones inalámbricas e IoT': 'Wireless communications and IoT',
    '¿Cómo conectamos sensores y dispositivos a distancia?':
        'How do we connect sensors and devices remotely?',
    'Sensores y monitoreo ambiental': 'Sensors and environmental monitoring',
    '¿Cómo medimos lo que ocurre en nuestro ambiente?':
        'How do we measure what happens in our environment?',
    'Tecnologías para observar el océano': 'Technologies for observing the ocean',
    '¿Cómo podemos conocer lo que ocurre en el mar?':
        'How can we know what is happening in the sea?',
    'Observación de la Tierra': 'Earth observation',
    '¿Cómo podemos estudiar el territorio y el océano desde el espacio?':
        'How can we study the land and the ocean from space?',
    'Procesamiento digital de señales': 'Digital signal processing',
    '¿Cómo extraemos información útil de una señal?':
        'How do we extract useful information from a signal?',
    'Sistemas embebidos': 'Embedded systems',
    '¿Qué hay detrás de un dispositivo electrónico inteligente?':
        'What is behind a smart electronic device?',
    'Drones y procesamiento de imágenes': 'Drones and image processing',
    '¿Qué información podemos obtener observando desde el aire?':
        'What information can we obtain by observing from the air?',
    'Inteligencia Artificial y datos': 'Artificial Intelligence and data',
    '¿Cómo transformamos datos en información útil?':
        'How do we turn data into useful information?',
    'Posicionamiento acústico': 'Acoustic positioning',
    '¿Podemos utilizar el sonido para localizar un dispositivo bajo el agua?':
        'Can we use sound to locate a device underwater?',
    # Experiencia: comunicaciones acústicas
    'Comunicaciones acústicas': 'Acoustic communications',
    '¿Cómo se comunican los equipos bajo el agua? Descubrí cómo transformamos un mensaje digital en una señal acústica, la transmitimos y recuperamos la información. Divulgación GIPIS.':
        'How do devices communicate underwater? Discover how we turn a digital message into an acoustic signal, transmit it and recover the information. GIPIS Outreach.',
    'En nuestra vida cotidiana utilizamos Wi-Fi, Bluetooth, telefonía celular y otras tecnologías inalámbricas para comunicarnos. Pero ¿qué ocurre cuando queremos comunicarnos debajo del agua?':
        'In everyday life we use Wi-Fi, Bluetooth, cell phones and other wireless technologies to communicate. But what happens when we want to communicate underwater?',
    'En el medio acuático, y especialmente en el agua de mar, las ondas electromagnéticas utilizadas habitualmente para las comunicaciones inalámbricas se atenúan rápidamente.':
        'In aquatic environments, and especially in seawater, the electromagnetic waves normally used for wireless communications are quickly attenuated.',
    'Una de las principales alternativas para transmitir información a distancia en ambientes subacuáticos es utilizar ondas acústicas.':
        'One of the main alternatives for transmitting information over distance in underwater environments is to use acoustic waves.',
    'En esta experiencia vas a descubrir cómo podemos transformar un mensaje digital en una señal acústica, transmitirlo y recuperar nuevamente la información.':
        'In this experience you will discover how we can turn a digital message into an acoustic signal, transmit it and recover the information again.',
    '¿Por qué no usamos Wi-Fi bajo el agua?': 'Why don’t we use Wi-Fi underwater?',
    'Las tecnologías inalámbricas que utilizamos habitualmente emplean ondas electromagnéticas. En el agua, especialmente en agua de mar, estas señales se atenúan fuertemente y su alcance se reduce.':
        'The wireless technologies we normally use rely on electromagnetic waves. In water, especially seawater, these signals are strongly attenuated and their range is reduced.',
    'El sonido puede propagarse a distancias considerablemente mayores. Por esta razón, las ondas acústicas constituyen una de las principales alternativas para establecer comunicaciones subacuáticas.':
        'Sound can travel considerably longer distances. For this reason, acoustic waves are one of the main alternatives for underwater communications.',
    'En el aire': 'In the air',
    'Bajo el agua': 'Underwater',
    'Ondas electromagnéticas': 'Electromagnetic waves',
    'Wi-Fi / Bluetooth / LoRa': 'Wi-Fi / Bluetooth / LoRa',
    'Antena': 'Antenna',
    'Información digital': 'Digital information',
    'Ondas acústicas': 'Acoustic waves',
    'Comunicación acústica': 'Acoustic communication',
    'Transductor acústico': 'Acoustic transducer',
    'Información transportada mediante sonido': 'Information carried by sound',
    '¿Qué es una onda acústica?': 'What is an acoustic wave?',
    'El sonido es una onda mecánica y necesita un medio material para propagarse, como el aire o el agua.':
        'Sound is a mechanical wave and needs a material medium to propagate, such as air or water.',
    'En el agua de mar, el sonido se propaga aproximadamente a 1500 metros por segundo, aunque su velocidad depende de factores como la temperatura, la salinidad y la presión.':
        'In seawater, sound travels at roughly 1500 meters per second, although its speed depends on factors such as temperature, salinity and pressure.',
    'Un transmisor genera una onda acústica que se propaga por el agua hasta un receptor':
        'A transmitter generates an acoustic wave that propagates through the water to a receiver',
    'El transmisor genera una onda acústica que se propaga por el agua hasta el receptor, a ~1500 m/s.':
        'The transmitter generates an acoustic wave that propagates through the water to the receiver, at ~1500 m/s.',
    'AGUA': 'WATER',
    'Esquema del demostrador: el mensaje se codifica, se transmite como sonido a través del agua y se decodifica en el receptor':
        'Demonstrator diagram: the message is encoded, transmitted as sound through the water and decoded at the receiver',
    'El viaje de la información en el demostrador: el mensaje se codifica, se transmite como sonido a través del agua y se decodifica en el receptor.':
        'The information’s journey through the demonstrator: the message is encoded, transmitted as sound through the water and decoded at the receiver.',
    'Algunas magnitudes que caracterizan a una onda acústica y a su propagación en el agua:':
        'Some quantities that characterize an acoustic wave and its propagation in water:',
    'Frecuencia': 'Frequency',
    'cantidad de oscilaciones por segundo, medida en hertz (Hz).':
        'number of oscillations per second, measured in hertz (Hz).',
    'Longitud de onda': 'Wavelength',
    'distancia entre dos crestas consecutivas de la onda.':
        'distance between two consecutive crests of the wave.',
    'Velocidad de propagación': 'Propagation speed',
    'en el mar, cercana a 1500 m/s; varía con la temperatura, la salinidad y la presión.':
        'in the sea, close to 1500 m/s; it varies with temperature, salinity and pressure.',
    'Atenuación': 'Attenuation',
    'pérdida de energía de la señal a medida que se propaga.':
        'loss of signal energy as it propagates.',
    'Ruido': 'Noise',
    'sonidos del ambiente (olas, embarcaciones, fauna marina) que se mezclan con la señal.':
        'sounds from the environment (waves, vessels, marine life) that mix with the signal.',
    'Reflexiones': 'Reflections',
    'rebotes de la señal en la superficie y el fondo del mar.':
        'the signal bouncing off the sea surface and the seabed.',
    'Propagación multicamino': 'Multipath propagation',
    'la señal llega al receptor por varios caminos a la vez, con distintos retardos.':
        'the signal reaches the receiver through several paths at once, with different delays.',
    '¿Cómo convertimos una palabra en sonido?': 'How do we turn a word into sound?',
    'Para transmitir información, primero convertimos el mensaje en datos digitales.':
        'To transmit information, we first convert the message into digital data.',
    'Esos datos pueden utilizarse para modificar una señal mediante un proceso denominado modulación.':
        'That data can be used to modify a signal through a process called modulation.',
    'La señal resultante se transmite a través del agua. En el receptor se realiza el proceso inverso para recuperar la información enviada.':
        'The resulting signal is transmitted through the water. At the receiver, the inverse process recovers the information that was sent.',
    'Mensaje': 'Message',
    'Datos': 'Data',
    'Modulación': 'Modulation',
    'Señal acústica': 'Acoustic signal',
    'Agua': 'Water',
    'Recepción': 'Reception',
    'Decodificación': 'Decoding',
    'La palabra se convierte en bits y los bits modulan una onda acústica que transporta el mensaje':
        'The word is converted into bits and the bits modulate an acoustic wave that carries the message',
    'El ejemplo con la letra H (01001000): cada bit modifica la frecuencia de la onda — eso es la modulación, y así la información viaja en el sonido.':
        'The example with the letter H (01001000): each bit changes the frequency of the wave — that is modulation, and that is how information travels in sound.',
    'Del concepto a una experiencia real': 'From concept to a real experience',
    'En GIPIS desarrollamos un demostrador que permite observar de manera sencilla cómo funciona una comunicación acústica.':
        'At GIPIS we developed a demonstrator that lets you easily observe how an acoustic communication works.',
    'Un microcontrolador recibe una palabra ingresada desde una interfaz web, la codifica y genera la señal correspondiente para realizar la transmisión acústica. En el otro extremo, el sistema receptor procesa la señal para recuperar la información transmitida.':
        'A microcontroller receives a word entered through a web interface, encodes it and generates the corresponding signal for the acoustic transmission. At the other end, the receiving system processes the signal to recover the transmitted information.',
    'Interfaz web': 'Web interface',
    'Micro-': 'Micro-',
    'controlador': 'controller',
    'Microcontrolador': 'Microcontroller',
    'Transmisor': 'Transmitter',
    'Receptor': 'Receiver',
    'En una misma experiencia intervienen electrónica, programación, sistemas digitales, telecomunicaciones y procesamiento de señales.':
        'A single experience brings together electronics, programming, digital systems, telecommunications and signal processing.',
    '¿Estás en una muestra? Probá nuestro demostrador':
        'Are you at an exhibit? Try our demonstrator',
    'Si estás participando de una muestra o actividad de GIPIS y tenés el demostrador frente a vos, podés probarlo.':
        'If you are taking part in a GIPIS exhibit or activity and the demonstrator is in front of you, you can try it.',
    'Escribí una palabra, transmitila y observá cómo la información se transforma en una señal acústica y llega al receptor.':
        'Type a word, transmit it and watch how the information turns into an acoustic signal and reaches the receiver.',
    '¿Cómo participar?': 'How to take part?',
    'Conectate a la red indicada en el demostrador.':
        'Connect to the network indicated on the demonstrator.',
    'Accedé a la interfaz mediante el código QR.': 'Access the interface via the QR code.',
    'Escribí una palabra.': 'Type a word.',
    'Presioná «Transmitir».': 'Press “Transmit”.',
    'Observá qué sucede durante la transmisión y qué información llega al receptor.':
        'Watch what happens during the transmission and what information reaches the receiver.',
    'Acceder al demostrador': 'Access the demonstrator',
    'Esta función requiere estar presencialmente junto al demostrador y conectado a su red local.':
        'This feature requires being physically next to the demonstrator and connected to its local network.',
    '¿Para qué sirven las comunicaciones acústicas subacuáticas?':
        'What are underwater acoustic communications used for?',
    'Vehículos submarinos': 'Underwater vehicles',
    'Permiten intercambiar información con robots y vehículos utilizados para explorar ambientes subacuáticos.':
        'They allow exchanging information with robots and vehicles used to explore underwater environments.',
    'Permiten comunicar instrumentos y sensores utilizados para estudiar el océano.':
        'They allow communicating with instruments and sensors used to study the ocean.',
    'Posicionamiento y navegación': 'Positioning and navigation',
    'Las señales satelitales de posicionamiento no están disponibles normalmente bajo el agua. Las señales acústicas pueden utilizarse para desarrollar sistemas de localización y navegación subacuática.':
        'Satellite positioning signals are normally unavailable underwater. Acoustic signals can be used to develop underwater localization and navigation systems.',
    'Monitoreo ambiental': 'Environmental monitoring',
    'Permiten obtener y transmitir información proveniente de sensores instalados en ambientes acuáticos.':
        'They allow obtaining and transmitting information from sensors deployed in aquatic environments.',
    'Infraestructura submarina': 'Underwater infrastructure',
    'Pueden utilizarse para comunicación y supervisión de dispositivos e instalaciones ubicados bajo el agua.':
        'They can be used to communicate with and supervise devices and installations located underwater.',
    'Detrás de una comunicación acústica subacuática hay una cadena de conceptos que podés seguir profundizando:':
        'Behind an underwater acoustic communication there is a chain of concepts you can keep exploring:',
    'Propagación': 'Propagation',
    'Multicamino': 'Multipath',
    'Codificación': 'Coding',
    'Detección': 'Detection',
    'Procesamiento digital': 'Digital processing',
    'Este material también puede servir de apoyo para estudiantes universitarios de ingeniería.':
        'This material can also support university engineering students.',
    '¿Sabías que el GPS tampoco funciona normalmente debajo del agua?':
        'Did you know that GPS doesn’t normally work underwater either?',
    'Las señales provenientes de los satélites de posicionamiento no penetran suficientemente en el agua como para permitir el funcionamiento convencional de un receptor sumergido.':
        'Signals from positioning satellites do not penetrate water deeply enough for a submerged receiver to work conventionally.',
    'Entonces aparece otro desafío:': 'So another challenge appears:',

    # Experiencia acústica: robustez con DSSS
    '¿Cómo hacemos la comunicación más robusta?':
        'How do we make the communication more robust?',
    'Para aumentar la robustez frente al ruido y a las perturbaciones del canal utilizamos espectro ensanchado por secuencia directa (DSSS). Cada dato se representa mediante una secuencia conocida de elementos más cortos, llamados chips.':
        'To increase robustness against noise and channel disturbances we use direct-sequence spread spectrum (DSSS). Each data symbol is represented by a known sequence of shorter elements, called chips.',
    'El receptor conoce esa misma secuencia y utiliza un correlador para buscarla dentro de la señal recibida.':
        'The receiver knows that same sequence and uses a correlator to search for it within the received signal.',
    'Codificación DSSS': 'DSSS coding',
    'Modulador': 'Modulator',
    'Canal acústico': 'Acoustic channel',
    'Demodulador': 'Demodulator',
    'Correlador': 'Correlator',
    'El receptor busca una secuencia conocida': 'The receiver searches for a known sequence',
    'La ventana representa el correlador desplazándose sobre la señal recibida.':
        'The window represents the correlator sliding over the received signal.',
    'secuencia de referencia': 'reference sequence',
    'Ver correlación': 'Run correlation',
    'Pausar': 'Pause',
    'Repetir': 'Replay',
    'Desplazamiento del correlador': 'Correlator shift',
    'Resultado de la correlación': 'Correlation result',
    'Cuando la referencia se alinea con la secuencia recibida aparece un pico.':
        'When the reference lines up with the received sequence, a peak appears.',
    'Correlación en la posición actual:': 'Correlation at the current position:',
    'correlación': 'correlation',
    'desplazamiento': 'shift',
    'Al combinar la información distribuida en varios chips, la señal deseada se refuerza en el correlador mientras que el ruido no correlacionado tiende a combinarse de forma menos coherente. Esta es una de las razones por las que DSSS puede mejorar la detección en un canal acústico afectado por ruido e interferencias.':
        'By combining the information spread across several chips, the desired signal is reinforced in the correlator, while uncorrelated noise tends to combine less coherently. This is one of the reasons why DSSS can improve detection in an acoustic channel affected by noise and interference.',
    'El diseño de secuencias es una parte importante de los sistemas de espectro ensanchado. Se buscan secuencias con buenas propiedades de autocorrelación, para reconocer con claridad cuándo una señal está correctamente alineada, y de correlación cruzada, para poder distinguir distintas secuencias entre sí. Algunas son:':
        'Sequence design is an important part of spread-spectrum systems. Sequences are sought with good autocorrelation properties, to clearly recognize when a signal is correctly aligned, and good cross-correlation properties, to tell different sequences apart. Some of them are:',
    'son secuencias binarias cortas caracterizadas por tener lóbulos laterales de autocorrelación muy bajos. Esto genera un pico de correlación claramente distinguible y las hace especialmente útiles para detección, sincronización y estimación del instante de llegada de una señal. Sólo existen para determinadas longitudes cortas.':
        'short binary sequences characterized by very low autocorrelation sidelobes. This produces a clearly distinguishable correlation peak and makes them especially useful for detection, synchronization and estimating the arrival time of a signal. They only exist for certain short lengths.',
    'Pares de secuencias complementarias (Golay)': 'Complementary sequence pairs (Golay)',
    'están formados por dos secuencias cuyas autocorrelaciones aperiódicas se complementan. Al sumar los resultados de correlación de ambas, sus lóbulos laterales se cancelan idealmente y queda un único pico central. Son particularmente interesantes en sistemas de medición, estimación de canal y detección.':
        'formed by two sequences whose aperiodic autocorrelations complement each other. When the correlation results of both are added, their sidelobes ideally cancel out, leaving a single central peak. They are particularly interesting for measurement systems, channel estimation and detection.',
    'son secuencias complejas de amplitud constante que presentan autocorrelación periódica ideal. Diferentes desplazamientos cíclicos pueden conservar muy buenas propiedades de separación, lo que permite utilizarlas para sincronización, identificación y acceso de múltiples usuarios. Además, su envolvente constante resulta atractiva para sistemas de transmisión.':
        'complex constant-amplitude sequences with ideal periodic autocorrelation. Different cyclic shifts can preserve very good separation properties, which allows using them for synchronization, identification and multi-user access. In addition, their constant envelope is attractive for transmission systems.',
    'constituyen familias de secuencias binarias diseñadas para presentar valores reducidos y controlados de correlación cruzada. Esto permite asignar distintas secuencias a diferentes transmisores o señales y luego distinguirlas en el receptor. Son de interés en sistemas de espectro ensanchado y acceso múltiple.':
        'families of binary sequences designed to exhibit low, controlled cross-correlation values. This allows assigning different sequences to different transmitters or signals and then telling them apart at the receiver. They are of interest in spread-spectrum and multiple-access systems.',
    'son familias extensas de secuencias binarias que ofrecen un buen compromiso entre cantidad de códigos disponibles y propiedades de correlación cruzada. Pueden generarse de manera eficiente mediante registros de desplazamiento y permiten identificar numerosos usuarios utilizando secuencias diferentes. Por este motivo han sido ampliamente utilizadas en sistemas de espectro ensanchado.':
        'large families of binary sequences that offer a good trade-off between the number of available codes and cross-correlation properties. They can be generated efficiently with shift registers and allow identifying many users through different sequences. For this reason they have been widely used in spread-spectrum systems.',
    'Secuencias de máxima longitud (m-sequences)': 'Maximum length sequences (m-sequences)',
    'son secuencias pseudoaleatorias binarias generadas mediante registros de desplazamiento con realimentación lineal. Poseen una autocorrelación periódica muy favorable y pueden generarse con circuitos o algoritmos relativamente simples. Además, sirven como base para construir otras familias de secuencias, como Gold y Kasami.':
        'binary pseudo-random sequences generated with linear-feedback shift registers. They have very favorable periodic autocorrelation and can be generated with relatively simple circuits or algorithms. They also serve as the basis for building other sequence families, such as Gold and Kasami.',

    # Experiencia: posicionamiento acústico
    'Posicionamiento acústico subacuático': 'Underwater acoustic positioning',
    '¿Cómo sabemos dónde está un equipo debajo del agua?': 'How do we know where a device is underwater?',
    '¿Cómo enviamos información bajo el agua?': 'How do we send information underwater?',
    '¿Cómo sabemos dónde está un equipo debajo del agua? Descubrí cómo el sonido permite medir distancias y estimar la posición de dispositivos sumergidos. Divulgación GIPIS.':
        'How do we know where a device is underwater? Discover how sound lets us measure distances and estimate the position of submerged devices. GIPIS Outreach.',
    'En superficie podemos utilizar sistemas de posicionamiento satelital como GPS para conocer nuestra ubicación. Pero ¿qué ocurre cuando un sensor, un instrumento o un robot se sumerge?':
        'At the surface we can use satellite positioning systems such as GPS to know our location. But what happens when a sensor, an instrument or a robot goes underwater?',
    'Las señales utilizadas por los sistemas satelitales de posicionamiento no penetran suficientemente en el agua para permitir el funcionamiento convencional de un receptor sumergido.':
        'The signals used by satellite positioning systems do not penetrate far enough into the water to allow a submerged receiver to work normally.',
    '¿Cómo podemos localizar un dispositivo debajo del agua?': 'How can we locate a device underwater?',
    'Una de las principales alternativas consiste en utilizar señales acústicas.':
        'One of the main alternatives is to use acoustic signals.',
    '¿Por qué no podemos usar GPS bajo el agua?': 'Why can’t we use GPS underwater?',
    'Los sistemas de posicionamiento satelital utilizan señales electromagnéticas transmitidas desde satélites.':
        'Satellite positioning systems use electromagnetic signals transmitted from satellites.',
    'Estas señales se atenúan rápidamente al ingresar al agua, especialmente en agua de mar. Por esta razón, un receptor sumergido normalmente no puede utilizarlas directamente para determinar su posición.':
        'These signals are quickly attenuated when they enter the water, especially seawater. For this reason, a submerged receiver normally cannot use them directly to determine its position.',
    'Posición': 'Position',
    'Si no podemos recibir las señales de los satélites, ¿qué podemos utilizar?':
        'If we cannot receive the satellite signals, what can we use?',
    'Sonido': 'Sound',
    'El sonido se propaga muy bien en el agua.': 'Sound travels very well through water.',
    '¿Por qué podemos utilizar sonido?': 'Why can we use sound?',
    'A diferencia de las señales electromagnéticas utilizadas por GPS, las ondas acústicas pueden propagarse a distancias útiles debajo del agua.':
        'Unlike the electromagnetic signals used by GPS, acoustic waves can travel useful distances underwater.',
    'Esta característica hace que el sonido sea una herramienta especialmente interesante para comunicación, detección y posicionamiento subacuático.':
        'This makes sound an especially interesting tool for underwater communication, detection and positioning.',
    '¿Querés saber cómo enviamos información utilizando sonido?': 'Want to know how we send information using sound?',
    '¿Qué tan rápido viaja el sonido?': 'How fast does sound travel?',
    'El sonido no se propaga a la misma velocidad en todos los medios. Veamos cuánto recorre en un segundo en el aire y en el agua de mar.':
        'Sound does not travel at the same speed in every medium. Let’s see how far it goes in one second through air and through seawater.',
    'Un segundo de viaje': 'One second of travel',
    'Ver 1 segundo': 'Play 1 second',
    'Aire': 'Air',
    'Agua de mar': 'Seawater',
    'La animación reproduce un segundo en cámara lenta. Ambas señales parten al mismo tiempo.':
        'The animation plays one second in slow motion. Both signals start at the same time.',
    'En el agua de mar, el sonido se propaga aproximadamente 4,4 veces más rápido que en el aire.':
        'In seawater, sound travels roughly 4.4 times faster than in air.',
    '¿La velocidad del sonido en el mar es siempre la misma?': 'Is the speed of sound in the sea always the same?',
    'No. 1500 m/s es un valor aproximado que resulta muy útil para comprender cómo funciona el posicionamiento acústico.':
        'No. 1500 m/s is an approximate value that is very useful for understanding how acoustic positioning works.',
    'En el océano, la velocidad del sonido depende principalmente de la temperatura, la salinidad y la presión, esta última relacionada con la profundidad.':
        'In the ocean, the speed of sound depends mainly on temperature, salinity and pressure, the latter being related to depth.',
    'Temperatura': 'Temperature',
    'Salinidad': 'Salinity',
    'Profundidad / presión': 'Depth / pressure',
    'En sistemas reales, conocer con mayor precisión la velocidad del sonido permite mejorar la estimación de las distancias y, por lo tanto, de la posición.':
        'In real systems, knowing the speed of sound more precisely improves the distance estimates and, therefore, the position.',
    'Quiero saber más: perfiles de velocidad del sonido': 'I want to know more: sound speed profiles',
    'La velocidad del sonido aumenta con la temperatura, con la salinidad y con la presión. Como estas magnitudes cambian con la profundidad, la velocidad también lo hace: a esa variación se la llama perfil de velocidad del sonido.':
        'The speed of sound increases with temperature, salinity and pressure. Since these quantities change with depth, so does the speed: that variation is called the sound speed profile.',
    'Perfil típico: la velocidad disminuye con la profundidad en la termoclina y luego aumenta por la presión':
        'Typical profile: speed decreases with depth through the thermocline and then increases due to pressure',
    'velocidad': 'speed',
    'profundidad': 'depth',
    'superficie': 'surface',
    'termoclina': 'thermocline',
    'mínimo': 'minimum',
    'presión': 'pressure',
    'Cerca de la superficie, el agua es más cálida y el sonido viaja más rápido.':
        'Near the surface the water is warmer and sound travels faster.',
    'En la termoclina, la temperatura baja rápidamente y la velocidad disminuye.':
        'In the thermocline, temperature drops quickly and the speed decreases.',
    'A mayor profundidad, el aumento de la presión vuelve a incrementar la velocidad.':
        'Deeper down, the increase in pressure raises the speed again.',
    'Estas variaciones curvan las trayectorias del sonido. Los sistemas de posicionamiento de precisión miden el perfil de velocidad para corregir sus estimaciones.':
        'These variations bend the sound paths. Precision positioning systems measure the speed profile to correct their estimates.',
    '¿Por qué el sonido es atractivo para posicionarnos?': 'Why is sound attractive for positioning?',
    'Las ondas acústicas pueden propagarse a distancias útiles debajo del agua. Además, conocemos aproximadamente su velocidad y podemos medir cuánto tarda una señal en viajar entre dos puntos.':
        'Acoustic waves can travel useful distances underwater. In addition, we know their speed approximately and we can measure how long a signal takes to travel between two points.',
    'Esto nos permite utilizar el tiempo de propagación para obtener información sobre la distancia recorrida.':
        'This lets us use the propagation time to obtain information about the distance travelled.',
    'Señal': 'Signal',
    'Tiempo': 'Time',
    'Distancia': 'Distance',
    'Si medimos cuánto tarda el sonido, podemos estimar cuánto recorrió.':
        'If we measure how long the sound takes, we can estimate how far it travelled.',
    '¿Sabías que el sonido es mucho más lento?': 'Did you know sound is much slower?',
    'Onda electromagnética': 'Electromagnetic wave',
    'Sonido en agua de mar': 'Sound in seawater',
    'El sonido es aproximadamente 200.000 veces más lento. Para posicionamiento esta diferencia es una ventaja: los tiempos de propagación acústica son mucho mayores y resultan más fáciles de medir. Por ejemplo, una señal acústica tarda unos 67 milisegundos en recorrer 100 metros de agua.':
        'Sound is roughly 200,000 times slower. For positioning this difference is an advantage: acoustic propagation times are much longer and easier to measure. For example, an acoustic signal takes about 67 milliseconds to travel 100 metres through water.',
    '¿Podemos medir una distancia utilizando sonido?': 'Can we measure a distance using sound?',
    'Si conocemos aproximadamente la velocidad con la que se propaga el sonido y medimos cuánto tarda una señal en viajar entre dos puntos, podemos estimar la distancia recorrida.':
        'If we know approximately how fast sound travels and we measure how long a signal takes to go between two points, we can estimate the distance travelled.',
    'Transmisión': 'Transmission',
    'Medimos el tiempo': 'We measure the time',
    'Estimamos la distancia': 'We estimate the distance',
    'tiempo': 'time',
    'Probemos con un ejemplo': 'Let’s try an example',
    'Supongamos que una señal acústica tarda 0,1 segundos en viajar entre un transmisor y un receptor. Considerando una velocidad aproximada del sonido de 1500 m/s:':
        'Suppose an acoustic signal takes 0.1 seconds to travel between a transmitter and a receiver. Taking an approximate speed of sound of 1500 m/s:',
    'Movete en el tiempo': 'Move through time',
    'Deslizá el control para cambiar el tiempo de propagación y observá la distancia estimada.':
        'Drag the slider to change the propagation time and watch the estimated distance.',
    'Tiempo de propagación': 'Propagation time',
    'Velocidad': 'Speed',
    'Cuanto mayor es el tiempo de propagación, mayor es la distancia recorrida.':
        'The longer the propagation time, the greater the distance travelled.',
    '¿Siempre usamos directamente distancia = velocidad × tiempo?': 'Do we always use distance = speed × time directly?',
    'Depende de cómo se realice la medición.': 'It depends on how the measurement is made.',
    'Un solo viaje': 'One-way trip',
    'Se mide el tiempo que tarda una señal en viajar desde un transmisor hasta un receptor.':
        'We measure the time a signal takes to travel from a transmitter to a receiver.',
    'Ida y vuelta': 'Round trip',
    'Se transmite una señal, se recibe una respuesta y se mide el tiempo asociado al recorrido de ida y vuelta.':
        'A signal is transmitted, a reply is received and the time of the round trip is measured.',
    'Por eso debemos conocer cómo funciona el sistema antes de convertir el tiempo medido en una distancia.':
        'That is why we need to know how the system works before turning the measured time into a distance.',
    'Quiero saber más: TOA, TDOA y ranging': 'I want to know more: TOA, TDOA and ranging',
    'Ranging (medición de distancia)': 'Ranging (distance measurement)',
    'es la estimación de la distancia entre dos puntos a partir de una señal acústica. Puede hacerse en un solo sentido, si transmisor y receptor comparten una referencia de tiempo, o en ida y vuelta, cuando el dispositivo responde a una interrogación. En el segundo caso, el tiempo medido incluye dos recorridos y el retardo de respuesta del equipo, que debe descontarse.':
        'the estimation of the distance between two points from an acoustic signal. It can be one-way, if transmitter and receiver share a time reference, or two-way, when the device replies to an interrogation. In the second case the measured time includes two trips plus the reply delay of the equipment, which must be subtracted.',
    'se utiliza el instante de llegada de la señal a cada receptor. Si se conoce el instante de transmisión, la diferencia entre ambos es el tiempo de propagación y, con la velocidad del sonido, se obtiene la distancia. Requiere que los relojes de transmisor y receptores estén sincronizados.':
        'the arrival instant of the signal at each receiver is used. If the transmission instant is known, the difference between them is the propagation time and, with the speed of sound, the distance follows. It requires the transmitter and receiver clocks to be synchronized.',
    'se utilizan las diferencias entre los instantes de llegada a distintos receptores, sin necesidad de conocer cuándo se transmitió la señal. Cada diferencia de tiempo define una hipérbola de posiciones posibles; la intersección de varias hipérbolas estima la posición. Solo requiere sincronizar los receptores entre sí.':
        'the differences between the arrival instants at different receivers are used, without needing to know when the signal was transmitted. Each time difference defines a hyperbola of possible positions; the intersection of several hyperbolas estimates the position. Only the receivers need to be synchronized with each other.',
    'Una distancia no alcanza para saber dónde estamos': 'One distance is not enough to know where we are',
    'Supongamos que sabemos que el dispositivo se encuentra a 100 metros de una referencia A. ¿Sabemos exactamente dónde está?':
        'Suppose we know the device is 100 metres from a reference A. Do we know exactly where it is?',
    'Una referencia A y varios dispositivos posibles ubicados sobre un círculo, todos a 100 metros de A':
        'A reference A and several possible devices placed on a circle, all 100 metres from A',
    'Todos estos dispositivos están a 100 m de A': 'All these devices are 100 m from A',
    'No. Puede encontrarse en muchos lugares diferentes situados a la misma distancia.':
        'No. It could be in many different places at the same distance.',
    '¿Qué pasa si agregamos más referencias?': 'What if we add more references?',
    'Combinemos mediciones': 'Let’s combine measurements',
    'Si conocemos la ubicación de varias referencias y estimamos la distancia del dispositivo respecto de cada una, podemos combinar las mediciones para determinar su posición.':
        'If we know the location of several references and estimate the distance from the device to each one, we can combine the measurements to determine its position.',
    'Encontrando el punto': 'Finding the point',
    'Cantidad de referencias': 'Number of references',
    'Ver animación': 'Play animation',
    '¡Encontramos el dispositivo!': 'We found the device!',
    'Referencias conocidas': 'Known references',
    'Medimos tiempos': 'We measure times',
    'Estimamos distancias': 'We estimate distances',
    'Combinamos las mediciones': 'We combine the measurements',
    'Estimamos la posición': 'We estimate the position',
    'Cada medición de distancia limita los lugares donde podría encontrarse el dispositivo. Al combinar varias distancias podemos encontrar una posición compatible con ellas.':
        'Each distance measurement narrows down where the device could be. By combining several distances we can find a position consistent with all of them.',
    'Este principio se denomina': 'This principle is called',
    'trilateración': 'trilateration',
    'Quiero saber más: trilateración, multilateración y geometría': 'I want to know more: trilateration, multilateration and geometry',
    'Trilateración': 'Trilateration',
    'en el plano, cada distancia a una referencia define una circunferencia de posiciones posibles; dos circunferencias se cortan en hasta dos puntos y una tercera resuelve la ambigüedad. En tres dimensiones las circunferencias pasan a ser esferas y hacen falta al menos cuatro referencias, salvo que se conozca la profundidad del dispositivo, por ejemplo con un sensor de presión.':
        'in the plane, each distance to a reference defines a circle of possible positions; two circles intersect in up to two points and a third one resolves the ambiguity. In three dimensions the circles become spheres and at least four references are needed, unless the depth of the device is known, for example from a pressure sensor.',
    'Multilateración': 'Multilateration',
    'las mediciones reales tienen error, así que los círculos rara vez se cortan exactamente en un punto. Cuando hay más mediciones que incógnitas, se busca la posición que mejor se ajusta a todas ellas, por ejemplo mediante mínimos cuadrados. Más referencias permiten mejorar la estimación y detectar mediciones incorrectas.':
        'real measurements have errors, so the circles rarely intersect exactly at one point. When there are more measurements than unknowns, we look for the position that best fits all of them, for example by least squares. More references improve the estimate and help detect wrong measurements.',
    'Sincronización': 'Synchronization',
    'medir un tiempo de propagación exige saber cuándo partió la señal y cuándo llegó. Un error de un milisegundo en el reloj equivale a un error de 1,5 metros en la distancia. Por eso los sistemas utilizan relojes de precisión, respuestas de ida y vuelta o diferencias de tiempo (TDOA) que no dependen del reloj del dispositivo.':
        'measuring a propagation time requires knowing when the signal left and when it arrived. A one-millisecond clock error equals a 1.5-metre error in distance. That is why systems use precision clocks, round-trip replies or time differences (TDOA) that do not depend on the device clock.',
    'Geometría': 'Geometry',
    'la posición relativa de las referencias influye en la calidad de la estimación. Si las referencias están alineadas o muy próximas entre sí, los círculos se cortan en ángulos muy pequeños y un error pequeño en las distancias se traduce en un error grande en la posición. Esta amplificación se cuantifica con la dilución de precisión (DOP).':
        'the relative position of the references affects the quality of the estimate. If the references are aligned or very close together, the circles intersect at very small angles and a small error in the distances becomes a large error in the position. This amplification is quantified by the dilution of precision (DOP).',
    '¿Dónde está el dispositivo?': 'Where is the device?',
    'Tres referencias A, B y C conocen su posición. Movés el dispositivo y las distancias cambian; escondés el dispositivo y las distancias te dicen dónde está.':
        'Three references A, B and C know their position. Move the device and the distances change; hide the device and the distances tell you where it is.',
    'Modo': 'Mode',
    'Ver': 'Watch',
    'Encontrar': 'Find',
    'Revelar': 'Reveal',
    'Otro dispositivo': 'Another device',
    'Superficie con tres referencias y un dispositivo móvil': 'Surface with three references and a movable device',
    'dispositivo': 'device',
    'La posición determina las distancias, y las distancias nos permiten estimar la posición.':
        'The position determines the distances, and the distances let us estimate the position.',
    '¿Es tan sencillo en el océano?': 'Is it that simple in the ocean?',
    'El mar hace las cosas un poco más difíciles. Algunos de los factores que intervienen:':
        'The sea makes things a little harder. Some of the factors involved:',
    'Velocidad del sonido': 'Speed of sound',
    'La velocidad depende de la temperatura, la salinidad y la presión.': 'The speed depends on temperature, salinity and pressure.',
    'La señal puede reflejarse en la superficie, el fondo y otras estructuras.': 'The signal can bounce off the surface, the seabed and other structures.',
    'Una misma señal puede llegar siguiendo diferentes trayectorias.': 'The same signal can arrive along different paths.',
    'Olas, embarcaciones, fauna y otros equipos generan sonidos.': 'Waves, vessels, wildlife and other equipment produce sounds.',
    'Para medir tiempos con precisión necesitamos referencias temporales adecuadas.': 'To measure times precisely we need suitable time references.',
    'La posición relativa de las referencias influye en la calidad de la estimación.': 'The relative position of the references affects the quality of the estimate.',
    'Quiero saber más: ¿cómo se implementan estos sistemas? LBL, SBL y USBL': 'I want to know more: how are these systems implemented? LBL, SBL and USBL',
    'Existen diferentes formas de posicionarnos acústicamente. Se diferencian, sobre todo, en cuán separadas están las referencias entre sí (la «línea de base»).':
        'There are different ways to position ourselves acoustically. They differ mainly in how far apart the references are (the “baseline”).',
    'Referencias distribuidas': 'Distributed references',
    'Utiliza varias referencias acústicas separadas entre sí y ubicadas en posiciones conocidas dentro o alrededor de la zona de operación, por ejemplo balizas fondeadas. Es la configuración de mayor precisión, a costa de desplegar y calibrar las referencias.':
        'It uses several acoustic references spaced apart and placed at known positions within or around the operating area, such as moored beacons. It is the most precise configuration, at the cost of deploying and calibrating the references.',
    'Referencias próximas entre sí': 'References close together',
    'Utiliza varios elementos acústicos separados por distancias relativamente pequeñas, normalmente instalados sobre una misma plataforma, como el casco de una embarcación. No hace falta fondear balizas, pero la precisión depende del tamaño de la plataforma.':
        'It uses several acoustic elements separated by relatively short distances, usually mounted on the same platform, such as the hull of a vessel. No beacons need to be moored, but precision depends on the size of the platform.',
    'Un arreglo acústico compacto': 'A compact acoustic array',
    'Utiliza varios elementos acústicos integrados en un arreglo compacto, generalmente instalado en una embarcación o plataforma. Las diferencias observadas entre las señales recibidas por cada elemento permiten obtener la dirección desde la que llega la señal; combinada con una estimación de distancia, determina la posición.':
        'It uses several acoustic elements integrated into a compact array, usually installed on a vessel or platform. The differences observed between the signals received by each element give the direction the signal comes from; combined with a distance estimate, it determines the position.',
    'Embarcación': 'Vessel',
    'Arreglo USBL': 'USBL array',
    'Dispositivo': 'Device',
    'Dirección + distancia': 'Direction + distance',
    'Dos problemas que tienen mucho en común': 'Two problems with a lot in common',
    'Para comunicarnos y para posicionarnos debajo del agua necesitamos realizar muchas operaciones similares: generamos una señal, la transmitimos, atraviesa el canal acústico, la recibimos y finalmente la procesamos.':
        'To communicate and to position ourselves underwater we need to perform many similar operations: we generate a signal, transmit it, it crosses the acoustic channel, we receive it and finally we process it.',
    'Lo que cambia es la información que queremos obtener.': 'What changes is the information we want to obtain.',
    'Generación': 'Generation',
    'Detección / correlación': 'Detection / correlation',
    '¿Qué queremos obtener?': 'What do we want to obtain?',
    'Comunicaciones': 'Communications',
    'Posicionamiento': 'Positioning',
    'Recuperamos la información transmitida.': 'We recover the transmitted information.',
    'distancia': 'distance',
    'posición': 'position',
    'Medimos cuándo llegó la señal, estimamos la distancia y combinamos varias mediciones para estimar la posición.':
        'We measure when the signal arrived, estimate the distance and combine several measurements to estimate the position.',
    '¿Cómo sabemos cuándo llegó la señal?': 'How do we know when the signal arrived?',
    'Para medir cuánto tardó una señal necesitamos determinar cuándo llegó al receptor.':
        'To measure how long a signal took we need to determine when it reached the receiver.',
    'Una posibilidad consiste en transmitir una señal conocida y buscarla posteriormente dentro de la señal recibida. El procesamiento digital de señales nos ayuda a detectar esa señal incluso cuando existe ruido.':
        'One option is to transmit a known signal and then search for it within the received signal. Digital signal processing helps us detect that signal even in the presence of noise.',
    'Señal conocida': 'Known signal',
    'Señal + ruido': 'Signal + noise',
    'Probá el correlador interactivo': 'Try the interactive correlator',
    'En la experiencia de Comunicaciones acústicas podés deslizar la secuencia de referencia sobre la señal recibida y ver aparecer el pico de correlación.':
        'In the Acoustic communications experience you can slide the reference sequence over the received signal and watch the correlation peak appear.',
    'Quiero saber más: correlación y estimación del instante de llegada': 'I want to know more: correlation and arrival-time estimation',
    'El receptor calcula la correlación entre la señal recibida y una copia de la señal transmitida (un filtro adaptado). El resultado presenta un pico en el instante en que ambas se alinean; la posición de ese pico es la estimación del tiempo de llegada.':
        'The receiver computes the correlation between the received signal and a copy of the transmitted one (a matched filter). The result shows a peak at the instant when both are aligned; the position of that peak is the arrival-time estimate.',
    'Cuanto mayor es el ancho de banda de la señal, más angosto es el pico de correlación y más precisa es la estimación del instante de llegada.':
        'The wider the bandwidth of the signal, the narrower the correlation peak and the more precise the arrival-time estimate.',
    'Las secuencias con buena autocorrelación, como las utilizadas en espectro ensanchado, producen picos nítidos con lóbulos laterales bajos.':
        'Sequences with good autocorrelation, such as those used in spread spectrum, produce sharp peaks with low sidelobes.',
    'En un canal con multicamino aparecen varios picos: normalmente interesa el primero, que corresponde al camino directo.':
        'In a multipath channel several peaks appear: usually the first one matters, as it corresponds to the direct path.',
    'Un error de un milisegundo en el instante de llegada se traduce en un error de aproximadamente 1,5 metros en la distancia estimada.':
        'A one-millisecond error in the arrival instant becomes an error of about 1.5 metres in the estimated distance.',
    '¿Para qué sirve el posicionamiento acústico?': 'What is acoustic positioning used for?',
    'Robots submarinos': 'Underwater robots',
    'Localizar y seguir vehículos submarinos durante sus misiones.': 'Locating and tracking underwater vehicles during their missions.',
    'Instrumentación oceanográfica': 'Oceanographic instrumentation',
    'Conocer la posición de sensores e instrumentos utilizados para estudiar el océano.': 'Knowing the position of sensors and instruments used to study the ocean.',
    'Operaciones desde embarcaciones': 'Vessel operations',
    'Seguir dispositivos desplegados desde una embarcación.': 'Tracking devices deployed from a vessel.',
    'Investigación científica': 'Scientific research',
    'Relacionar una medición realizada bajo el agua con el lugar donde fue obtenida.': 'Linking an underwater measurement to the place where it was taken.',
    'Localizar equipos y asistir en tareas de inspección, instalación o recuperación.': 'Locating equipment and assisting in inspection, installation or recovery tasks.',
    'Detrás de un sistema de posicionamiento acústico hay una cadena de conceptos que podés seguir profundizando:':
        'Behind an acoustic positioning system there is a chain of concepts you can keep exploring:',
    'Correlación': 'Correlation',
    'Experimentá con el posicionamiento acústico': 'Experiment with acoustic positioning',
    'Estamos desarrollando nuevas experiencias para mostrar cómo las señales acústicas pueden utilizarse no solo para transmitir información, sino también para estimar la posición de dispositivos debajo del agua.':
        'We are developing new experiences to show how acoustic signals can be used not only to transmit information but also to estimate the position of devices underwater.',
    'Experiencia en desarrollo': 'Experience in development',
    'Del mensaje a la posición': 'From the message to the position',
    'El sonido nos permite resolver diferentes desafíos debajo del agua. Podemos utilizar señales acústicas para transmitir información, pero también para medir distancias y estimar posiciones.':
        'Sound lets us solve different challenges underwater. We can use acoustic signals to transmit information, but also to measure distances and estimate positions.',
    'Para hacerlo necesitamos comprender cómo se propaga el sonido, medir tiempos, detectar señales y procesar la información recibida.':
        'To do so we need to understand how sound propagates, measure times, detect signals and process the received information.',
    'Así, electrónica, telecomunicaciones y procesamiento digital de señales se combinan para desarrollar herramientas que nos ayudan a explorar y comprender el ambiente subacuático.':
        'Thus electronics, telecommunications and digital signal processing come together to develop tools that help us explore and understand the underwater environment.',
    'Experiencia anterior': 'Previous experience',
    'Con una referencia, el dispositivo puede estar en cualquier punto del círculo.': 'With one reference, the device could be anywhere on the circle.',
    'Con dos referencias quedan solo dos puntos posibles.': 'With two references only two possible points remain.',
    'La tercera referencia resuelve la ambigüedad: hay un único punto compatible con las tres distancias.':
        'The third reference resolves the ambiguity: there is a single point consistent with all three distances.',
    'Arrastrá el dispositivo (o tocá la superficie) y observá cómo cambian las tres distancias.':
        'Drag the device (or tap the surface) and watch how the three distances change.',
    'El dispositivo está escondido. Tocá la superficie donde creés que está: los tres círculos te dan la pista.':
        'The device is hidden. Tap the surface where you think it is: the three circles give you the clue.',
    '¡Lo encontraste! Error:': 'You found it! Error:',
    'Estás a': 'You are',
    'del dispositivo. Buscá el punto donde se cruzan los tres círculos.': 'from the device. Look for the point where the three circles cross.',
    'Ahí estaba. Tu estimación quedó a': 'There it was. Your guess was',

    # --- Cooperación ---
    'Cooperación científica e industrial del GIPIS. Vínculos con el sector productivo, convenios de investigación y transferencia tecnológica desde la Patagonia.':
        'Scientific and industrial cooperation at GIPIS. Ties with the productive sector, research agreements, and technology transfer from Patagonia.',
    'Campus Universitario': 'University Campus',
    'Cooperación Científica e Industrial': 'Scientific and Industrial Cooperation',
    'Desarrollamos vinculaciones estratégicas con instituciones académicas, centros de investigación y el sector productivo.':
        'We build strategic partnerships with academic institutions, research centers and industry.',
    'Redes Académicas': 'Academic Networks',
    'Convenios de colaboración con universidades nacionales e internacionales para intercambio científico.':
        'Collaboration agreements with national and international universities for scientific exchange.',
    'Transferencia Industrial': 'Industrial Transfer',
    'Soluciones profesionales y asesoría técnica para empresas del sector energético y telecomunicaciones.':
        'Professional solutions and technical consulting for companies in the energy and telecommunications sectors.',
    'Proyectos Conjuntos': 'Joint Projects',
    'Planificación y ejecución de proyectos I+D+i con financiamiento público, privado e institucional.':
        'Planning and execution of R&D&i projects with public, private and institutional funding.',
    'Red de Colaboración': 'Collaboration Network',
    'Colaboramos con prestigiosas organizaciones para potenciar el desarrollo tecnológico regional y nacional.':
        'We collaborate with prestigious organizations to boost regional and national technological development.',
    'Oportunidades de Cooperación': 'Cooperation Opportunities',
    '¿Su institución o empresa está interesada en colaborar con nosotros? Buscamos constantemente nuevos socios para proyectos de investigación, tesis doctorales y consultoría tecnológica.':
        'Is your institution or company interested in collaborating with us? We are always looking for new partners for research projects, doctoral theses and technology consulting.',
    'Becas de postgrado conjuntas': 'Joint postgraduate scholarships',
    'Prácticas profesionales': 'Professional internships',
    'I+D para el sector industrial': 'R&D for industry',
    'Proyectos internacionales': 'International projects',
    'Iniciar una Propuesta': 'Start a Proposal',
    'Contactar': 'Contact us',

    # --- Novedades ---
    'Enterate de las últimas actividades, logros y anuncios del grupo.':
        'Stay up to date with the latest activities, achievements and announcements of the group.',
    'Volver a novedades': 'Back to news',
    'No hay novedades publicadas por el momento.': 'There are no news posted at the moment.',
    'No hay novedades aún.': 'No news yet.',
    'Novedades y noticias del GIPIS. Congresos, publicaciones, proyectos y actividades del grupo de investigación.':
        'News and updates from GIPIS. Conferences, publications, projects and activities of the research group.',
    'Publicado en Facebook': 'Posted on Facebook',
    'Novedad del GIPIS, Grupo de Investigación en Procesamiento de la Información y Sensores.':
        'News from GIPIS, the Information Processing and Sensors Research Group.',
    'Detalle': 'Detail',
    'Volver a Novedades': 'Back to News',
    'Anterior': 'Previous',
    'Siguiente': 'Next',
    'Paginación': 'Pagination',
    'Cooperación académica': 'Academic cooperation',
    'Cooperación científica': 'Scientific cooperation',
    'Vinculación y transferencia': 'Partnerships and technology transfer',
    'Comunicación pública de la ciencia': 'Public science communication',
    'Filtrar por categoría': 'Filter by category',
    'Todas': 'All',
    'No hay novedades en esta categoría.': 'There are no news in this category.',
    'Galería de fotos': 'Photo gallery',
    'Ver en tamaño completo': 'View full size',
    'Foto anterior': 'Previous photo',
    'Foto siguiente': 'Next photo',
    'Foto': 'Photo',
    'Archivos adjuntos': 'Attachments',

    # --- Producción científica ---
    'Producción Científica': 'Scientific Production',
    'Producción': 'Production',
    'Producción científica del GIPIS: publicaciones, proyectos y tesis del grupo de investigación.':
        'Scientific production of GIPIS: publications, projects and theses of the research group.',
    'Publicaciones, proyectos y tesis del grupo. Usá los filtros para encontrar trabajos específicos.':
        'Publications, projects and theses of the group. Use the filters to find specific works.',
    'Buscar por título o autor…': 'Search by title or author…',
    'Todos los años': 'All years',
    'Todas las secciones': 'All sections',
    'Limpiar filtros': 'Clear filters',
    'No se encontraron resultados con esos filtros.': 'No results were found with those filters.',
    'La producción del grupo se mostrará próximamente.': "The group's production will be published soon.",
    'Ver toda la producción': 'View all production',
    'Citar (BibTeX)': 'Cite (BibTeX)',
    'citas': 'citations',
    '¡Copiado!': 'Copied!',
    'Software y Repositorios': 'Software & Repositories',
    'Ver en GitHub': 'View on GitHub',

    # --- Contacto ---
    'Estamos interesados en establecer nuevas colaboraciones y responder tus consultas.':
        'We are interested in establishing new collaborations and answering your inquiries.',
    'Envianos tu consulta': 'Send us your inquiry',
    'Nombre completo': 'Full name',
    'Correo electrónico': 'Email address',
    'Asunto': 'Subject',
    'Mensaje': 'Message',
    'Enviar mensaje': 'Send message',
    'Información de contacto': 'Contact information',
    'Dirección': 'Address',
    'Seguinos en redes': 'Follow us',
    'Escribinos y te responderemos a la brevedad.':
        'Write to us and we will get back to you shortly.',
    'Contactá al GIPIS. Consultas académicas, propuestas de cooperación científica o información sobre líneas de investigación. Ciudad Universitaria, Comodoro Rivadavia.':
        'Contact GIPIS. Academic inquiries, scientific cooperation proposals or information about research lines. Ciudad Universitaria, Comodoro Rivadavia.',
    'Contáctenos': 'Contact Us',
    'Estamos a su disposición para consultas académicas, propuestas de cooperación científica o información sobre nuestras líneas de investigación.':
        'We are at your disposal for academic inquiries, scientific cooperation proposals or information about our research lines.',
    'Nombre Completo': 'Full Name',
    'Ej: Dr. Juan Pérez': 'E.g.: Dr. John Smith',
    'Correo Electrónico': 'Email Address',
    'nombre@institucion.edu': 'name@institution.edu',
    'Ej: Consulta sobre Redes de Sensores': 'E.g.: Inquiry about Sensor Networks',
    'Escriba su consulta aquí...': 'Write your inquiry here...',
    'Enviar Mensaje': 'Send Message',
    'Dirección Postal': 'Postal Address',
    'Ver en Google Maps': 'View on Google Maps',

    # --- Panel de miembros y administración ---
    # Login / recuperación de contraseña
    'Bienvenido': 'Welcome',
    'Ingresá con tu cuenta de miembro': 'Sign in with your member account',
    'Contraseña': 'Password',
    '¿Olvidaste tu contraseña?': 'Forgot your password?',
    'Volver al inicio': 'Back to home',
    '¿No tenés cuenta? Contactá al administrador del grupo.':
        "Don't have an account? Contact the group administrator.",
    'Recuperar contraseña': 'Reset your password',
    'Ingresá tu email y te enviamos un enlace para restablecerla.':
        'Enter your email and we will send you a link to reset it.',
    'Enviar enlace': 'Send link',
    'Volver al ingreso': 'Back to sign in',
    'Nueva contraseña': 'New password',
    'Hola': 'Hello',
    'definí tu nueva contraseña.': 'set your new password.',
    'Mínimo 8 caracteres': 'At least 8 characters',
    'Repetir contraseña': 'Repeat password',
    'Guardar contraseña': 'Save password',
    # Dashboard
    'Acá podés administrar tu información.': 'Here you can manage your information.',
    'Cerrar sesión': 'Sign out',
    'Ver perfil público': 'View public profile',
    'Administración': 'Administration',
    'Miembros': 'Members',
    'Información actual': 'Current information',
    'Público': 'Public',
    'Privado': 'Private',
    'Con este email iniciás sesión': 'You sign in with this email',
    'Título/Grado': 'Degree',
    'Cargo/Posición': 'Position',
    'Biografía': 'Biography',
    'Sin biografía': 'No biography',
    'Editar mi perfil': 'Edit my profile',
    'Mi Producción': 'My Production',
    # Editar perfil
    'Editar Perfil': 'Edit Profile',
    'Editar perfil': 'Edit profile',
    'Editar perfil de': 'Edit profile of',
    'Volver a Miembros': 'Back to Members',
    'Estás editando este perfil como administrador. Los cambios se aplican directamente y el integrante no recibe aviso.':
        'You are editing this profile as an administrator. Changes apply immediately and the member is not notified.',
    'Datos administrativos': 'Administrative data',
    'Email de acceso *': 'Sign-in email *',
    'Con este email inicia sesión; también recibe ahí el enlace de recuperación de contraseña.':
        'The member signs in with this email; password reset links are sent there too.',
    'Orden': 'Order',
    'Desempate dentro de la misma categoría y cargo (menor = más arriba).':
        'Tie-breaker within the same category and position (lower = higher up).',
    'El rol y el estado se cambian desde el listado de Miembros.':
        'Role and status are changed from the Members list.',
    'Alta de nuevos integrantes, edición de perfiles y gestión de roles.':
        'Add new members, edit profiles and manage roles.',
    'Volver al dashboard': 'Back to dashboard',
    'Foto de perfil': 'Profile photo',
    'Hacé click o arrastrá una imagen': 'Click or drag an image',
    'PNG, JPG o WebP • Máximo 10 MB': 'PNG, JPG or WebP • 10 MB max',
    'Eliminar foto actual': 'Remove current photo',
    'Información básica': 'Basic information',
    'Nombre completo *': 'Full name *',
    'Título / Grado académico': 'Degree / Academic title',
    'Ej: Dr. en Ingeniería': 'E.g.: PhD in Engineering',
    'Cargo / Posición': 'Position',
    'Ej: Investigador Principal': 'E.g.: Principal Investigator',
    'Contanos sobre tu trayectoria, áreas de interés, etc.':
        'Tell us about your background, areas of interest, etc.',
    'Biografía en inglés (opcional)': 'Biography in English (optional)',
    'Si la dejás vacía, los visitantes en inglés ven tu biografía en español.':
        'If you leave it empty, English-language visitors will see your Spanish biography.',
    'LinkedIn (URL completa)': 'LinkedIn (full URL)',
    'Tu identificador de': 'Your identifier from',
    'Se muestra en tu perfil público y permite importar tus publicaciones desde "Mi Producción".':
        'It is shown on your public profile and lets you import your publications from "My Production".',
    'Emails de contacto': 'Contact emails',
    'Podés elegir qué emails se muestran en tu perfil público y con cuáles podés iniciar sesión (tu email de acceso original':
        'You can choose which emails are shown on your public profile and which ones you can sign in with (your original sign-in email',
    'siempre funciona).': 'always works).',
    'Mostrar en perfil público': 'Show on public profile',
    'Permitir iniciar sesión con este email': 'Allow signing in with this email',
    'Teléfono de contacto': 'Contact phone',
    'Cambiar contraseña': 'Change password',
    '(opcional)': '(optional)',
    'Dejá en blanco para no cambiarla': 'Leave blank to keep it unchanged',
    'Mínimo 6 caracteres. Hacé click en el ojo para ver la contraseña.':
        'At least 6 characters. Click the eye icon to reveal the password.',
    'La imagen no puede superar los 10 MB.': 'The image cannot exceed 10 MB.',
    'Guardar cambios': 'Save changes',
    'Cancelar': 'Cancel',
    # Mi Producción
    'Tus publicaciones, proyectos y direcciones. Lo que compartas aparece también en la página de Investigación del sitio.':
        "Your publications, projects and supervisions. Whatever you share also appears on the site's Research page.",
    'Volver al panel': 'Back to dashboard',
    'Importar desde SIGEVA': 'Import from SIGEVA',
    'Subí el PDF de tu CV exportado de SIGEVA (Banco de datos → Imprimir CV). Vas a poder revisar y elegir qué importar antes de guardar.':
        'Upload the PDF of your CV exported from SIGEVA (Data bank → Print CV). You will be able to review and choose what to import before saving.',
    'Analizar PDF': 'Analyze PDF',
    'Importar desde ORCID': 'Import from ORCID',
    'Vamos a buscar los trabajos públicos de tu registro':
        'We will look up the public works from your record',
    'Vas a poder revisar y elegir qué importar antes de guardar.':
        'You will be able to review and choose what to import before saving.',
    'Buscar mis publicaciones': 'Find my publications',
    'Ingresá tu ORCID iD (o la URL de tu perfil en orcid.org) para buscar tus trabajos públicos. Se guarda en tu perfil para la próxima vez.':
        'Enter your ORCID iD (or your orcid.org profile URL) to look up your public works. It is saved to your profile for next time.',
    'Buscar publicaciones': 'Find publications',
    'Descubrir publicaciones (OpenAlex)': 'Discover publications (OpenAlex)',
    'OpenAlex indexa publicaciones de toda la literatura académica, incluso las que no cargaste en ORCID. Buscamos por tu ORCID iD y te mostramos lo que encuentre, con su cantidad de citas. Ojo: puede traer atribuciones erróneas — revisá antes de importar.':
        'OpenAlex indexes publications from across the academic literature, including ones you did not add to ORCID. We search by your ORCID iD and show you what it finds, with citation counts. Note: it may include incorrect attributions — review before importing.',
    'Buscar en OpenAlex': 'Search OpenAlex',
    'Cargá tu ORCID iD (en la tarjeta de arriba o en tu perfil) y vas a poder descubrir publicaciones tuyas indexadas en OpenAlex, con su cantidad de citas.':
        'Add your ORCID iD (in the card above or in your profile) and you will be able to discover your publications indexed in OpenAlex, with citation counts.',
    'Agregar trabajo a mano': 'Add a work manually',
    '¿Tenés el DOI? Completá los campos automáticamente':
        'Have the DOI? Fill in the fields automatically',
    '10.1109/5.771073 o https://doi.org/…': '10.1109/5.771073 or https://doi.org/…',
    'Buscar DOI': 'Look up DOI',
    'Título *': 'Title *',
    'Tipo': 'Type',
    'Año': 'Year',
    'Autores': 'Authors',
    'Agregar': 'Add',
    'En el sitio': 'On the site',
    'Quitar de la página de Investigación': 'Remove from the Research page',
    'Compartir al sitio': 'Share to the site',
    'Guardar': 'Save',
    '¿Eliminar este trabajo de tu producción?': 'Delete this work from your production?',
    'Eliminar': 'Delete',
    'Todavía no cargaste ningún trabajo. Importá tu CV de SIGEVA o agregá uno a mano.':
        'You have not added any works yet. Import your SIGEVA CV or add one manually.',
    'Ingresá un DOI.': 'Enter a DOI.',
    'Consultando…': 'Looking up…',
    'Datos cargados. Revisalos antes de agregar.': 'Data loaded. Review it before adding.',
    'No se pudo consultar el DOI.': 'Could not look up the DOI.',
    # Revisión de importaciones
    'Revisar importación': 'Review import',
    'Destildá lo que no tenga relevancia para el grupo y confirmá. Después vas a poder editar cada trabajo y elegir cuáles compartir en la página de Investigación.':
        'Uncheck anything not relevant to the group and confirm. Afterwards you will be able to edit each work and choose which ones to share on the Research page.',
    'Ya está en tu producción': 'Already in your production',
    'Importar seleccionados': 'Import selected',
    'Esto es lo que encontramos en tu CV de SIGEVA.': 'This is what we found in your SIGEVA CV.',
    'Datos de perfil': 'Profile data',
    'Reemplaza tu valor actual:': 'Replaces your current value:',
    'Biografía (resumen de experticia):': 'Biography (expertise summary):',
    'Reemplaza tu biografía actual.': 'Replaces your current biography.',
    # Admin: miembros
    'Administrar Miembros': 'Manage Members',
    'Nuevo integrante': 'New member',
    'Contraseña inicial *': 'Initial password *',
    'El integrante puede cambiarla desde su perfil.': 'The member can change it from their profile.',
    'Categoría *': 'Category *',
    '— Elegir categoría —': '— Choose a category —',
    'Determina en qué bloque aparece en la página del grupo.':
        'Determines which block they appear in on the team page.',
    'Ej: Ing. Electrónico': 'E.g.: Electronic Engineer',
    'Ej: Investigador': 'E.g.: Researcher',
    'Rol': 'Role',
    'Miembro': 'Member',
    'Administrador': 'Administrator',
    'Crear integrante': 'Create member',
    'Integrantes': 'Members',
    'Nombre': 'Name',
    'Categoría': 'Category',
    'Estado': 'Status',
    'Acciones': 'Actions',
    '⚠ Sin categoría': '⚠ No category',
    'Activo': 'Active',
    'Inactivo': 'Inactive',
    'Quitar admin': 'Remove admin',
    'Hacer admin': 'Make admin',
    'Desactivar': 'Deactivate',
    'Activar': 'Activate',
    '¿Generar una contraseña temporal para': 'Generate a temporary password for',
    'La actual dejará de funcionar.': 'The current one will stop working.',
    'Restablecer contraseña': 'Reset password',
    '(vos)': '(you)',
    # Admin: investigación
    'Administrar Investigación': 'Manage Research',
    'Secciones e ítems (publicaciones, proyectos, tesis, etc.) que se muestran en la página de Investigación.':
        'Sections and items (publications, projects, theses, etc.) shown on the Research page.',
    'Agregar ítem': 'Add item',
    'Sección *': 'Section *',
    'Resumen / detalle': 'Summary / detail',
    'Nueva sección': 'New section',
    'Ej: Patentes': 'E.g.: Patents',
    'Crear sección': 'Create section',
    'ítems': 'items',
    'Resumen': 'Summary',
    '¿Eliminar este ítem del sitio?': 'Delete this item from the site?',
    'Sin ítems.': 'No items.',
    # Admin: red de colaboración
    'Organizaciones que se muestran en la página de Cooperación.':
        'Organizations shown on the Cooperation page.',
    'Agregar organización': 'Add organization',
    'Nombre de la organización *': 'Organization name *',
    'Sitio web (opcional)': 'Website (optional)',
    '(opcional, PNG/JPG/WebP/SVG, idealmente con fondo transparente)':
        '(optional, PNG/JPG/WebP/SVG, ideally with a transparent background)',
    'Orden': 'Order',
    'Original': 'Original',
    'Hacé clic en la parte de la foto que tiene que quedar siempre visible': 'Click the part of the photo that must always stay visible',
    'Así se ve en el carrusel': 'How it looks in the carousel',
    'Así se ve en la tarjeta': 'How it looks on the card',
    'Vista previa: carrusel y tarjeta': 'Preview: carousel and card',
    '(orden 1 = portada; clic en la foto para elegir qué parte queda visible al recortar)': '(order 1 = cover; click the photo to choose which part stays visible when cropped)',
    'Sitio web': 'Website',
    'Quitar logo': 'Remove logo',
    '¿Quitar': 'Remove',
    'de la Red de Colaboración?': 'from the Collaboration Network?',
    'No hay organizaciones cargadas.': 'No organizations added yet.',
    # Admin: novedades
    'Cargá y administrá las novedades que se muestran en el sitio y en la portada.':
        'Add and manage the news shown on the site and on the home page.',
    'Publicar novedad': 'Publish news',
    'Congresos, Proyectos, Publicaciones…': 'Conferences, Projects, Publications…',
    'Fecha': 'Date',
    '(se muestra en las tarjetas)': '(shown on the cards)',
    'Contenido': 'Content',
    '(texto de la novedad; separá párrafos con una línea en blanco)':
        '(news text; separate paragraphs with a blank line)',
    'Imagen': 'Image',
    '(opcional, PNG/JPG/WebP)': '(optional, PNG/JPG/WebP)',
    'Traducción al inglés (opcional)': 'English translation (optional)',
    'Si se completa, los visitantes que usen el sitio en inglés verán esta versión; si no, se muestra el texto en español.':
        'If provided, visitors using the site in English will see this version; otherwise the Spanish text is shown.',
    'Publicar': 'Publish',
    'Sin fecha': 'No date',
    'Ver en el sitio': 'View on the site',
    'Quitar imagen actual': 'Remove current image',
    '¿Eliminar la novedad': 'Delete the news item',
    'Todavía no hay novedades cargadas.': 'No news added yet.',
    # Botones admin en páginas públicas
    'Gestionar novedades': 'Manage news',
    'Sin categoría': 'No category',
    'Métricas de la web': 'Website analytics',
    'Editar novedad': 'Edit post',
    'Fotos': 'Photos',
    'Podés elegir varias a la vez. La primera de la galería es la portada; con más de una se muestra un carrusel.':
        'You can pick several at once. The first one in the gallery is the cover; with more than one a carousel is shown.',
    'Se listan al pie de la novedad para descargar. Máximo 25 MB por envío.':
        'Listed at the bottom of the post for download. Up to 25 MB per submission.',
    'Para intercalar una foto de la galería entre párrafos, escribí [foto 2] (el número según el orden de la galería) en una línea aparte.':
        'To place a gallery photo between paragraphs, write [photo 2] (the number follows the gallery order) on its own line.',
    'Galería': 'Gallery',
    '(orden 1 = portada; epígrafe opcional)': '(order 1 = cover; caption optional)',
    'Orden': 'Order',
    'Quitar': 'Remove',
    'Epígrafe': 'Caption',
    'Nombre visible': 'Display name',
    'Gestionar red de colaboración': 'Manage collaboration network',
    'Gestionar miembros': 'Manage members',
    'Gestionar investigación': 'Manage research',
}


MONTHS = {
    'es': ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio',
           'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'],
    'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July',
           'August', 'September', 'October', 'November', 'December'],
}


def format_date(dt, lang='es', short=False):
    """Formatear fecha según el idioma de la interfaz ('1 de agosto de 2026',
    'August 1, 2026'; short: '1 ago, 2026' / 'Aug 1, 2026')."""
    if not dt:
        return ''
    month = MONTHS.get(lang, MONTHS['es'])[dt.month - 1]
    if lang == 'en':
        return f'{month[:3]} {dt.day}, {dt.year}' if short else f'{month} {dt.day}, {dt.year}'
    return f'{dt.day} {month[:3]}, {dt.year}' if short else f'{dt.day} de {month} de {dt.year}'


def translate(text, lang):
    """Traducir una cadena; si no hay traducción, devolver el original."""
    if lang == 'en':
        return TRANSLATIONS.get(text, text)
    return text
