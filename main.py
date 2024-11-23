from fastapi.responses import HTMLResponse
from app.api import image_routes, text_routes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np

from fastapi.responses import JSONResponse

import os


app = FastAPI(
    title="Text & Image Classification API",
    description="API untuk klasifikasi teks dan gambar",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
