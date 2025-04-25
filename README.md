# Como Rodar o Projeto

## 1. **Clone o repositório**

Primeiro, clone o repositório do projeto em sua máquina local:

```
git clone https://github.com/Pedrocs50/API-de-Autentica-o-com-Django-Deploy-no-Fly.io
cd API-de-Autentica-o-com-Django-Deploy-no-Fly.io
```

## 2. Criando e ativando o ambiente virtual

Recomendamos o uso de um ambiente virtual para gerenciar as dependências do projeto:

```
python -m venv venv
# Para Windows
venv\Scripts\activate
# Para Linux/Mac
source venv/bin/activate
```

## 3. Instalando as dependências

Instale todas as dependências para o projeto com o comando:

```
pip install -r requirements.txt
```

## 4. Configurando o banco de dados

Rode as migrações para configurar o banco de dados:

```
python manage.py migrate
```

## 5. Rodando o servidor de desenvolvimento

Inicie o servidor local para testar a API:

```
python manage.py runserver
```

## 6. Testando os endpoints manualmente

Teste os endpoints da API manualmente usando ferramentas como o **Postman** ou pelo proprio navegador, utilizando os seguintes caminhos:

**URL:**

* Para Signup: `POST http://127.0.0.1:8000/api/signup/`
* Para Login: `POST http://127.0.0.1:8000/api/login/`

* Para Me: `GET http://127.0.0.1:8000/api/me/`

### **Exemplo de Signup (Criação de Usuário)**

**URL:** `POST http://127.0.0.1:8000/api/signup/`

**Parâmetros:**

* `email`: Email do usuário.
* `name`: Nome do usuário.
* `password`: Senha do usuário.

**Exemplo de corpo da requisição:**

```
{
  "email": "novousuario@example.com",
  "name": "Novo Usuário",
  "password": "senhasegura123"
}
```

### **Exemplo de Login**

**URL:** `POST http://127.0.0.1:8000/api/login/`

****Parâmetros**:**

* `email`: Email do usuário.
* `password`: Senha do usuário.

**Exemplo de corpo da requisição:**

```
{
  "email": "novousuario@example.com",
  "password": "senhasegura123"
}
```

### Exemplo de Me(Informações do Usuário Autenticado)

**URL:** `GET http://127.0.0.1:8000/api/me/`

**Auteticação:** Após o login, adicione o token `acesss` JWT no cabeçalho da requisição.

**Exemplo de cabeçalho:**

```
Authorization: Bearer <seu_token_jwt>
```

---

# 💻🛠️ Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias:

- **Django** 🐍: Framework web para desenvolvimento de aplicações Python.
- **Django REST Framework** 🖥️: Toolkit poderoso para a construção de APIs em Django.
- **JWT** 🔑: Autenticação segura com JSON Web Tokens.
- **SQLite** 🗄️: Banco de dados local.
- **Fly.io** 🌐: Plataforma para deploy e hospedagem da aplicação.
- **Docker** 🐋: Containerização da aplicação.
- **Gunicorn** 🏎️: Servidor HTTP Python WSGI para produção.
- **Swagger** 📑: Ferramenta para documentação interativa da API.
- **unittest** ✅: Framework de testes.

---

# Funcionalidades Extras

## Documentação com Swagger

A  API apresentada possui documentação interativa utilizando o Swagger UI, acessível em  `/api/docs/.`

Sendo possível visualizar todos os endpoints disponíveis, testar requisições diretamente do navegador e entender os dados esperados e retornados pela API.

### Como acessar a documentação:

1. Depoios de rodar a API, acesse a seguinte URL no seu navegador:

   ```
   http://127.0.0.1:8000/api/docs/
   ```
2. Você verá todos os **endpoints** da API, como:

   * `POST /api/signup/` para criar um novo usuário.
   * `POST /api/login/` para obter o token JWT.
   * `GET /api/me/` para pegar os dados do usuário autenticado.

   Para testar um **endpoint**, você pode clicar nele, preencher os campos necessários (como `email`, `password`, etc.), e clicar em "Try it out" para enviar a requisição diretamente do Swagger UI.

## Middleware de Log de Requisições

O middleware **registra todas as requisições** feitas para a API. Para cada requisição, ele mostra no terminal:

* O método HTTP (GET, POST etc.)
* O endpoint acessado
* O status da resposta (200, 400 etc.)
* O tempo de resposta
* E o usuário (ou `Anonymous` se não estiver autenticado)

O  middleware ajuda a depurar e monitorar o sistema, consequentemente entendendo o comportamento em tempo real.

## Testes Automatizas 

A aplicação conta com **testes automatizados** para garantir que as principais funcionalidades da API funcionem corretamente.

### Como rodar os testes:

1. Para rodar todos os testes de uma vez:

   ```
   python manage.py test
   ```
2. Para rodar um teste específico (testes de signup, login e me):

   ```
   python manage.py test core.test_auth.SignupTestCase
   python manage.py test core.test_auth.LoginTestCase
   python manage.py test core.test_auth.MeEndpointTestCase
   ```

---

## 🌍 Link da API Online

A aplicação está disponível na seguinte URL: [https://auth-api-app.fly.dev](https://auth-api-app.fly.dev)
