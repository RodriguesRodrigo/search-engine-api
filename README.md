# Search Engine by Name

## Rodando o projeto

### Pré-requisitos
  - Python na versão 3.9 ou superior (recomendado a utilização de [pyenv](https://pypi.org/project/pyenv/))

### Instalando dependências

#### Linux

É possível criar o virtualenv e instalar as dependências utilizando o comando make, basta executar o comando abaixo:

```
$ make setup
$ source venv/bin/activate
```

#### Windows

É importante que você crie uma virtualenv para o projeto, para evitar complicações com libs externas. Para isso, crie uma virtualenv e ative.

```
$ python -m venv venv
$ source venv/bin/activate
```

Com sua virtualenv instalada e ativada, podemos instalar as dependências com o comando abaixo:

```
$ pip install -r requirements.txt
```

### Rodando o projeto

Instalada as dependências, basta você rodar o comando abaixo para que o projeto esteja rodando na porta `5000`:

```
$ python app.py
```

Você pode testar por linha de comando:

```
$ curl http://localhost:5000/api/healthcheck
```

## Rodando os testes

Para rodar os testes é bem simples, primeiro você precisa instalar as dependências do projeto e depois executar os testes.

> Recomendo utilizar o virtualenv para instalar as dependências e rodar os testes.

É possível realizar a instalação e rodar os testes utilizando o comando make da seguinte maneira:

```
$ make install
$ make test
```

Desta forma, o comando `make install` irá instalar todas as dependências, inclusive as de desenvolvimento automaticamente e depois executará os testes com o comando `make test`, entregando um relatório de cobertura dos testes. Para visualizar o relatório de cobertura, basta abrir o arquivo `htmlcov/index.html`.

Caso você não consiga ou não queira utilizar os comandos make, é possível instalar as dependências e rodar os testes da seguinte forma:

```
# Instalando todas as dependências
$ pip install -r requirements.txt
$ pip install -r requirements-dev.txt
$ pip install -e .

# Rodando os testes
$ pytest
```

Caso precise visualizar os testes de forma mais detalhada, adicione o parâmetro `-v` da seguinte forma:

```
$ pytest -v
```

E para executar a cobertura dos testes, basta adicionar o parâmetro `--cov` e informar o diretório que deve ser realizada a cobertura, da seguinte forma:

```
$ pytest tests/ -v --cov=application
```

## API

### `GET` /api/healthcheck

#### Descrição

Endpoint responsável por retornar o status da API para monitoramento.

#### Exemplo de uso

```
$ curl http://localhost:5000/api/healthcheck
```

#### Resposta

```
{
  "message": "ok"
}
```
