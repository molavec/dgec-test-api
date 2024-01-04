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
