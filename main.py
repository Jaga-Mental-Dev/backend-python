from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from app.routes import image_classification
from fastapi import FastAPI
import numpy as np

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import tensorflow as tf

app = FastAPI()

app.include_router(image_classification.router)


def preprosesing(image_data):
    image = tf.io.decode_image(image_data, channels=3)
    image = tf.image.resize(image, [120, 120])
    image = tf.cast(image, tf.float32) / 255.0
    image_tensor = tf.expand_dims(image, axis=0)
    return image_tensor


@app.post("/api/image")
async def create_upload_file(file: UploadFile = File(...)):

    image_data = await file.read()
    image_tensor = preprosesing(image_data)

    model = tf.keras.models.load_model(
        "model.h5")
    

    prediction = model.predict(image_tensor)

    if prediction.shape[1] == 1:  
        prediction = np.concatenate([1 - prediction, prediction], axis=-1)

    predicted_class = np.argmax(prediction, axis=-1)[0]  

    labels = ["Anjing", "Dost"]

    predicted_label = labels[predicted_class]
    
    percentage = prediction[0] * 100  
  
    return {
        "filename": file.filename,
        "predicted_class": predicted_label,
        "prediction_percentages": {
            labels[0]: f"{percentage[0]:.2f}%",  
            labels[1]: f"{percentage[1]:.2f}%"   
        },
        "prediction": prediction.tolist()
    }


@app.get("/", response_class=HTMLResponse)
async def main():
    content = """
    <form action="/api/image" method="post" enctype="multipart/form-data">
    <input name="file" type="file">
    <button type="submit">Upload</button>
    </form>
    """
    return HTMLResponse(content=content)
