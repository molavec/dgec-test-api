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
        "PROGRAM_ID": 23,
        "PROGRAM_NAME": "Diploma en Integridad Mecánica de Equipos Estáticos de Procesos Industriales",
        "PROGRAM_DESC": "(Estanques, Sistema de Piping, Dispositivos de Alivio)",
        "SIGA_PROGRAM_CODE": 271,
        "BANNER_PROGRAM_CODE": None,
        "BANNER_MAJR_CODE": None,
        "PROGRAM_TYPES_ID": 2,
        "PROGRAM_TYPE_NAME": "Diploma",
        "PUBLISH": "SI",
        "IS_FEATURED": "NO",
        "SIGA_PLAN_NAME": None,
        "PROGRAM_VERSION_ID": 23,
        "IMPART_TYPES_ID": 1,
        "IMPART_TYPE_NAME": "Abierto",
        "MODALITY_TYPES_ID": 1,
        "MODALITY_TYPE_NAME": "Profesional",
        "MODALITY_TYPE_DESC": None,
        "SIGA_COD_JORNADA": 1,
        "SIGA_COD_SEDE": 1,
        "SIGA_COD_DEPARTAMENTO": 21,
        "MEMO_AUTHORIZATION": None,
        "NUMBER_VERSION": 1,
        "START_DATE": "2023-12-22T00:00:00",
        "END_DATE": "2024-12-22T00:00:00",
        "DURATION_VALUE": 250,
        "DURATION_TYPES_ID": 1,
        "DURATION_TYPE_NAME": "Horas",
        "DURATION_TEXT": None,
        "SIGA_PERIOD": None,
        "DGEC_CODE": None,
        "QUOTAS": 0,
        "LEAST_ENROLLMENT_VALUE": 0,
        "PROGRAM_AMOUNT": 0,
        "REGISTRATION_AMOUNT": 0,
        "BANNER_ORGN_CODE": None,
        "BANNER_DETAIL_CODE": None,
        "DISTRIBUTION_PERCENT": None,
        "DISCOUNT_TEXT": None,
        "RECORD_STATE": "E",
        "SEND_DATE": "2023-12-27T09:26:27",
        "PROGRAM_VALIDATION_STATE": 1,
        "VERSION_VALIDATION_STATE": 1,
        "SECTIONS": [
            {
                "NAME": "Información General del Programa",
                "TEXT": "<p>La Integridad Mecánica de equipos es una filosofía de trabajo que tiene por objeto garantizar que todo equipo (de proceso, eléctrico, de instrumentación y control, seguridad, entre otros), sea diseñado, fabricado, instalado, operado, mantenido, y/o reemplazado oportunamente para prevenir fallas, accidentes o riesgos a personas, instalaciones y al ambiente, estableciendo los criterios basados en datos históricos, normas y regulaciones nacionales e internacionales.</p><p>&nbsp;</p><p>La Gestión de la integridad de equipos en los Procesos se puede definir como la aplicación metodológica de sistemas de gestión y de control, de una forma tal que todos los riesgos existentes y potenciales sean identificados, analizados, evaluados y controlados, con la finalidad de prevenir cualquier tipo de incidente que pueda afectar a los procesos.</p>",
                "PUBLISH": "SI",
                "SEQ_NUMBER": 2,
                "FILE_NAME": None,
                "BUTTON_TEXT": None,
                "LINK": None
            },
            {
                "NAME": "Objetivo General del Programa",
                "TEXT": "<ul><li>La integridad Mecánica es el proceso de garantizar que los equipos sean fabricados con los materiales adecuados de construcción y, además, sean correctamente instalados, mantenidos y reemplazados para evitar fallas y daños ambientales.</li><li>La existencia y aplicación de procedimientos escritos, que deben incluir métodos que faciliten que los empleados identifiquen y reporten equipos potencialmente defectuosos o inseguros y, además, que similarmente puedan registrar sus observaciones y sugerencias.</li><li>Establecer e implementar la correcta y completa formación de los empleados en todas las actividades de operación y mantenimiento.</li><li>El diseño de un programa de inspecciones y pruebas para todos los equipos de proceso. Estos procedimientos para inspecciones y pruebas deben seguir reconocidas y generalmente aceptadas buenas prácticas de ingeniería, con una frecuencia coherente con las recomendaciones del fabricante o según lo determine el historial de funcionamiento del equipo y su evaluación en función del riesgo.</li><li>La creación de un programa de aseguramiento de la calidad para comprobar la idoneidad de los equipos durante el proceso de construcción de la instalación, su modificación o reparación, su adecuada instalación y finalmente, la existencia de partes y repuestos que cumplan con códigos aplicables y especificaciones de diseño para el apropiado mantenimiento de dichos equipos.</li></ul>",
                "PUBLISH": "SI",
                "SEQ_NUMBER": 3,
                "FILE_NAME": None,
                "BUTTON_TEXT": None,
                "LINK": None
            },
            {
                "NAME": "A quién va Dirigido",
                "TEXT": "<p>El Diploma está dirigido a mantenedores, operadores, técnicos y profesionales de los diversos sectores industriales que se desempeñan en el área de mantenimiento y producción, y para todos aquellos interesados en la temática de integridad mecánica de equipos con la ayuda de los programas y planes mantenimiento predictivo/preventivo.</p>",
                "PUBLISH": "SI",
                "SEQ_NUMBER": 4,
                "FILE_NAME": None,
                "BUTTON_TEXT": None,
                "LINK": None
            },
            {
                "NAME": "Staff de Profesores",
                "TEXT": "<ul><li>Ing. Sr. Guillermo Larson M.</li><li>Ing. Sr. Marcelo Quiroz N.</li><li>Ing. Sr. Ariel Zoñez R.</li><li>Ing. Sr. Oscar Castro C.</li></ul>",
                "PUBLISH": "SI",
                "SEQ_NUMBER": 7,
                "FILE_NAME": None,
                "BUTTON_TEXT": None,
                "LINK": None
            },
            {
                "NAME": "Proceso de Admisión",
                "TEXT": "<p>Para más información de admisión, escribir a educacion.continua@usm.cl</p>",
                "PUBLISH": "SI",
                "SEQ_NUMBER": 8,
                "FILE_NAME": None,
                "BUTTON_TEXT": None,
                "LINK": None
            },
            {
                "NAME": "Más información",
                "TEXT": "pamela.araya@usm.cl",
                "PUBLISH": "SI",
                "SEQ_NUMBER": 9,
                "FILE_NAME": None,
                "BUTTON_TEXT": None,
                "LINK": None
            },
            {
                "NAME": "Lugar",
                "TEXT": "Plataforma Zoom",
                "PUBLISH": "SI",
                "SEQ_NUMBER": 10,
                "FILE_NAME": None,
                "BUTTON_TEXT": None,
                "LINK": None
            }
        ],
        "DIRECTORS": [
            {
                "ID": 1,
                "PROGRAM_VERSIONS_ID": 23,
                "PEOPLE_TYPES_ID": 1,
                "NAME": "Director de Programa",
                "BANNER_SPRIDEN_ID": "92601862",
                "FIRST_NAME": "Marcelo",
                "LAST_NAME": "Quiroz Neira",
                "POSITION": None,
                "SOCIAL_MEDIA_LINK": None,
                "FILE_NAME": None,
                "BUTTON_TEXT": None,
                "TEXT": "<p>El mantenimiento es una de las actividades que influye directamente en la producción, en los costos globales de la actividad productiva, en los clientes, en la seguridad y en el medio ambiente.</p><p>&nbsp;</p><p>La integridad Mecánica es el proceso de garantizar que los equipos sean fabricados con los materiales adecuados de construcción y, además, sean correctamente instalados, mantenidos y reemplazados para evitar fallas y daños ambientales.</p>"
            },
            {
                "ID": 2,
                "PROGRAM_VERSIONS_ID": 23,
                "PEOPLE_TYPES_ID": 1,
                "NAME": "Director de Programa",
                "BANNER_SPRIDEN_ID": "150969441",
                "FIRST_NAME": "Catherine",
                "LAST_NAME": "Tessini",
                "POSITION": None,
                "SOCIAL_MEDIA_LINK": None,
                "FILE_NAME": None,
                "BUTTON_TEXT": None,
                "TEXT": "<p>PRUEBA 2: El mantenimiento es una de las actividades que influye directamente en la producción, en los costos globales de la actividad productiva, en los clientes, en la seguridad y en el medio ambiente.</p><p>&nbsp;</p><p>La integridad Mecánica es el proceso de garantizar que los equipos sean fabricados con los materiales adecuados de construcción y, además, sean correctamente instalados, mantenidos y reemplazados para evitar fallas y daños ambientales.</p>"
            }
        ],
        "MODULES": [
            {
                "ID": 1,
                "PROGRAM_PLANS_ID": None,
                "SEQ_NUMBER": 1,
                "LEVEL_NUMBER": None,
                "DESCRIPTION": None,
                "HOURS": 5,
                "SIGA_MNEMONIC": None,
                "SIGA_SCT_CREDIT": None,
                "SIGA_PLAN_LEVEL": None
            },
            {
                "ID": 3,
                "PROGRAM_PLANS_ID": None,
                "SEQ_NUMBER": 3,
                "LEVEL_NUMBER": None,
                "DESCRIPTION": None,
                "HOURS": 40,
                "SIGA_MNEMONIC": None,
                "SIGA_SCT_CREDIT": None,
                "SIGA_PLAN_LEVEL": None
            },
            {
                "ID": 4,
                "PROGRAM_PLANS_ID": None,
                "SEQ_NUMBER": 4,
                "LEVEL_NUMBER": None,
                "DESCRIPTION": None,
                "HOURS": 40,
                "SIGA_MNEMONIC": None,
                "SIGA_SCT_CREDIT": None,
                "SIGA_PLAN_LEVEL": None
            },
            {
                "ID": 5,
                "PROGRAM_PLANS_ID": None,
                "SEQ_NUMBER": 5,
                "LEVEL_NUMBER": None,
                "DESCRIPTION": None,
                "HOURS": 40,
                "SIGA_MNEMONIC": None,
                "SIGA_SCT_CREDIT": None,
                "SIGA_PLAN_LEVEL": None
            },
            {
                "ID": 6,
                "PROGRAM_PLANS_ID": None,
                "SEQ_NUMBER": 6,
                "LEVEL_NUMBER": None,
                "DESCRIPTION": None,
                "HOURS": 30,
                "SIGA_MNEMONIC": None,
                "SIGA_SCT_CREDIT": None,
                "SIGA_PLAN_LEVEL": None
            }
        ],
        "PAYMENT_TYPES": [],
        "REQUIREMENTS": [
            {
                "ID": 1,
                "PROGRAM_VERSIONS_ID": 23,
                "REQUIREMENT_TYPES_ID": 1,
                "NAME": "CI",
                "DESCRIPTION": "copia de cédula de identidad ambos lados"
            },
            {
                "ID": 3,
                "PROGRAM_VERSIONS_ID": 23,
                "REQUIREMENT_TYPES_ID": 2,
                "NAME": "CV",
                "DESCRIPTION": "actualizado"
            },
            {
                "ID": 2,
                "PROGRAM_VERSIONS_ID": 23,
                "REQUIREMENT_TYPES_ID": 11,
                "NAME": "Copia Título Profesional carrera mínimo 4 semestres,",
                "DESCRIPTION": None
            }
        ],
        "DISCOUNTS": [
            {
                "ID": 4,
                "PROGRAM_VERSIONS_ID": 23,
                "DISCOUNT_TYPES_ID": 9,
                "NAME": "Académicos, docentes, funcionarios USM",
                "DESCRIPTION": None,
                "PERCENT": 10,
                "OTRO_DESCUENTO": None
            },
            {
                "ID": 1,
                "PROGRAM_VERSIONS_ID": 23,
                "DISCOUNT_TYPES_ID": 7,
                "NAME": "Alumnos y ex alumnos Departamento Mecánica USM Sede Concepción",
                "DESCRIPTION": None,
                "PERCENT": 20,
                "OTRO_DESCUENTO": None
            },
            {
                "ID": 2,
                "PROGRAM_VERSIONS_ID": 23,
                "DISCOUNT_TYPES_ID": 8,
                "NAME": "Descuento inscripción durante julio/agosto",
                "DESCRIPTION": None,
                "PERCENT": 10,
                "OTRO_DESCUENTO": None
            },
            {
                "ID": 3,
                "PROGRAM_VERSIONS_ID": 23,
                "DISCOUNT_TYPES_ID": 1,
                "NAME": "Ex-Alumnos USM",
                "DESCRIPTION": "ser exalumno de la Universidad, cualquier título, grado o diplomas",
                "PERCENT": 10,
                "OTRO_DESCUENTO": None
            },
            {
                "ID": 5,
                "PROGRAM_VERSIONS_ID": 23,
                "DISCOUNT_TYPES_ID": 10,
                "NAME": "Pago contado",
                "DESCRIPTION": None,
                "PERCENT": 10,
                "OTRO_DESCUENTO": None
            }
        ]
    }

]


program = {
    "PROGRAM_ID": 23,
    "PROGRAM_NAME": "Diploma en Integridad Mecánica de Equipos Estáticos de Procesos Industriales",
    "PROGRAM_DESC": "(Estanques, Sistema de Piping, Dispositivos de Alivio)",
    "SIGA_PROGRAM_CODE": 271,
    "BANNER_PROGRAM_CODE": None,
    "BANNER_MAJR_CODE": None,
    "PROGRAM_TYPES_ID": 2,
    "PROGRAM_TYPE_NAME": "Diploma",
    "PUBLISH": "SI",
    "IS_FEATURED": "NO",
    "SIGA_PLAN_NAME": None,
    "PROGRAM_VERSION_ID": 23,
    "IMPART_TYPES_ID": 1,
    "IMPART_TYPE_NAME": "Abierto",
    "MODALITY_TYPES_ID": 1,
    "MODALITY_TYPE_NAME": "Profesional",
    "MODALITY_TYPE_DESC": None,
    "SIGA_COD_JORNADA": 1,
    "SIGA_COD_SEDE": 1,
    "SIGA_COD_DEPARTAMENTO": 21,
    "MEMO_AUTHORIZATION": None,
    "NUMBER_VERSION": 1,
    "START_DATE": "2023-12-22T00:00:00",
    "END_DATE": "2024-12-22T00:00:00",
    "DURATION_VALUE": 250,
    "DURATION_TYPES_ID": 1,
    "DURATION_TYPE_NAME": "Horas",
    "DURATION_TEXT": None,
    "SIGA_PERIOD": None,
    "DGEC_CODE": None,
    "QUOTAS": 0,
    "LEAST_ENROLLMENT_VALUE": 0,
    "PROGRAM_AMOUNT": 0,
    "REGISTRATION_AMOUNT": 0,
    "BANNER_ORGN_CODE": None,
    "BANNER_DETAIL_CODE": None,
    "DISTRIBUTION_PERCENT": None,
    "DISCOUNT_TEXT": None,
    "RECORD_STATE": "E",
    "SEND_DATE": "2023-12-27T09:26:27",
    "PROGRAM_VALIDATION_STATE": 1,
    "VERSION_VALIDATION_STATE": 1,
    "SECTIONS": [
        {
            "NAME": "Información General del Programa",
            "TEXT": "<p>La Integridad Mecánica de equipos es una filosofía de trabajo que tiene por objeto garantizar que todo equipo (de proceso, eléctrico, de instrumentación y control, seguridad, entre otros), sea diseñado, fabricado, instalado, operado, mantenido, y/o reemplazado oportunamente para prevenir fallas, accidentes o riesgos a personas, instalaciones y al ambiente, estableciendo los criterios basados en datos históricos, normas y regulaciones nacionales e internacionales.</p><p>&nbsp;</p><p>La Gestión de la integridad de equipos en los Procesos se puede definir como la aplicación metodológica de sistemas de gestión y de control, de una forma tal que todos los riesgos existentes y potenciales sean identificados, analizados, evaluados y controlados, con la finalidad de prevenir cualquier tipo de incidente que pueda afectar a los procesos.</p>",
            "PUBLISH": "SI",
            "SEQ_NUMBER": 2,
            "FILE_NAME": None,
            "BUTTON_TEXT": None,
            "LINK": None
        },
        {
            "NAME": "Objetivo General del Programa",
            "TEXT": "<ul><li>La integridad Mecánica es el proceso de garantizar que los equipos sean fabricados con los materiales adecuados de construcción y, además, sean correctamente instalados, mantenidos y reemplazados para evitar fallas y daños ambientales.</li><li>La existencia y aplicación de procedimientos escritos, que deben incluir métodos que faciliten que los empleados identifiquen y reporten equipos potencialmente defectuosos o inseguros y, además, que similarmente puedan registrar sus observaciones y sugerencias.</li><li>Establecer e implementar la correcta y completa formación de los empleados en todas las actividades de operación y mantenimiento.</li><li>El diseño de un programa de inspecciones y pruebas para todos los equipos de proceso. Estos procedimientos para inspecciones y pruebas deben seguir reconocidas y generalmente aceptadas buenas prácticas de ingeniería, con una frecuencia coherente con las recomendaciones del fabricante o según lo determine el historial de funcionamiento del equipo y su evaluación en función del riesgo.</li><li>La creación de un programa de aseguramiento de la calidad para comprobar la idoneidad de los equipos durante el proceso de construcción de la instalación, su modificación o reparación, su adecuada instalación y finalmente, la existencia de partes y repuestos que cumplan con códigos aplicables y especificaciones de diseño para el apropiado mantenimiento de dichos equipos.</li></ul>",
            "PUBLISH": "SI",
            "SEQ_NUMBER": 3,
            "FILE_NAME": None,
            "BUTTON_TEXT": None,
            "LINK": None
        },
        {
            "NAME": "A quién va Dirigido",
            "TEXT": "<p>El Diploma está dirigido a mantenedores, operadores, técnicos y profesionales de los diversos sectores industriales que se desempeñan en el área de mantenimiento y producción, y para todos aquellos interesados en la temática de integridad mecánica de equipos con la ayuda de los programas y planes mantenimiento predictivo/preventivo.</p>",
            "PUBLISH": "SI",
            "SEQ_NUMBER": 4,
            "FILE_NAME": None,
            "BUTTON_TEXT": None,
            "LINK": None
        },
        {
            "NAME": "Staff de Profesores",
            "TEXT": "<ul><li>Ing. Sr. Guillermo Larson M.</li><li>Ing. Sr. Marcelo Quiroz N.</li><li>Ing. Sr. Ariel Zoñez R.</li><li>Ing. Sr. Oscar Castro C.</li></ul>",
            "PUBLISH": "SI",
            "SEQ_NUMBER": 7,
            "FILE_NAME": None,
            "BUTTON_TEXT": None,
            "LINK": None
        },
        {
            "NAME": "Proceso de Admisión",
            "TEXT": "<p>Para más información de admisión, escribir a educacion.continua@usm.cl</p>",
            "PUBLISH": "SI",
            "SEQ_NUMBER": 8,
            "FILE_NAME": None,
            "BUTTON_TEXT": None,
            "LINK": None
        },
        {
            "NAME": "Más información",
            "TEXT": "pamela.araya@usm.cl",
            "PUBLISH": "SI",
            "SEQ_NUMBER": 9,
            "FILE_NAME": None,
            "BUTTON_TEXT": None,
            "LINK": None
        },
        {
            "NAME": "Lugar",
            "TEXT": "Plataforma Zoom",
            "PUBLISH": "SI",
            "SEQ_NUMBER": 10,
            "FILE_NAME": None,
            "BUTTON_TEXT": None,
            "LINK": None
        }
    ],
    "DIRECTORS": [
        {
            "ID": 1,
            "PROGRAM_VERSIONS_ID": 23,
            "PEOPLE_TYPES_ID": 1,
            "NAME": "Director de Programa",
            "BANNER_SPRIDEN_ID": "92601862",
            "FIRST_NAME": "Marcelo",
            "LAST_NAME": "Quiroz Neira",
            "POSITION": None,
            "SOCIAL_MEDIA_LINK": None,
            "FILE_NAME": None,
            "BUTTON_TEXT": None,
            "TEXT": "<p>El mantenimiento es una de las actividades que influye directamente en la producción, en los costos globales de la actividad productiva, en los clientes, en la seguridad y en el medio ambiente.</p><p>&nbsp;</p><p>La integridad Mecánica es el proceso de garantizar que los equipos sean fabricados con los materiales adecuados de construcción y, además, sean correctamente instalados, mantenidos y reemplazados para evitar fallas y daños ambientales.</p>"
        },
        {
            "ID": 2,
            "PROGRAM_VERSIONS_ID": 23,
            "PEOPLE_TYPES_ID": 1,
            "NAME": "Director de Programa",
            "BANNER_SPRIDEN_ID": "150969441",
            "FIRST_NAME": "Catherine",
            "LAST_NAME": "Tessini",
            "POSITION": None,
            "SOCIAL_MEDIA_LINK": None,
            "FILE_NAME": None,
            "BUTTON_TEXT": None,
            "TEXT": "<p>PRUEBA 2: El mantenimiento es una de las actividades que influye directamente en la producción, en los costos globales de la actividad productiva, en los clientes, en la seguridad y en el medio ambiente.</p><p>&nbsp;</p><p>La integridad Mecánica es el proceso de garantizar que los equipos sean fabricados con los materiales adecuados de construcción y, además, sean correctamente instalados, mantenidos y reemplazados para evitar fallas y daños ambientales.</p>"
        }
    ],
    "MODULES": [
        {
            "ID": 1,
            "PROGRAM_PLANS_ID": None,
            "SEQ_NUMBER": 1,
            "LEVEL_NUMBER": None,
            "DESCRIPTION": None,
            "HOURS": 5,
            "SIGA_MNEMONIC": None,
            "SIGA_SCT_CREDIT": None,
            "SIGA_PLAN_LEVEL": None
        },
        {
            "ID": 3,
            "PROGRAM_PLANS_ID": None,
            "SEQ_NUMBER": 3,
            "LEVEL_NUMBER": None,
            "DESCRIPTION": None,
            "HOURS": 40,
            "SIGA_MNEMONIC": None,
            "SIGA_SCT_CREDIT": None,
            "SIGA_PLAN_LEVEL": None
        },
        {
            "ID": 4,
            "PROGRAM_PLANS_ID": None,
            "SEQ_NUMBER": 4,
            "LEVEL_NUMBER": None,
            "DESCRIPTION": None,
            "HOURS": 40,
            "SIGA_MNEMONIC": None,
            "SIGA_SCT_CREDIT": None,
            "SIGA_PLAN_LEVEL": None
        },
        {
            "ID": 5,
            "PROGRAM_PLANS_ID": None,
            "SEQ_NUMBER": 5,
            "LEVEL_NUMBER": None,
            "DESCRIPTION": None,
            "HOURS": 40,
            "SIGA_MNEMONIC": None,
            "SIGA_SCT_CREDIT": None,
            "SIGA_PLAN_LEVEL": None
        },
        {
            "ID": 6,
            "PROGRAM_PLANS_ID": None,
            "SEQ_NUMBER": 6,
            "LEVEL_NUMBER": None,
            "DESCRIPTION": None,
            "HOURS": 30,
            "SIGA_MNEMONIC": None,
            "SIGA_SCT_CREDIT": None,
            "SIGA_PLAN_LEVEL": None
        }
    ],
    "PAYMENT_TYPES": [],
    "REQUIREMENTS": [
        {
            "ID": 1,
            "PROGRAM_VERSIONS_ID": 23,
            "REQUIREMENT_TYPES_ID": 1,
            "NAME": "CI",
            "DESCRIPTION": "copia de cédula de identidad ambos lados"
        },
        {
            "ID": 3,
            "PROGRAM_VERSIONS_ID": 23,
            "REQUIREMENT_TYPES_ID": 2,
            "NAME": "CV",
            "DESCRIPTION": "actualizado"
        },
        {
            "ID": 2,
            "PROGRAM_VERSIONS_ID": 23,
            "REQUIREMENT_TYPES_ID": 11,
            "NAME": "Copia Título Profesional carrera mínimo 4 semestres,",
            "DESCRIPTION": None
        }
    ],
    "DISCOUNTS": [
        {
            "ID": 4,
            "PROGRAM_VERSIONS_ID": 23,
            "DISCOUNT_TYPES_ID": 9,
            "NAME": "Académicos, docentes, funcionarios USM",
            "DESCRIPTION": None,
            "PERCENT": 10,
            "OTRO_DESCUENTO": None
        },
        {
            "ID": 1,
            "PROGRAM_VERSIONS_ID": 23,
            "DISCOUNT_TYPES_ID": 7,
            "NAME": "Alumnos y ex alumnos Departamento Mecánica USM Sede Concepción",
            "DESCRIPTION": None,
            "PERCENT": 20,
            "OTRO_DESCUENTO": None
        },
        {
            "ID": 2,
            "PROGRAM_VERSIONS_ID": 23,
            "DISCOUNT_TYPES_ID": 8,
            "NAME": "Descuento inscripción durante julio/agosto",
            "DESCRIPTION": None,
            "PERCENT": 10,
            "OTRO_DESCUENTO": None
        },
        {
            "ID": 3,
            "PROGRAM_VERSIONS_ID": 23,
            "DISCOUNT_TYPES_ID": 1,
            "NAME": "Ex-Alumnos USM",
            "DESCRIPTION": "ser exalumno de la Universidad, cualquier título, grado o diplomas",
            "PERCENT": 10,
            "OTRO_DESCUENTO": None
        },
        {
            "ID": 5,
            "PROGRAM_VERSIONS_ID": 23,
            "DISCOUNT_TYPES_ID": 10,
            "NAME": "Pago contado",
            "DESCRIPTION": None,
            "PERCENT": 10,
            "OTRO_DESCUENTO": None
        }
    ]
}