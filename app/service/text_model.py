import tensorflow as tf
from tensorflow.keras.models import load_model
import os
from app.utils.model_utils import preprocess_text


try:
    model_path = os.path.join(os.path.dirname(__file__), "../data_model/text_model.h5")
    text_model = load_model(model_path)
except Exception as e:
    raise RuntimeError("Text model loading failed: " + str(e))


LABELS = ['senang', 'sedih', 'love', 'netral', 'marah']

def predict_text(text: str):
  
    try:
        text_tensor = preprocess_text(text)  
        prediction = text_model.predict(text_tensor)

        prediction = prediction[0]

        max_index = tf.argmax(prediction).numpy()
        max_label = LABELS[max_index]
        max_probability = float(prediction[max_index])
               
        return {"label": max_label, "probability": max_probability}

    except Exception as e:
        raise RuntimeError("Prediction failed: " + str(e))
