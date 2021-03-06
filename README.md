# 💰 Banco Digital 💰
> Sistema de Banco digital criado como parte do Desafio para a semifinal do Codigo[/s] da how

<h2 align="left">conteudo </h2>

  - [Instalação](#instalação)
  - [Funcionalidades](#funcionalidades)
  - [Base de dados](##base-de-dados)
  - [Documentação de apoio](#documentação-de-apoio)
  
# Instalação:
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
## Base de Dados

![image](https://user-images.githubusercontent.com/86573930/179431291-5d2c8752-75dc-4067-88ec-eb99849805fd.png)

# Funcionalidades
## Tela inicial 
### /
Retorna a tela de inicio mostrada abaixo
![image](https://user-images.githubusercontent.com/86573930/179430011-01dc5320-07e0-4ebd-b477-b1d17367a1e4.png)

Na Home page existem 4 links:um para  [cadastramento de conta bancaria](##cadastrar-conta-bancaria),outro para [cadastramento de cliente](##cadastrar-cliente),uma terceira para permitir a criação de transferencias e por ultimo uma pagina para consultar as transferencias dentro de um periodo de tempo.


## Cadastrar Conta Bancaria
### /contabancaria

![image](https://user-images.githubusercontent.com/86573930/179430694-8bd8c08d-f10a-44ca-9b5e-b23a8caa27f5.png)

pode ser cadastrado 3 tipos diferentes de contas sendo elas pupança salario e corrente dessa forma um cliente pode ter multiplas contas e o codigo da conta bancaria e gerado automaticamente 

### Validações 
# Cadastrar Cliente
### /cliente

### /contabancaria/[numero da conta]

### /cliente/<id do cliente>

# Fazer uma transferencia 
### /transferencia
![image](https://user-images.githubusercontent.com/86573930/179430908-f371ff2f-037b-4139-a7c0-2db1931dd7f2.png)

# Listar todas as contas bancarias
Lista todas as Contas bancarias cadastradas

### /contabancaria/todas
![image](https://user-images.githubusercontent.com/86573930/179430958-2f360ea6-263a-4221-950d-9709dcf31a08.png)

## Consultar saldo
### /contabancaria/[numero da conta]/saldo
Retorna somente o saldo de uma conta estipulada

# Consultar transferencias

## Interface consultar tranferencias em um periodo
### /consultartransferencia

Intervafe para consultar transferencias realizadas por uma especifica conta bancaria dentro de um periodo de tempo podendo separálas por enviada e recebidas 

![image](https://user-images.githubusercontent.com/86573930/179430789-a307b515-5bf9-485d-b1ac-65133b3d969d.png)

## Consultar transferencias específicas
### /contabancaria/[numero da conta ]/transferencias
consulta todas as transferencias realizadas por uma dada  conta bancaria 
### /contabancaria/[numero da conta ]/transferencias/enviado
Filtra as transferencias retornando somente as enviadas
### /contabancaria/[numero da conta ]/transferencias/recebido
Filtra as transferencias retornando somente as recebidas


# Documentação de apoio

### [django mysql](https://docs.djangoproject.com/pt-br/4.0/ref/databases/#mysql-notes)

### [django rest framework](https://www.django-rest-framework.org/)

### [video demostrando a aplicação]()
