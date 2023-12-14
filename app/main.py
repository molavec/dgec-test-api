from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import ORJSONResponse

from .data import programs as programsData

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
  return """
    <html>
      <head>
        <title>Test API</title>
        </head>
        <body>
            <h1>Hello Test API</h1>
        </body>
    </html>
"""


@app.get("/programs/", response_class=ORJSONResponse)
async def programs():
  return ORJSONResponse(programsData.programs)

@app.get("/programs/{itemId}", response_class=ORJSONResponse)
async def programs(itemId: int):
  return ORJSONResponse(*[d for d in programsData.programs if d['id'] in [itemId]])