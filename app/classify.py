# Imports
import argparse
import numpy as np
import pandas as pd
import random
import tensorflow as tf
import json
import os

from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences

from app.utils import clean_text

# Constantes
SEED = 42
MAX_TEXT_LENGTH = 200
MODEL_PATH="../modeldata"
TARGETS = {
    0: "exploration",
    1: "headhunters",
    2: "intelligence",
    3: "logistics",
    4: "politics",
    5: "transportation",
    6: "weapons"
}


def get_class(text):
    # Lee los datos de los archivos y crea un dataframe con el texto
    predict_text = pd.DataFrame(columns=["text"])
    predict_text = predict_text.append({"text": text}, ignore_index=True)
    # Limpia los datos
    c_text = clean_text(predict_text["text"])

    # Carga el modelo del tokenizador y tokeniza los datos de entrada
    with open(os.path.join(MODEL_PATH, 'tokenizer.json')) as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)
    train_sequences = tokenizer.texts_to_sequences(c_text)
    # Añadir padding o truncar el texto para que todas las sentencias de texto tengan la misma longitud
    train_padded = pad_sequences(train_sequences, maxlen=MAX_TEXT_LENGTH, padding="post", truncating="post")

    # Cargar el modelo
    trained_model = tf.keras.models.load_model(os.path.join(MODEL_PATH, 'model.h5'))

    # Hacer las predicciones
    predictions = trained_model.predict(train_padded)

    # Transformar las predicciones a una clase e imprimir el resultado para cada arhcivo
    # con el formato: "archivo clase"
    y_p = [TARGETS[np.argmax(x)] for x in predictions]
    print("------------")
    print(y_p)
    return y_p
