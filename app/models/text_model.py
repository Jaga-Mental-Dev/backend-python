import tensorflow as tf
from tensorflow.keras.models import load_model
import os

try:
    model_path = os.path.join(os.path.dirname(__file__), '../../ai_models/text_classifiation/model_text_expresi.h5')
    image_model = load_model(model_path)
except Exception as e:
    raise RuntimeError("Text model loading failed: " + str(e))

def predict_text(text_tensor: tf.Tensor):
    return text_model.predict(text_tensor)
