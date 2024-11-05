from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse
import tensorflow as tf
from tensorflow.keras.models import load_model

app = FastAPI()

try:
    model = load_model('./ai_models/model.h5')
except Exception as e:
    raise RuntimeError("failed model nya tidak diload" + str(e))

async def preprocess_image(image_data: bytes) -> tf.Tensor:
    image = tf.io.decode_image(image_data, channels=1)  
    image = tf.image.resize(image, [48, 48])         
    image = tf.cast(image, tf.float32) / 255.0    
    image_tensor = tf.expand_dims(image, axis=0)
    return image_tensor


@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    try:
        file_data = await file.read()
        image_tensor = await preprocess_image(file_data)
        prediction = model.predict(image_tensor)
        return JSONResponse(content={"filename": file.filename, "prediction": prediction.tolist()})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Prediction error: " + str(e))



@app.get("/", response_class=HTMLResponse)
async def main():
    content = """
    <form action="/uploadfile/" method="post" enctype="multipart/form-data">
    <input name="file" type="file">
    <button type="submit">Upload</button>
    </form>
    """
    return HTMLResponse(content=content)
