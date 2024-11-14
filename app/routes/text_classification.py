from fastapi import APIRouter, Form, HTTPException
from fastapi.responses import JSONResponse
from app.utils.text_preprocessing import preprocess_text
import tensorflow as tf
import os
import requests
import io
from dotenv import load_dotenv


load_dotenv()
router = APIRouter()

UPLOADTHING_TOKEN = os.getenv("UPLOADTHING_TOKEN")

if UPLOADTHING_TOKEN is None:
    print("API key tidak ditemukan. Pastikan untuk mengatur variabel lingkungan dengan benar.")

MODEL_URL = 'https://utfs.io/f/xAikvGeCp3WDHvUWql15GcheMFpbiXQKBgtRNz2IkH6jl3sa'   



@router.post("/api/text")
async def create_text(text: str = Form(...)):
    try:
       
        text_tensor = await preprocess_text(text)
        
        # Mengunduh model dari UploadThing
        response = requests.get(MODEL_URL, headers={'Authorization': f'Bearer {UPLOADTHING_TOKEN}'})
        
        if response.status_code == 200:
            # Simpan file model yang diunduh sementara di server
            temp_model_path = '/tmp/temp_model.h5'
            with open(temp_model_path, 'wb') as f:
                f.write(response.content)
            
            # Memuat model dari file yang disimpan sementara
            model = tf.keras.models.load_model(temp_model_path)
            
            
            prediction = model.predict(text_tensor)
            prediction_list = prediction.tolist()
            
          
            return JSONResponse(content={"text": text, "prediction": prediction_list})
        else:
            raise HTTPException(status_code=500, detail="Failed to download model from UploadThing")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Prediction error: " + str(e))