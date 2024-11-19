import tensorflow as tf
from tensorflow.keras.models import load_model
import os
from app.utils.model_utils import preprocess_image
from fastapi import UploadFile

try:
    model_path = os.path.join(os.path.dirname(__file__), "../data_model/face_model.h5")
    image_model = load_model(model_path)
except Exception as e:
    raise RuntimeError("face model loading failed: " + str(e))

LABELS = ['marah', 'happy', 'netral', 'sedih']

def predict_image(file: UploadFile):

    try:
        image_data = file.file.read() 
        image_tensor = preprocess_image(image_data) 
         
        prediction = image_model.predict(image_tensor)

        prediction = prediction[0]

        max_index = tf.argmax(prediction).numpy()
        max_label = LABELS[max_index]
        max_probability = float(prediction[max_index])
               
        return {"label": max_label, "probability": max_probability}

    except Exception as e:
        raise RuntimeError("Prediction failed: " + str(e))
