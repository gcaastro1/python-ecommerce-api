# E-Commerce Python API

## Instalação dos pacotes:

**1.** Crie seu ambiente virtual:
```bash
python -m venv venv
```

**2.** Ative seu venv:
```bash
# Linux:
source venv/bin/activate

# Windows (Powershell):
.\venv\Scripts\activate

# Windows (Git Bash):
source venv/Scripts/activate
```

**3.** Instale todas as dependencias em `requirements.txt`:
```shell
pip install -r requirements.txt
```

**4.** Configure o arquivo **.env**:
```SECRET_KEY= chave_secreta
POSTGRES_DB= nome_do_banco_de_dados
POSTGRES_USER= usuário
POSTGRES_PASSWORD= senha_do_usuário
```

**5.** A documentação pode ser encontrada no seguinte end-point:
```shell
# Localhost:
http://localhost:8000/api/docs/
http://127.0.0.1:8000/api/docs/

# Host externo:
http://_dominio-aqui_/api/docs/
```

## Executando a API localmente:

Siga os seguintes passos com o **venv ativo**:

**1.** Gere as migrações:
```shell
python manage.py makemigrations
```

**2.** Para criar o banco de dados configurado de acordo com as models execute:
```shell
python manage.py migrate
```

**3.** Execute o server:
```shell
python manage.py runserver
```

