from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from datetime import date, datetime

from pydantic import BaseModel

from .data import programs as programsData

app = FastAPI()

# HTML de inicio


@app.get("/", response_class=HTMLResponse)
async def root():
  return """
    <html>
      <head>
        <title>Test API</title>
        </head>
        <body>
            <h1>Hello Test API</h1>
            <p><a href="/docs">Puedes ver la documentación aquí</a></p>
        </body>
    </html>
"""


class PUBLISHED_SECTION(BaseModel):
  NAME: Union[str, None] = None
  TEXT: Union[str, None] = None
  PUBLISH: Union[str, None] = None
  SEQ_NUMBER: Union[int, None] = None
  FILE_NAME: Union[str, None] = None
  BUTTON_TEXT: Union[str, None] = None
  LINK: Union[str, None] = None


class PUBLISHED_DIRECTOR(BaseModel):
  ID: Union[int, None] = None
  PROGRAM_VERSIONS_ID: Union[int, None] = None
  PEOPLE_TYPES_ID: Union[int, None] = None
  NAME: Union[str, None] = None
  BANNER_SPRIDEN_ID: Union[str, None] = None
  FIRST_NAME: Union[str, None] = None
  LAST_NAME: Union[str, None] = None
  POSITION: Union[str, None] = None
  SOCIAL_MEDIA_LINK: Union[str, None] = None
  FILE_NAME: Union[str, None] = None
  BUTTON_TEXT: Union[str, None] = None
  TEXT: Union[str, None] = None


# For Published Programs
class PUBLISHED_MODULE(BaseModel):
  ID: Union[int, None] = None
  PROGRAM_PLANS_ID: Union[int, None] = None
  SEQ_NUMBER: Union[int, None] = None
  LEVEL_NUMBER: Union[str, None] = None
  DESCRIPTION: Union[str, None] = None
  HOURS: Union[int, None] = None
  SIGA_MNEMONIC: Union[str, None] = None
  SIGA_SCT_CREDIT: Union[int, None] = None
  SIGA_PLAN_LEVEL: Union[int, None] = None


class PUBLISHED_DISCOUNT(BaseModel):
  ID: Union[int, None] = None
  PROGRAM_VERSIONS_ID: Union[int, None] = None
  DISCOUNT_TYPES_ID: Union[int, None] = None
  NAME: Union[str, None] = None
  DESCRIPTION: Union[str, None] = None
  PERCENT: Union[int, None] = None
  OTRO_DESCUENTO: Union[str, None] = None


class PUBLISHED_PAYMENT_TYPE(BaseModel):
  ID: Union[int, None] = None
  PROGRAM_VERSIONS_ID: Union[int, None] = None
  PAYMENT_TYPES_ID: Union[int, None] = None
  NAME: Union[str, None] = None
  VALUE: Union[int, None] = None


class PUBLISHED_REQUIREMENT(BaseModel):
  ID: Union[int, None] = None
  PROGRAM_VERSIONS_ID: Union[int, None] = None
  REQUIREMENT_TYPES_ID: Union[int, None] = None
  NAME: Union[str, None] = None
  DESCRIPTION: Union[str, None] = None


class PROGRAM(BaseModel):
  PROGRAM_ID: Union[int, None] = None
  PROGRAM_NAME: Union[str, None] = None
  PROGRAM_DESC: Union[str, None] = None
  SIGA_PROGRAM_CODE: Union[int, None] = None
  BANNER_PROGRAM_CODE: Union[str, None] = None
  BANNER_MAJR_CODE: Union[str, None] = None
  PROGRAM_TYPES_ID: Union[int, None] = None
  PROGRAM_TYPE_NAME: Union[str, None] = None
  PUBLISH: Union[str, None] = None
  IS_FEATURED: Union[str, None] = None
  SIGA_PLAN_NAME: Union[str, None] = None
  PROGRAM_VERSION_ID: Union[int, None] = None
  IMPART_TYPES_ID: Union[int, None] = None
  IMPART_TYPE_NAME: Union[str, None] = None
  MODALITY_TYPES_ID: Union[int, None] = None
  MODALITY_TYPE_NAME: Union[str, None] = None
  MODALITY_TYPE_DESC: Union[str, None] = None
  SIGA_COD_JORNADA: Union[int, None] = None
  SIGA_COD_SEDE: Union[int, None] = None
  SIGA_COD_DEPARTAMENTO: Union[int, None] = None
  MEMO_AUTHORIZATION: Union[str, None] = None
  NUMBER_VERSION: Union[int, None] = None
  START_DATE: Union[datetime, None] = None
  END_DATE: Union[datetime, None] = None
  DURATION_VALUE: Union[int, None] = None
  DURATION_TYPES_ID: Union[int, None] = None
  DURATION_TYPE_NAME: Union[str, None] = None
  DURATION_TEXT: Union[str, None] = None
  SIGA_PERIOD: Union[str, None] = None
  DGEC_CODE: Union[str, None] = None
  QUOTAS: Union[int, None] = None
  LEAST_ENROLLMENT_VALUE: Union[int, None] = None
  PROGRAM_AMOUNT: Union[int, None] = None
  REGISTRATION_AMOUNT: Union[int, None] = None
  BANNER_ORGN_CODE: Union[str, None] = None
  BANNER_DETAIL_CODE: Union[str, None] = None
  DISTRIBUTION_PERCENT: Union[str, None] = None
  DISCOUNT_TEXT: Union[str, None] = None
  RECORD_STATE: Union[str, None] = None
  SEND_DATE: Union[datetime, None] = None
  PROGRAM_VALIDATION_STATE: Union[int, None] = None
  VERSION_VALIDATION_STATE: Union[int, None] = None
  SECTIONS: Union[list[PUBLISHED_SECTION], None] = None
  DIRECTORS: Union[list[PUBLISHED_DIRECTOR], None] = None
  MODULES: Union[list[PUBLISHED_MODULE], None] = None
  PAYMENT_TYPES: Union[list[PUBLISHED_PAYMENT_TYPE], None] = None
  REQUIREMENTS: Union[list[PUBLISHED_REQUIREMENT], None] = None
  DISCOUNTS: Union[list[PUBLISHED_DISCOUNT], None] = None


@app.get("/programs/published")
async def programs(type: int = 0) -> list[PROGRAM]:
  if type == 1:
    return programsData.courses
  else:
    return programsData.diplomas


@app.get("/program/published/{itemId}")
async def programs() -> PROGRAM:
  return programsData.program


@app.get("/campuses")
async def campuses():
  campuses = [
      {
          "COD_SEDE": 1,
          "NOM_SEDE": "Casa Central Valparaíso"
      },
      {
          "COD_SEDE": 4,
          "NOM_SEDE": "Concepción  "
      },
      {
          "COD_SEDE": 7,
          "NOM_SEDE": "Santiago San Joaquín"
      },
      {
          "COD_SEDE": 2,
          "NOM_SEDE": "Santiago Vitacura"
      },
      {
          "COD_SEDE": 3,
          "NOM_SEDE": "Viña del Mar  "
      }
  ]
  return campuses


@app.get("/deparments")
async def deparments():
  deparments = [
      {
          "COD_DEPARTAMENTO": 103,
          "NOM_DEPARTAMENTO": "AERONÁUTICA"
      },
      {
          "COD_DEPARTAMENTO": 16,
          "NOM_DEPARTAMENTO": "ARQUITECTURA"
      },
      {
          "COD_DEPARTAMENTO": 20,
          "NOM_DEPARTAMENTO": "BIOTECNOLOGIA"
      },
      {
          "COD_DEPARTAMENTO": 313,
          "NOM_DEPARTAMENTO": "CIENCIAS, Concepción"
      },
      {
          "COD_DEPARTAMENTO": 225,
          "NOM_DEPARTAMENTO": "CIENCIAS, Viña del Mar"
      },
      {
          "COD_DEPARTAMENTO": 255,
          "NOM_DEPARTAMENTO": "CONSTRUCCIÓN Y PREVENCIÓN DE RIESGOS, Concepción"
      },
      {
          "COD_DEPARTAMENTO": 209,
          "NOM_DEPARTAMENTO": "CONSTRUCCIÓN Y PREVENCIÓN DE RIESGOS, Viña del Mar"
      },
      {
          "COD_DEPARTAMENTO": 41,
          "NOM_DEPARTAMENTO": "DEFIDER"
      },
      {
          "COD_DEPARTAMENTO": 114,
          "NOM_DEPARTAMENTO": "DIREC. GRAL. DE INVESTIG. INNOV. Y EMPRENDIMIENTO"
      },
      {
          "COD_DEPARTAMENTO": 9,
          "NOM_DEPARTAMENTO": "DIRECCION GENERAL DE DOCENCIA"
      },
      {
          "COD_DEPARTAMENTO": 320,
          "NOM_DEPARTAMENTO": "DIRECCIÓN ACADÉMICA"
      },
      {
          "COD_DEPARTAMENTO": 45,
          "NOM_DEPARTAMENTO": "DIRECCIÓN DE ENSEÑANZA Y APRENDIZAJE"
      },
      {
          "COD_DEPARTAMENTO": 94,
          "NOM_DEPARTAMENTO": "DIRECCIÓN DE ESTUDIOS"
      },
      {
          "COD_DEPARTAMENTO": 25,
          "NOM_DEPARTAMENTO": "DIRECCIÓN DE POSTGRADO Y PROGRAMAS"
      },
      {
          "COD_DEPARTAMENTO": 101,
          "NOM_DEPARTAMENTO": "DIRECCIÓN GENERAL DE ASISTENCIA TÉCNICA"
      },
      {
          "COD_DEPARTAMENTO": 226,
          "NOM_DEPARTAMENTO": "DISEÑO Y MANUFACTURA"
      },
      {
          "COD_DEPARTAMENTO": 256,
          "NOM_DEPARTAMENTO": "ELECTRICIDAD"
      },
      {
          "COD_DEPARTAMENTO": 210,
          "NOM_DEPARTAMENTO": "ELECTROTECNIA E INFORMÁTICA"
      },
      {
          "COD_DEPARTAMENTO": 12,
          "NOM_DEPARTAMENTO": "ELECTRÓNICA"
      },
      {
          "COD_DEPARTAMENTO": 257,
          "NOM_DEPARTAMENTO": "ELECTRÓNICA E INFORMÁTICA"
      },
      {
          "COD_DEPARTAMENTO": 31,
          "NOM_DEPARTAMENTO": "ESTUDIOS HUMANÍSTICOS"
      },
      {
          "COD_DEPARTAMENTO": 21,
          "NOM_DEPARTAMENTO": "FÍSICA"
      },
      {
          "COD_DEPARTAMENTO": 15,
          "NOM_DEPARTAMENTO": "INDUSTRIAS"
      },
      {
          "COD_DEPARTAMENTO": 18,
          "NOM_DEPARTAMENTO": "INFORMÁTICA"
      },
      {
          "COD_DEPARTAMENTO": 26,
          "NOM_DEPARTAMENTO": "INGENIERÍA COMERCIAL"
      },
      {
          "COD_DEPARTAMENTO": 13,
          "NOM_DEPARTAMENTO": "INGENIERÍA ELÉCTRICA"
      },
      {
          "COD_DEPARTAMENTO": 112,
          "NOM_DEPARTAMENTO": "INGENIERÍA EN DISEÑO"
      },
      {
          "COD_DEPARTAMENTO": 14,
          "NOM_DEPARTAMENTO": "INGENIERÍA MECÁNICA"
      },
      {
          "COD_DEPARTAMENTO": 17,
          "NOM_DEPARTAMENTO": "INGENIERÍA METALÚRGICA Y DE MATERIALES"
      },
      {
          "COD_DEPARTAMENTO": 19,
          "NOM_DEPARTAMENTO": "INGENIERÍA QUÍMICA Y AMBIENTAL"
      },
      {
          "COD_DEPARTAMENTO": 49,
          "NOM_DEPARTAMENTO": "INSTITUTO INTERNACIONAL PARA LA INNOVACIÓN EMPRESA"
      },
      {
          "COD_DEPARTAMENTO": 22,
          "NOM_DEPARTAMENTO": "MATEMÁTICA"
      },
      {
          "COD_DEPARTAMENTO": 258,
          "NOM_DEPARTAMENTO": "MECÁNICA, Concepción"
      },
      {
          "COD_DEPARTAMENTO": 204,
          "NOM_DEPARTAMENTO": "MECÁNICA, Viña del Mar"
      },
      {
          "COD_DEPARTAMENTO": 11,
          "NOM_DEPARTAMENTO": "OBRAS CIVILES"
      },
      {
          "COD_DEPARTAMENTO": 51,
          "NOM_DEPARTAMENTO": "PROMOCIÓN UNIVERSITARIA"
      },
      {
          "COD_DEPARTAMENTO": 23,
          "NOM_DEPARTAMENTO": "QUÍMICA"
      },
      {
          "COD_DEPARTAMENTO": 259,
          "NOM_DEPARTAMENTO": "QUÍMICA Y MEDIO AMBIENTE, Concepción"
      },
      {
          "COD_DEPARTAMENTO": 211,
          "NOM_DEPARTAMENTO": "QUÍMICA Y MEDIO AMBIENTE, Viña del Mar"
      },
      {
          "COD_DEPARTAMENTO": 206,
          "NOM_DEPARTAMENTO": "SECRETARÍA ACADÉMICA"
      },
      {
          "COD_DEPARTAMENTO": 316,
          "NOM_DEPARTAMENTO": "SIDERO METAL CONCEPCIÓN"
      },
      {
          "COD_DEPARTAMENTO": 317,
          "NOM_DEPARTAMENTO": "TÉCNICA CONCEPCIÓN"
      },
      {
          "COD_DEPARTAMENTO": 319,
          "NOM_DEPARTAMENTO": "UNIDAD DE PROGRAMAS ESPECIALES"
      },
      {
          "COD_DEPARTAMENTO": 10,
          "NOM_DEPARTAMENTO": "VICERREACTORÍA ACADÉMICA"
      }
  ]
  return deparments


@app.get("/diu_vesp")
async def diuVesp():
  jornada = [
      {
          "COD_JORNADA": 1,
          "NOM_JORNADA": "Diurno"
      },
      {
          "COD_JORNADA": 2,
          "NOM_JORNADA": "Vespertino"
      }
  ]
  return jornada


@app.get("/modalities")
async def modalities():
  modalities = [
      {
          "ID": 1,
          "NAME": "Profesional"
      },
      {
          "ID": 2,
          "NAME": "Online"
      },
      {
          "ID": 3,
          "NAME": "Híbrida"
      }
  ]
  return modalities
