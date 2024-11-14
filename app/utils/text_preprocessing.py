import tensorflow as tf
import re
from nltk.stem import PorterStemmer
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.preprocessing.sequence import pad_sequences


import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stopwords = set(stopwords.words("english"))


async def preprocess_text(text: str) -> tf.Tensor:
    try:
        stemmer = PorterStemmer()
        corpus = []
        text = re.sub("[^a-zA-Z]", " ", text)
        text = text.lower()
        text = text.split()
        text = [stemmer.stem(word) for word in text if word not in stopwords]
        text = " ".join(text)
        corpus.append(text)
        one_hot_word = [one_hot(input_text=word, n=11000) for word in corpus]
        tensor_text = pad_sequences(sequences=one_hot_word, maxlen=500, padding='pre')
        return tensor_text
    except Exception as e:
        raise RuntimeError(f"Error processing text: {e}")

