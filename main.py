from fastapi.responses import HTMLResponse
from app.api import image_routes, text_routes
from fastapi import FastAPI
import numpy as np

from fastapi.responses import JSONResponse

import os


app = FastAPI(
    title="Text & Image Classification API",
    description="API untuk klasifikasi teks dan gambar",
    version="1.0.0",
)


app.include_router(text_routes.router, prefix="/text", tags=["Text Classification"])
app.include_router(image_routes.router, prefix="/image", tags=["Image Classification"])


# @app.get("/", response_class=HTMLResponse)
# async def main():
#     content = """
#     <form action="/api/text" method="post">
#     <input name="text" type="text" placeholder="Masukkan teks">
#     <button type="submit">Submit</button>
#     </form>
#     """
#     return HTMLResponse(content=content)
