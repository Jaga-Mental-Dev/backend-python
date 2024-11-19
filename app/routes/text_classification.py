from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import JSONResponse
from app.utils.text_preprocessing import preprocess_text
import tensorflow as tf
import os
import requests
import io
from dotenv import load_dotenv

router = APIRouter()

@router.post("/api/text")
async def create_text(text: str = Form(...)):
    try:
        
        MODEL_URL = "https://storage.googleapis.com/model_bucket/model.h5"
        
        response = requests.get(MODEL_URL)
        model_data = io.BytesIO(response.content)
       
        text_tensor = await preprocess_text(text)
        
        model = tf.keras.models.load_model(model_data)
            
        prediction = model.predict(text_tensor)
        prediction_list = prediction.tolist()
            
        return JSONResponse(content={"text": text, "prediction": prediction_list})
    except Exception as e:
        raise HTTPException(status_code=500, detail="Prediction error: " + str(e))