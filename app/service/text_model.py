import tensorflow as tf
from tensorflow.keras.models import load_model
import os
from app.utils.model_utils import preprocess_text


def load_model_with_custom_objects():
    try:
        model_path = os.path.join(os.path.dirname(__file__), "../data_model/text_model.h5")
        custom_objects = {
            'LSTM': lambda **kwargs: tf.keras.layers.LSTM(
                **{k: v for k, v in kwargs.items() if k != 'time_major'}
            )
        }
        
        return load_model(model_path, custom_objects=custom_objects)
    except Exception as e:
        raise RuntimeError(f"Text model loading failed: {str(e)}")

try:
    text_model = load_model_with_custom_objects()
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