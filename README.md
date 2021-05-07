# plpred

By Giuli Argou Marques

a protein subcellular location predition program

## Setup

```
$ make setup
```

## Project Structure

  - `environment.yml`: configurações para criar/atualizar o ambiente do conda.
  - `requirements.txt`: bibliotecas do Python a serem instaladas no ambiente.
  - `Makefile`: cria chamadas (regras) para comandos a serem executados.
  - `data/`: diretório de dados. Os dados brutos são armazenados na pasta `data/raw`, no formato FASTA, os dados preprocessados são armazenados na pasta `data/processed` e os modelos treinados são armazenados na pasta `data/models`.
  - `plpred/`: diretório principal do pacote. Local de armazenamento das funções da aplicação: scripts de preprocessamento e de treinamento.
  - `model.pickle`: modelos são serializados utilizando arquivos `.pickle`, sendo salvos na pasta `data/models`.
  - `plpred/models`: disponibiliza modelos preditivos baseados em *Random Forest*, *Gradient Boosting*, *SVM* e redes neurais (MLP).