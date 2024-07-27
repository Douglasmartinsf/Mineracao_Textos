# Projeto de Mineração de Textos - Ciência de Dados II

## Universidade Federal de Santa Maria
### Engenharia da Computação
### Disciplina: Ciência de Dados II
### Docente: Gabriel Machado Lunardi

## Descrição do Projeto
Este projeto foi desenvolvido como parte da disciplina de Ciência de Dados II e tem como objetivo aplicar as etapas do processo de Knowledge Discovery in Texts (KDT), incluindo seleção, limpeza, transformação, mineração e interpretação de dados. O projeto envolve a criação de um mecanismo de classificação automática de sentimentos dos usuários acerca dos 10 aplicativos mais populares da Google Play Store.

## Aplicativos Analisados
- Shopee
- SHEIN
- TikTok Lite
- Nubank
- Instagram
- Photo & File Detect
- Whatsapp Messenger
- Canva: Desenho Fotos e Vídeos
- CapCut - Editor de Vídeos
- Gov.br

## Base de Dados
Foram coletados 300 comentários de usuários para cada um dos aplicativos supracitados, totalizando 3.000 comentários. Cada comentário foi classificado por avaliadores humanos em duas dimensões:
1. **Polaridade**: Positivo ou Negativo.
2. **Emoção**: 
   - Felicidade
   - Surpresa
   - Tristeza
   - Neutro
   - Medo
   - Nojo
   - Raiva

## Objetivo
Desenvolver um mecanismo para classificar (prever) a emoção e a polaridade dos comentários dos usuários.

## Estrutura do Projeto
O projeto foi estruturado da seguinte forma:
- **Pré-processamento dos Dados**: Limpeza e transformação dos dados coletados.
- **Modelagem e Treinamento**: Implementação e treinamento de diversos modelos de classificação de texto.
- **Avaliação de Desempenho**: Análise da performance dos modelos utilizando métricas como precisão, revocação, medida-F e matriz de confusão.
- **Classificação de Novos Comentários**: Predição de três novos comentários não presentes no conjunto de treino.

## Modelos Utilizados
- BoW + NaiveBayes (Modelo Base)
- TF-IDF + NaiveBayes
- BoW + KNN
- TF-IDF + KNN
- Redes Neurais com embeddings (Word2Vec, GloVe, Doc2Vec)
- Modelos pré-treinados avançados como BERTimbau e LLama

## Instruções para Execução
1. Clone o repositório:
    ```bash
    git clone https://github.com/Douglasmartinsf/Mineracao_Textos.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd Mineracao_Textos
    ```
3. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```
4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
5. Execute o Jupyter Notebook:
    ```bash
    jupyter notebook
    ````

