import datetime
from enum import Enum

class SectionEnum(Enum):
  FEATURED_IMAGE = 'FEATURED_IMAGE'
  CONTACT_INFO = 'CONTACT_INFO'
  REQUIREMENTS = 'REQUIREMENTS'
  GENERAL_INFO = 'GENERAL_INFO'
  GENERAL_GOAL = 'GENERAL_GOAL'
  TARGET_AUDIENCES = 'TARGET_AUDIENCES'
  STAFF = 'STAFF'
  ADMISSION_INFO = 'ADMISSION_INFO'
  BROCHURE = 'BROCHURE'

programs = [
    {
      'id': 1,
      'siga_program_code': 2, 
      'banner_program_code': 'banner_code', 
      'banner_majr_code': 'banner_code_majr', 
      'version': 1, 
      'name': 'Diploma en Higiene Ocupacional Concepción',
      'level_type': {
        'id': 1,
        'name': 'Diploma',
      },
      'start_date': datetime.datetime(2024, 3, 1),
      'end_date': datetime.datetime(2024, 3, 1),
      'duration_value': 152,
      'duration_type_name': 'horas',
      'place': 'Aula virtual UTFSM',
      'quotas': 60,
      'program_amount': 2100000,
      'registration_amount': 100000,
      'modality_type_name': 'Online',
      'discount_text': '15% con inscripción temprana. 25% ex alumnos y ex alumnos IPRLA.',
      'modules': [
        {
          'id': 1,
          'seq_number': 1,
          'description': 'Modulo I: Lugar de Trabajo',
          'hours': 10,
        },
        {
          'id': 2,
          'seq_number': 2,
          'description': 'Modulo II: Factores Ambientales',
          'hours': 20,
        },
        {
          'id': 3,
          'seq_number': 3,
          'description': 'Modulo III: Control de Ingeniería',
          'hours': 30,
        },
      ],
      'sections': [
        {
          'id': 1,
          'section_type': {
            'name': 'Main image',
            'type': SectionEnum.FEATURED_IMAGE,
            'seq_number': 1,
          },
          'seq_number': 1,
          'text': '',
          'publish': datetime.datetime(2024, 3, 1),
          'attached_files': [
            {
              'id': '1',
              'file_name': 'p/Higiene-ocupacional.png',
              'file_type_name': 'PNG',
              'text': 'Higiene Ocupacional',
              'link': '/temp/Higiene-ocupacional.png',
            },
          ],
        },
        {
          'id': 2,
          'section_type': {
            'name': 'Requisitos',
            'type': SectionEnum.REQUIREMENTS,
            'seq_number': 2,
          },
          'seq_number': 2,
          'text': 'Título Profesional o Título Técnico Nivel Superior',
          'publish': datetime.datetime(2024, 3, 1),
          'attached_files': [],
        },
        {
          'id': 3,
          'section_type': {
            'name': 'Más Información',
            'type': SectionEnum.CONTACT_INFO,
            'seq_number': 3,
          },
          'seq_number': 3,
          'text': 'educacion.continua@usm.cl',
          'publish': datetime.datetime(2024, 3, 1),
          'attached_files': [],
        },
        {
          'id': 4,
          'section_type': {
            'name': 'Información General',
            'type': SectionEnum.GENERAL_INFO,
            'seq_number': 4,
          },
          'seq_number': 4,
          'text': """El Diploma en Higiene Ocupacional es un programa diseñado para proporcionar las habilidades necesarias a los profesionales que deseen evaluar ambientes de trabajo donde se encuentren presentes agentes químicos, físicos y biológicos, así como abordar temas relacionados con los factores humanos.

 

          El objetivo principal del programa es mejorar las condiciones de trabajo de las personas. Este diploma es una oportunidad para actualizar a los profesionales en esta área y contribuir de manera efectiva en la mejora de los ambientes de trabajo, aumentando así la productividad en las organizaciones.""",
          'publish': datetime.datetime(2024, 3, 1),
          'attached_files': [],
        },
        {
          'id': 5,
          'section_type': {
            'name': 'Objetivo General',
            'type': SectionEnum.GENERAL_GOAL,
            'seq_number': 5,
          },
          'seq_number': 5,
          'text': 'Entregar las competencias para todo aquel profesional, que desee desempeñarse evaluando ambientes de trabajo, en el cual se encuentren presentes agentes: químicos, físicos y biológicos, inclusive abordar temáticas relacionadas con los factores humanos, mejorando con ello las condiciones de trabajo de las personas.',
          'publish': datetime.datetime(2024, 3, 1),
          'attached_files': [],
        },
        {
          'id': 6,
          'section_type': {
            'name': 'A quién va dirigido',
            'type': SectionEnum.TARGET_AUDIENCES,
            'seq_number': 6,
          },
          'seq_number': 6,
          'text': 'Profesionales que deseen profundizar sus conocimientos en el ámbito Higiene Ocupacional ',
          'publish': datetime.datetime(2024, 3, 1),
          'attached_files': [],
        },
        {
          'id': 7,
          'section_type': {
            'name': 'Staff de Profesores',
            'type': SectionEnum.STAFF,
            'seq_number': 7,
          },
          'seq_number': 7,
          'text': """María Eliana Tobar Garziglia
          Carlos Andrés Ibarra Villanueva
          Christian Eduardo Albornoz Villagra
          Alfonso Enrique Espinoza Leyton
          Rolando Eduardo Vilasau Domínguez
          Rodrigo Domínguez Carmona
          Juan Carlos Valenzuela Illanes
          Juan Leopoldo Ferruz Rojas
          David Eduardo Escanilla Camus
          Víctor Hugo Lizama Molina
          Denis Riquelme Sandoval""",
          'publish': datetime.datetime(2024, 3, 1),
          'attached_files': [],
        },
        {
          'id': 8,
          'section_type': {
            'name': 'Proceso de Admisión',
            'type': SectionEnum.ADMISSION_INFO,
            'seq_number': 8,
          },
          'seq_number': 8,
          'text': 'Si deseas más información sobre el proceso de admisión puedes escribir a: carlos.bizamaf@usm.cl o educacion.continua@usm.cl',
          'publish': datetime.datetime(2024, 3, 1),
          'attached_files': [],
        },
        {
          'id': 9,
          'section_type': {
            'name': 'Proceso de Admisión',
            'type': SectionEnum.BROCHURE,
            'seq_number': 9,
          },
          'seq_number': 9,
          'text': '',
          'publish': datetime.datetime(2024, 3, 1),
          'attached_files': [
            {
              'id': '1',
              'file_name': 'Diploma-en-Gestion-Estrategica-2023.pdf',
              'file_type_name': 'PDF',
              'text': 'Diploma en Gestion Estrategica 2023',
              'link': 'https://educacioncontinua.usm.cl/wp-content/uploads/2023/01/Diploma-en-Gestion-Estrategica-2023.pdf',
            },
          ],
        },
      ],
      'managers': [
        {
          'id': 1,
          'last_name': 'Hurtado',
          'first_name': 'Marcela',
          'profile': """El patrimonio cultural, representado por sus múltiples expresiones, se entiende cada vez más integrado a la vida cotidiana de las personas, jugando un papel importante como factor de cohesión social. En particular, el patrimonio arquitectónico y urbano constituye una de las categorías más significativas por las oportunidades que ofrece de albergar diversas actividades, de ser portador de la memoria de los pueblos y de configurar la imagen de nuestras ciudades y asentamientos en general. Gran parte de estos bienes son públicos y tienen, por tanto, una fuerte vocación de uso público, lo que contribuye a conectar a las comunidades con su historia y sus tradiciones. 

          La gestión y el manejo de este valioso patrimonio recae en muchas ocasiones en instituciones y organismos públicos que deben hacer frente a diversos factores que amenazan su preservación en el tiempo: la natural degradación física, la obsolescencia funcional frente a las nuevas demandas, los elevados costos de mantenimiento, además de aquellos derivados de eventos naturales como sismos o, cada vez más preocupante, el impacto del cambio climático. Si bien existen desde el Estado iniciativas que dan cabida a proyectos que buscan rescatar este tipo de bienes culturales, no existe a la fecha un conocimiento generalizado de éstas, que dé espacio a formulación de propuestas de manera más extendida en el país. 
          
          Desde este diagnóstico, el presente Diplomado apunta a fortalecer las capacidades de profesionales y técnicos, principalmente de organismos públicos, pero también del sector privado, que tienen entre sus responsabilidades la búsqueda de alternativas para la salvaguardia y preservación de patrimonio arquitectónico y/o urbano. El foco está puesto, por tanto, en profundizar en el conocimiento de los procesos que llevan a la formulación de proyectos, en sus distintas fases y características, a partir de fundamentos teóricos, experiencias exitosas y ejercicios prácticos. """,
          'prefix': 'Dra.',
          'linkedin': 'https://www.linkedin.com/in/marcela-hurtado-61692539/',
          'image':
            'https://educacioncontinua.usm.cl/wp-content/uploads/2023/01/Marcela-Hurtado.png',
        },
        {
          'id': 2,
          'last_name': 'Boris',
          'first_name': 'Uribe Améstica',
          'profile': """Estimado Postulante:

 

          Es un placer dirigirme a ustedes para presentarles el programa de Diploma en Higiene Ocupacional, del cual tengo el honor de ser el director. Mi nombre es Boris Uribe Améstica y quiero darles la más cordial bienvenida a nuestro programa.
          
           
          
          Desde su creación, hemos tenido el privilegio de realizar 8 exitosas versiones, lo que nos ha permitido consolidarnos como referentes en el campo de la higiene ocupacional. Nuestro principal objetivo es brindarle a nuestros estudiantes una formación integral y de calidad, que les permita enfrentar los desafíos y exigencias del mundo laboral.
          
           
          
          Contamos con un equipo de profesionales altamente capacitados en cada una de las temáticas del programa, quienes estarán encantados de compartir sus conocimientos y experiencia con ustedes. Nuestro compromiso es garantizarles una educación de excelencia, que les permita adquirir las habilidades y competencias necesarias para desempeñarse de manera eficiente en el ámbito de la higiene ocupacional.
          
           
          
          Les invitamos a formar parte de nuestra comunidad académica y a aprovechar al máximo todas las oportunidades que nuestro programa tiene para ofrecerles. Estamos seguros de que esta experiencia será enriquecedora y les permitirá alcanzar sus metas profesionales.""",
          'prefix': '',
          'linkedin': '',
          'image':
            'https://educacioncontinua.usm.cl/wp-content/uploads/2023/01/boris-uribe.png',
        },
      ],
      'payment_methods': [
        {
          'id': 1,
          'value': 1000, 
          'method_type_name': 'Tarjeta de crédito',
        },
        
      ],
      'discounts': [
        {
          'id': 1,
          'discount_type_name': 'Inscripción temprana',
          'percent': '15%',
          'desciption': 'Descuento por inscripción temprana',
        },
        
      ],
    },
    
  ];
