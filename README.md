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
1. **Polaridade**: Positivo, Negativo ou Neutro.
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
O projeto foi organizado em uma estrutura de pastas para facilitar a navegação e a manutenção do código.

- **Base/:** Contém o código base utilizado no projeto, além do enunciado
- **Data/:** Contém os conjuntos de dados utilizados no projeto, como os comentários coletados, os comentários pré-processados, e arquivos de backup.
- ***Notebooks/:*** Contém os notebooks Jupyter com diferentes processos de vetorização e treinamento.

Além dessas pastas principais, o projeto inclui os seguintes arquivos:

- ***.gitignore:*** Arquivo de configuração para ignorar arquivos e pastas que não devem ser versionados pelo Git.
- ***README.md:*** Este arquivo, que descreve o projeto e fornece instruções de uso.
- ***requirements.txt:*** Contém as dependências necessárias para a execução do projeto.

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
    jupyter notebook Notebooks
    ````

