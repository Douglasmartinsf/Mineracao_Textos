# Notebooks

## Visão Geral

Esta pasta contém diversos notebooks do Jupyter que foram utilizados para a análise de dados, treinamento de modelos e pré-processamento de texto no projeto. Cada notebook aborda uma técnica ou modelo específico para o processamento de linguagem natural (NLP) aplicado no estudo.

### Notebooks Incluídos:

1. **Doc2Vec.ipynb**:
   - Implementação do modelo Doc2Vec para a vetorização de documentos. Este notebook mostra como transformar textos em vetores de características, que podem ser usados para várias tarefas de NLP.

2. **bertimbau.ipynb**:
   - Utiliza o modelo BERTimbau, uma variante do BERT para o português. Este notebook abrange o fine-tuning do modelo e sua aplicação para classificação de texto ou outras tarefas relevantes.

3. **bow_knn.ipynb**:
   - Implementação de um modelo de classificação K-Nearest Neighbors (KNN) usando uma abordagem Bag-of-Words (BoW). O notebook cobre a transformação do texto em uma matriz BoW e a subsequente classificação.

4. **llama.ipynb**:
   - Aplicação do modelo LLAMA para geração de texto ou outras tarefas de NLP. Este notebook demonstra o uso de LLAMA, que é um modelo poderoso para tarefas de linguagem natural.

5. **pre_processamento.ipynb**:
   - Notebook dedicado ao pré-processamento dos textos. Inclui etapas como limpeza, tokenização, remoção de stopwords, e outras técnicas necessárias para preparar os dados para modelagem.

6. **tf-idf_knn.ipynb**:
   - Implementação de um modelo KNN utilizando a técnica TF-IDF para a vetorização do texto. Este notebook foca na transformação de textos em vetores TF-IDF e na aplicação do KNN.

7. **tf-idf_nb.ipynb**:
   - Implementação de um modelo Naive Bayes (NB) utilizando vetores TF-IDF. Este notebook mostra como treinar um classificador Naive Bayes com características extraídas via TF-IDF.

## Explicação dos Modelos de Vetorização e Treinamento

### Modelos de Vetorização

1. **TF-IDF (Term Frequency-Inverse Document Frequency)**:
   - TF-IDF é uma técnica amplamente utilizada para transformar textos em vetores numéricos, levando em consideração tanto a frequência de termos quanto sua importância inversa em diferentes documentos. Ele captura a relevância de palavras em um contexto específico, penalizando termos comuns em todo o corpus.

2. **Bag-of-Words (BoW)**:
   - BoW é uma representação simples em que cada texto é transformado em um vetor baseado na frequência das palavras, desconsiderando a ordem e estrutura das palavras no texto. É uma abordagem eficaz para modelos simples, mas pode não capturar relações semânticas entre as palavras.

3. **Doc2Vec**:
   - Doc2Vec é uma extensão do Word2Vec que gera vetores para documentos inteiros, em vez de palavras individuais. Ele é capaz de capturar o contexto completo de um documento, produzindo uma representação densa que leva em conta o significado global do texto, ao invés de focar apenas em palavras isoladas.

### Modelos de Treinamento

1. **K-Nearest Neighbors (KNN)**:
   - O KNN é um algoritmo de classificação simples que atribui rótulos com base nas classes dos vizinhos mais próximos no espaço vetorial. É útil para problemas em que as fronteiras de decisão não são lineares e onde se pode beneficiar de uma abordagem baseada em exemplos.

2. **Naive Bayes (NB)**:
   - O Naive Bayes é um classificador probabilístico baseado no Teorema de Bayes, com a suposição de independência entre os preditores. É especialmente eficaz para tarefas de classificação de texto, como análise de sentimentos, devido à sua simplicidade e eficiência.

3. **BERTimbau**:
   - BERTimbau é uma versão do modelo BERT treinada especificamente para o português. Ele utiliza mecanismos de atenção para entender o contexto das palavras dentro de uma frase, oferecendo representações robustas para tarefas de NLP como classificação de texto.

4. **LLAMA**:
   - O LLAMA é um modelo de linguagem avançado que pode ser utilizado para várias tarefas de NLP, incluindo geração de texto e classificação. Ele é conhecido por sua capacidade de produzir resultados de alta qualidade em tarefas complexas.

## Justificativa para a Escolha do Doc2Vec

Escolhi o Doc2Vec para este trabalho em vez de outros modelos como Word2Vec ou GloVe por conta de sua capacidade de capturar o contexto global dos comentários. Diferente de Word2Vec, que gera vetores para palavras individuais, o Doc2Vec cria uma representação vetorial para o texto completo. Isso é particularmente útil para a classificação de sentimentos, onde o sentimento geral de um comentário pode depender da combinação e contexto das palavras, e não apenas das palavras individualmente.

Em análises de sentimentos, palavras individuais podem ser ambíguas e aparecer em diferentes contextos com significados diversos. Por exemplo, a palavra "bom" pode ser utilizada tanto em críticas positivas quanto em negativas, dependendo do contexto. O Doc2Vec, ao capturar a visão geral do comentário, ajuda a evitar essa ambiguidade, tornando-o mais eficaz para tarefas onde o significado completo da frase é crucial.

## Como Utilizar

- **Passo 1: Pré-processamento**:
  - Comece pelo notebook `pre_processamento.ipynb` para preparar os dados de entrada. Esse passo é essencial para garantir que os textos estejam limpos e prontos para a modelagem.

- **Passo 2: Escolha o Modelo**:
  - Dependendo da tarefa, escolha um dos notebooks que implementa o modelo de interesse (`Doc2Vec.ipynb`, `bertimbau.ipynb`, `bow_knn.ipynb`, `tf-idf_knn.ipynb`, `tf-idf_nb.ipynb`, `llama.ipynb`).

- **Passo 3: Treinamento e Avaliação**:
  - Utilize os notebooks para treinar os modelos escolhidos e avalie os resultados. Cada notebook inclui as etapas de treinamento, validação e avaliação do desempenho.