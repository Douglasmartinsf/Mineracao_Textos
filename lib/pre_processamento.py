import regex
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def non_latin_rm(texto):
    texto = texto.apply(lambda x: regex.sub('[^\p{Latin}]', u' ', str(x)))
    return texto


def lower_case(texto):
    texto = texto.apply(lambda x: str(x).lower())
    return texto


def remove_stopwords(texto):
    nltk.download('stopwords')
    nltk.download('punkt')
    stops_list = stopwords.words("portuguese")
    word_tokens = word_tokenize(texto)
    texto_sem_stops = [w for w in word_tokens if w not in stops_list]
    return " ".join(texto_sem_stops)


def pre_processar(texto_final):
    return remove_stopwords(lower_case(non_latin_rm(texto_final)))
