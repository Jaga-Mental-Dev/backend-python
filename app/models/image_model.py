# import os
# import tensorflow as tf
# from tensorflow.keras.models import load_model


# try:
#     model_path = os.path.join(os.path.dirname(__file__), '../../ai_models/text_classifiation/model_text_expresi.h5')
#     image_model = load_model(model_path)
# except Exception as e:
#     raise RuntimeError("Image model loading failed: " + str(e))

# def predict_image(image_tensor: tf.Tensor):
#     return image_model.predict(image_tensor)
