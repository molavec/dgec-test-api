from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from datetime import date

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


class Section(BaseModel):
  NAME: str
  TEXT: str | None
  PUBLISH: str | None
  SEQ_NUMBER: int | None
  FILE_NAME: str | None
  BUTTON_TEXT: str | None
  LINK: str | None


class Director(BaseModel):
  ID: int
  PROGRAM_VERSIONS_ID: int
  PEOPLE_TYPES_ID: int
  NAME: str
  BANNER_SPRIDEN_ID: str
  FIRST_NAME: str
  LAST_NAME: str
  POSITION: str | None
  SOCIAL_MEDIA_LINK: str | None
  FILE_NAME: str | None
  BUTTON_TEXT: str | None
  TEXT: str | None


class Module(BaseModel):
  ID: int
  PROGRAM_PLANS_ID: int | None
  SEQ_NUMBER: int
  LEVEL_NUMBER: int | None
  DESCRIPTION: str | None
  HOURS: int | None
  SIGA_MNEMONIC: int | None
  SIGA_SCT_CREDIT: int | None
  SIGA_PLAN_LEVEL: int | None


class PaymentType(BaseModel):
  ID: int


class Requirement(BaseModel):
  ID: int
  PROGRAM_VERSIONS_ID: int
  REQUIREMENT_TYPES_ID: int
  NAME: str
  DESCRIPTION: str | None


class Discount(BaseModel):
  ID: int
  PROGRAM_VERSIONS_ID: int
  DISCOUNT_TYPES_ID: int
  NAME: str
  DESCRIPTION: str | None
  PERCENT: int | None
  OTRO_DESCUENTO: int | None


class Program(BaseModel):
  PROGRAM_ID: int
  PROGRAM_NAME: str
  PROGRAM_DESC: str
  SIGA_PROGRAM_CODE: int
  BANNER_PROGRAM_CODE: None
  BANNER_MAJR_CODE: None
  PROGRAM_TYPES_ID: int
  PROGRAM_TYPE_NAME: str
  PUBLISH: str
  IS_FEATURED: str | None
  SIGA_PLAN_NAME: str | None
  PROGRAM_VERSION_ID: int | None
  IMPART_TYPES_ID: int
  IMPART_TYPE_NAME: str
  MODALITY_TYPES_ID: int
  MODALITY_TYPE_NAME: str | None
  MODALITY_TYPE_DESC: str | None
  SIGA_COD_JORNADA: int
  SIGA_COD_SEDE: int
  SIGA_COD_DEPARTAMENTO: int
  MEMO_AUTHORIZATION: str | None
  NUMBER_VERSION: int
  START_DATE: str | None
  END_DATE: str | None
  DURATION_VALUE: int | None
  DURATION_TYPES_ID: int
  DURATION_TYPE_NAME: str | None
  DURATION_TEXT: str | None
  SIGA_PERIOD: str | None
  DGEC_CODE: str | None
  QUOTAS: int
  LEAST_ENROLLMENT_VALUE: int
  PROGRAM_AMOUNT: int
  REGISTRATION_AMOUNT: int
  BANNER_ORGN_CODE: int | None
  BANNER_DETAIL_CODE: int | None
  DISTRIBUTION_PERCENT: int | None
  DISCOUNT_TEXT: str | None
  RECORD_STATE: str | None
  SEND_DATE: str | None
  PROGRAM_VALIDATION_STATE: int
  VERSION_VALIDATION_STATE: int
  SECTIONS: list[Section] = []
  DIRECTORS: list[Director] = []
  MODULES: list[Module] = []
  PAYMENT_TYPES: list[PaymentType] = []
  REQUIREMENTS: list[Requirement] = []
  DISCOUNTS: list[Discount] = []


@app.get("/programs/")
async def programs() -> list[Program]:
  return programsData.programs


@app.get("/programs/{itemId}")
async def programs(itemId: int) -> Program:
  return programsData.program
