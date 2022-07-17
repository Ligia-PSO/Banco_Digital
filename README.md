# Banco Digital
> Sistema de Banco digital criado como parte do Desafio para a semifinal do Codigo[/s] da how

## Instalação:
**1.Clone Repo**
```sh
git clone https://github.com/Ligia-PSO/Banco_Digital
```
**2.Criar ambiente virtual & Requisitos de instalção**
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