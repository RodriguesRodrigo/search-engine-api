# Search Engine by Name

## Índice

- [Rodando o projeto][Rodando o projeto]
  - [Pré-requisitos][Pré-requisitos]
- [API][API]
  - Health Check

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
$ python application.py
```

Você pode testar por linha de comando:

```
$ curl http://localhost:5000/api/healthcheck
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
