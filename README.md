# Banco Digital
> Banking Website built on Django designed with Bootstrap
## Installation:
**1.Clone Repo**
```sh
git clone https://github.com/shyam999/ParagonBank.git
```
**2.Setup Virtualenv & Install Requirements**
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
**3.Migre a Base de Dados**
```
python manage.py makemigrations
python manage.py migrate
```
**4.Rode o Servidor**
```
python manage.py runserver
```