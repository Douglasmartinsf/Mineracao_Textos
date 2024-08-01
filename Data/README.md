# Data

## Conteúdo da Pasta

Esta pasta contém os principais conjuntos de dados utilizados no projeto de mineração de textos. Os dados fornecidos aqui são essenciais para o pré-processamento, análise e validação dos modelos desenvolvidos nos notebooks.

### Arquivos:

- **apps_reviews_validacao.xlsx**: Dataframe original, contendo um conjunto de dados de validação de reviews de aplicativos. Este arquivo é utilizado pelo notebook de pré-processamento, para gerar o dataframe seguinte.
  
- **content_pre_processado.csv**: Dataframe que contém os dados de comentários pré-processados. Este arquivo já passou por etapas de limpeza, tokenização e outras transformações necessárias para a modelagem de texto, e é importado por todos demais notebooks.
  
- **spellchecker_bak.csv**: Arquivo CSV que serve como backup dos dados após a etapa de correção ortográfica, por ser a etapa mais demorada do pré-processamento. Caso queira atualizar alguma etapa depois dela no notebook de pré-processamento, não é necessário executar a etapa de correção ortográfica novamente.

-  **bertimbau.csv**: Arquivo com a coluna 'predictions' gerada pelo modelo BERTimbau
