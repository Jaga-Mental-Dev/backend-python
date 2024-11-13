# import tensorflow as tf
# from tensorflow.keras.models import load_model

# # Load the text model
# try:
#     text_model = load_model('./ai_models/text_model.h5')
# except Exception as e:
#     raise RuntimeError("Text model loading failed: " + str(e))

# def predict_text(text_tensor: tf.Tensor):
#     return text_model.predict(text_tensor)
