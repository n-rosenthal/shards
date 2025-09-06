
# Sobre o Django
1. Cada aplicação em Django consiste em um pacote Python que segue uma certa convenção (arquitetura de arquivos, etc.). Django possui um utilitário que cria a estrutura de diretórios automaticamente, tanto para **criar um projeto** quanto para **criar uma aplicação**: `manage.py`; este programa possui diversas funções distintas e serve ao gerenciamento do projeto Django.


---
# Criar um projeto
```bash
[sudo] django-admin startproject site project
```

---
## Arquitetura de Diretórios

```bash
project/
    manage.py
    site/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```

- `manage.py`: ferramenta de terminal que permite interagir diretamente com o projeto Django de diversas formas.
- diretório `site/`: pacote Python *de facto* do projeto. Seu nome será o nome utilizado para importar qualquer coisa necessária. (e.g. `site.urls`)
	- `site/__init__.py`: documento de texto vazio que indica ao interpretador que este diretório deve ser lido como um pacote Python.
	- `site/settings.py`: settings/configuração do projeto;
	- `site/urls.py`: **declarações URL**, uma tabela de conteúdos (índice) da aplicação web.
	- `site/asgi.py`: *entry-point for ASGI-compatible web servers to serve the project.*
	- `site/wsgi.py`: *entry-point for WSGI-compatible web servers to serve the project.*

---
## Servidor de Desenvolvimento
O servidor de desenvolvimento Django é um servidor de web leve e escrito inteiramente em Python. Não deve ser usado em produção. Para **servir o site em outra porta**, verifique a documentação para `runserver`).

Para **verificar se o projeto Django funciona**, vamos até seu diretório e rodamos o servidor, a partir de `manage.py`.

```bash
cd project
python manage.py runserver
```

Se o servidor estiver rodando, então [http://127.0.0.1:8000/](http://127.0.0.1:8000/) deve mostrar a página padrão do Django.

---
## Criar uma Aplicação
Para criar uma aplicação dentro um projeto Django, utilizamos novamente o utilitário `manage.py` para criar a estrutura de diretórios adequada a uma **Aplicação Django**:

```bash
python manage.py startapp appname [path]
```

Se `path` for nulo, teremos `path=.`

---
### Arquitetura de Diretórios de uma Aplicação
```bash
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

#### `views.py`

