# 💰 Banco Digital 💰
> Sistema de Banco digital criado como parte do Desafio para a semifinal do Codigo[/s] da how
_________

<h2 align="left">conteudo </h2>

  - [Instalação](#instalação)
  - [Base de dados](##base-de-dados)
  - [listagem de urls habilitados](#listagem-de-urls-habilitados)
  - [Funcionalidades](#funcionalidades)
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
_______________________
## Base de Dados
A base de dados do sistema final se econtra representada abaixo:

![image](https://user-images.githubusercontent.com/86573930/179450349-98a804aa-6912-4d30-959d-b9c71481a8bf.png)

________________________
# Listagem de urls habilitados
### Cadastro

/contabancaria

/cliente

/transferencia

### Consulta Base de Dados

/contabancaria/[numero da conta]/saldo

/contabancaria/[numero da conta]

/contabancaria/todas

/cliente/[id do cliente]


### Consulta de Transferencias:

/consultartransferencia

/contabancaria/[numero da conta ]/transferencias

/contabancaria/[numero da conta ]/transferencias/enviado

/contabancaria/[numero da conta ]/transferencias/enviado
_______________
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
Pagina de cadastro do cliente, possui diversas validaçoes para a conformidade dos campos , o botao de filtro pode ser usado para pesquisar por um cliente especifico por meio do seu cpf

![image](https://user-images.githubusercontent.com/86573930/179446193-1d5394ac-5e59-44b5-aa2d-20148d714f3b.png)

### /contabancaria/[numero da conta]
Consultar uma conta bancaria especifica

### /cliente/[id do cliente]
Consultar um cliente especifico
# Fazer uma transferencia 
### /transferencia

![image](https://user-images.githubusercontent.com/86573930/179430908-f371ff2f-037b-4139-a7c0-2db1931dd7f2.png)

Pagina de realização de transferencias nao permite transferencias de valor 0 nem negativos e avisa se nao ha saldo suficiente , tambem nao permite a transferencia de uma conta para si mesma. 
## Listar todas as contas bancarias


### /contabancaria/todas
![image](https://user-images.githubusercontent.com/86573930/179430958-2f360ea6-263a-4221-950d-9709dcf31a08.png)
Lista todas as Contas bancarias cadastradas
## Consultar saldo
### /contabancaria/[numero da conta]/saldo
Retorna somente o saldo de uma conta estipulada

# Consultar transferencias

### /consultartransferencia
![image](https://user-images.githubusercontent.com/86573930/179450666-daa35648-fd1f-401f-b15e-b9eece264c47.png)

Interface para consultar transferencias realizadas por uma especifica conta bancaria dentro de um periodo de tempo podendo separá-las por enviada e recebidas 

## Consultar transferencias específicas
### /contabancaria/[numero da conta ]/transferencias
Consulta todas as transferencias realizadas por uma dada  conta bancaria 
### /contabancaria/[numero da conta ]/transferencias/enviado
Filtra as transferencias retornando somente as enviadas
### /contabancaria/[numero da conta ]/transferencias/recebido
Filtra as transferencias retornando somente as recebidas

# Documentação de apoio

### [django mysql](https://docs.djangoproject.com/pt-br/4.0/ref/databases/#mysql-notes)

### [django rest framework](https://www.django-rest-framework.org/)

### [video demostrando a aplicação](https://youtu.be/_vOCj_L6T8w)
