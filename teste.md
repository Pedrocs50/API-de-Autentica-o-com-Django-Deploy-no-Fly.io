## ✅ Proposta de teste técnico

### 📝 **Título**: API de Autenticação com Django + Deploy no Fly.io

### 🎯 **Objetivo**
Criar uma API REST simples para cadastro e login de usuários, utilizando Django + Django Rest Framework, e disponibilizar em produção usando o Fly.io.

---

## 🔧 **Requisitos técnicos**

### 1. **Backend em Django**
- Usar Django 4+ ou 5 e Django Rest Framework.
- Criar endpoints:
  - `POST /api/signup/`: criar um novo usuário com `email`, `nome`, `senha`.
  - `POST /api/login/`: autenticação via JWT.
  - `GET /api/me/`: retornar os dados do usuário autenticado (JWT obrigatório).

### 2. **Autenticação**
- Utilizar `SIMPLE_JWT` ou outra solução JWT confiável.
- Tokens devem ter expiração de 1 hora.

### 3. **Validação**
- Não permitir e-mails duplicados.
- Senha com pelo menos 8 caracteres.

### 4. **Banco de dados**
- Pode usar SQLite em ambiente local.
- No Fly.io pode manter SQLite ou usar PostgreSQL gratuito (via Supabase, por exemplo).

### 5. **Deploy**
- Fazer deploy no **Fly.io** com link acessível publicamente.
- Pode usar `Dockerfile` ou `fly.toml` com `buildpacks`.

---

## 📂 Estrutura esperada do repositório

```
/auth-api/
├── manage.py
├── Dockerfile
├── requirements.txt / poetry.lock
├── fly.toml
└── core/
    ├── models.py
    ├── views.py
    ├── urls.py
    └── serializers.py
```

---

## ⚙️ Extras (não obrigatórios, mas contam pontos)

- Documentação com Swagger ou ReDoc.
- Middleware para log de requisições.
- Tests automatizados (`pytest` ou `unittest`).
- Explicação breve no README.

---

## 🚀 Entrega

- Repositório público no GitHub com instruções de instalação e deploy.
- Link público da API em produção no Fly.io.
- README com:
  - Tecnologias utilizadas.
  - Como rodar localmente.
  - Como testar o login.
  - Link da API online.

---

## 💡 Dica para o candidato

Se for o primeiro contato com Fly.io:
```bash
fly launch
fly deploy
```

---

Se quiser, posso te gerar esse `README.md` inicial para já deixar pronto no repositório. Quer?