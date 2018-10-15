# jupyter notebook que faz o fechamento mensal do calango hackerclube

A ideia: criar um script que, dado os arquivos de dados, faça o fechamento das contas e ainda exporte um csv no formato para control^c control^v no google docs.

O que ele já faz:

* fecha as contas
* gera o arquivo com os dados pro gdocs

O que ele não faz, mas deveria:

* conectar automagicamente no gdocs e subir os dados
* fazer uns gráficos lokos
* brujeria!!!

Pré-requisitos para rodar o código:

- Python 3
- Pipenv

Executando o código:

Crie seu ambiente pipenv e ative seu shell:

```bash
$ pipenv install
$ pipenv shell
```

Copie os arquivos da pasta de exemplo para a pasta input:

```bash
$ cp data/example/caixa.txt data/input/caixa.txt
$ cp data/example/mercadopago.xls data/input/mercadopago.xls
$ cp data/example/paypal.csv data/input/paypal.csv
```

Inicialize o jupyter notebook:

```bash
$ jupyter-notebook financeiro.ipynb
```
