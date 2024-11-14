from fastapi.responses import HTMLResponse
from app.routes import image_classification
from app.routes import text_classification
from fastapi import FastAPI
import numpy as np

from fastapi.responses import JSONResponse
import tensorflow as tf
import os


app = FastAPI()

app.include_router(image_classification.router)
app.include_router(text_classification.router)


@app.get("/", response_class=HTMLResponse)
async def main():
    content = """
    <form action="/api/text" method="post">
    <input name="text" type="text" placeholder="Masukkan teks">
    <button type="submit">Submit</button>
    </form>
    """
    return HTMLResponse(content=content)
