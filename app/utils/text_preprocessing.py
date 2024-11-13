import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer()

async def preprocess_text(text: str) -> tf.Tensor:
    try:
        sequences = tokenizer.texts_to_sequences([text])
        padded_sequences = pad_sequences(sequences, maxlen=100)  
        return tf.convert_to_tensor(padded_sequences)
    except Exception as e:
        raise RuntimeError(f"Error processing text: {e}")

