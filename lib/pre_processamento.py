import regex
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('stopwords')
nltk.download('punkt')


def non_latin_rm(texto):
    return regex.sub('[^\p{Latin}]', u' ', str(texto))


def lower_case(texto):
    return str(texto).lower()


def remove_stopwords(texto):
    stops_list = stopwords.words("portuguese")
    word_tokens = word_tokenize(texto)
    texto_sem_stops = [w for w in word_tokens if w not in stops_list]
    return " ".join(texto_sem_stops)


def pre_processar(texto):
    texto = non_latin_rm(texto)
    texto = lower_case(texto)
    texto = remove_stopwords(texto)
    return texto


def pre_processar_dataframe(df, text_column):
    df[text_column] = df[text_column].apply(pre_processar)
    return df
