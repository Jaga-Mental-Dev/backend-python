from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    with open(f"uploaded_files/{file.filename}", "wb") as buffer:
        buffer.write(await file.read())
    return {"filename": file.filename}

@app.get("/", response_class=HTMLResponse)
async def main():
    content = """
    <form action="/uploadfile/" method="post" enctype="multipart/form-data">
    <input name="file" type="file">
    <button type="submit">Upload</button>
    </form>
    """
    return HTMLResponse(content=content)
