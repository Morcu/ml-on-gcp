#!/usr/bin/env python

# Imports
import nltk
import re
from nltk.corpus import stopwords

# Descargar las stopwords en ingles y generar la constante
nltk.download('stopwords')
", ".join(stopwords.words('english'))
STOPWORDS = stopwords.words('english')


def remove_urls(text):
    """
    Funcion que elimina urls
    :param str text: texto a procesar
    """
    url_remove = re.compile(r'https?://\S+|www\.\S+')
    return url_remove.sub(r' ', text)


def remove_html(text):
    """
    Funcion que elimina marcados de html
    :param str text: texto a procesar
    """
    html = re.compile(r'<.*?>')
    return html.sub(r' ', text)


def punct_remove(text):
    """
    Funcion que elimina simbolos de puntuacion
    :param str text: texto a procesar
    """
    return re.sub(r"[^\w\s\d]", " ", text)


def underscore_remove(text):
    """
    Funcion que elimina guiones bajos
    :param str text: texto a procesar
    """
    return re.sub(r"_", " ", text)


def remove_num(text):
    """
    Funcion que elimina numeros
    :param str text: texto a procesar
    """
    return re.sub(r'\d+', ' ', text)


def remove_space(text):
    """
    Funcion que elimina espacios
    :param str text: texto a procesar
    """
    return re.sub(r"\s+", " ", text).strip()


def remove_stopwords(text):
    """
    Funcion que elimina stopwords
    :param str text: texto a procesar
    """
    return " ".join([w for w in text.split() if not w in STOPWORDS])


def lower(text):
    """
    Funcion que convierte el texto a minusculas
    :param str text: texto a procesar
    """
    return text.lower()


def clean_text(df_text):
    """
    Funcion que convierte el texto a minusculas
    :param str text: texto a procesar
    """
    df_text = df_text.apply(lower)
    df_text = df_text.apply(remove_urls)
    df_text = df_text.apply(remove_html)
    df_text = df_text.apply(underscore_remove)
    df_text = df_text.apply(punct_remove)
    df_text = df_text.apply(remove_num)
    df_text = df_text.apply(remove_stopwords)
    df_text = df_text.apply(remove_space)

    return df_text
