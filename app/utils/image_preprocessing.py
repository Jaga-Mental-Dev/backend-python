import tensorflow as tf

async def preprocess_image(image_data: bytes) -> tf.Tensor:
    try:
        image = tf.io.decode_image(image_data, channels=1)
        image = tf.image.resize(image, [48, 48])
        image = tf.cast(image, tf.float32) / 255.0
        image_tensor = tf.expand_dims(image, axis=0)
        return image_tensor
    except Exception as e:
        raise RuntimeError(f"Error processing image: {e}")
