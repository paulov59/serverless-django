# Serverless Django

![GitHub repo size](https://img.shields.io/github/repo-size/paulov59/serverless-django?style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/paulov59/serverless-django?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/paulov59/serverless-django?style=for-the-badge)
![Bitbucket open issues](https://img.shields.io/github/issues/paulov59/serverless-django?style=for-the-badge)


## Instalando o Serverless Django

Para executar, siga estas etapas:

1. Baixe o repositório :
```bash
git clone https://github.com/paulov59/serverless-django.git
```

2. Abra o diretorio do projeto:
```bash
cd serverless-django
```

3. Instale as dependencias e inicie a aplicação:
 ```bash
python -m venv env
```
```bash
source env/bin/activate
```
```bash
pip install -r requirements.txt
```
```bash
python manage.py migrate
```
```bash
python manage.py popula_db
```
```bash
python manage.py runserver
```
4. Acesse o sistema: [http://localhost:8000/](http://localhost:8000/).
