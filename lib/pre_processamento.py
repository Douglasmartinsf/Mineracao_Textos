import regex
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Baixando as listas de stopwords e o tokenizador de palavras do nltk
nltk.download('stopwords')
nltk.download('punkt')

# Função para remover caracteres não latinos de um texto
def non_latin_rm(texto):
    return regex.sub('[^\p{Latin}]', u' ', str(texto))

# Função para converter um texto para minúsculas
def lower_case(texto):
    return str(texto).lower()

# Função para remover stopwords de um texto
def remove_stopwords(texto):
    stops_list = stopwords.words("portuguese")
    word_tokens = word_tokenize(texto)
    texto_sem_stops = [w for w in word_tokens if w not in stops_list]
    return " ".join(texto_sem_stops)

# Função principal de pré-processamento que aplica as três funções anteriores
def pre_processar(texto):
    texto = non_latin_rm(texto)
    texto = lower_case(texto)
    texto = remove_stopwords(texto)
    return texto

# Função para pré-processar uma coluna de um DataFrame aplicando a função de pré-processamento em cada linha
def pre_processar_dataframe(df, text_column):
    df[text_column] = df[text_column].apply(pre_processar)
    return df
