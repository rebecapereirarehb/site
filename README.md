# 🛡️ FlaskAuth — Sistema Web Completo com Autenticação

Sistema de autenticação completo desenvolvido em Python com Flask, design moderno dark, responsivo e seguro.

---

## 📋 Funcionalidades

- ✅ Login e Cadastro de usuários
- ✅ Logout com registro de atividade
- ✅ Criptografia de senhas (Werkzeug/bcrypt)
- ✅ Controle de sessão (Flask-Login)
- ✅ Proteção de páginas restritas
- ✅ Dois perfis: **Usuário** e **Administrador**
- ✅ Dashboard personalizado por perfil
- ✅ Edição de perfil e upload de avatar
- ✅ Alteração de senha com verificação
- ✅ Recuperação de senha via token
- ✅ Painel admin: listar, criar, editar, ativar/desativar e excluir usuários
- ✅ Registro de atividades (logs) com IP e user-agent
- ✅ Validação de formulários no front e back-end
- ✅ Proteção CSRF em todos os formulários
- ✅ Páginas de erro customizadas (403, 404, 500)
- ✅ Interface responsiva para celular, tablet e desktop
- ✅ Design dark moderno com Bootstrap 5

---

## 🏗️ Estrutura do Projeto

```
flask_auth_system/
│
├── app/
│   ├── __init__.py          # Application Factory
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py          # Modelos User e Role
│   │   └── activity.py      # Modelo ActivityLog
│   ├── forms/
│   │   ├── __init__.py
│   │   ├── auth_forms.py    # Formulários de autenticação
│   │   ├── user_forms.py    # Formulários do perfil
│   │   └── admin_forms.py   # Formulários do admin
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py          # Rotas principais
│   │   ├── auth.py          # Rotas de autenticação
│   │   ├── user.py          # Rotas do painel do usuário
│   │   ├── admin.py         # Rotas do painel admin
│   │   └── errors.py        # Handlers de erro
│   ├── static/
│   │   ├── css/style.css    # Estilos principais
│   │   ├── js/app.js        # JavaScript principal
│   │   └── img/avatars/     # Avatars dos usuários
│   └── templates/
│       ├── base.html        # Template base (sidebar + topbar)
│       ├── main/index.html  # Página inicial
│       ├── auth/            # Login, cadastro, reset de senha
│       ├── user/            # Dashboard, perfil, edição
│       ├── admin/           # Dashboard admin, usuários, logs
│       └── errors/          # Páginas 403, 404, 500
│
├── instance/                # Banco de dados SQLite (gerado automaticamente)
├── config.py                # Configurações (dev, prod, test)
├── run.py                   # Ponto de entrada + comandos CLI
├── requirements.txt         # Dependências Python
├── .env.example             # Exemplo de variáveis de ambiente
└── README.md
```

---

## 🚀 Instalação e Execução

### Pré-requisitos
- Python 3.9 ou superior
- pip

### Passo 1 — Clone ou extraia o projeto
```bash
cd flask_auth_system
```

### Passo 2 — Crie e ative o ambiente virtual
```bash
# Criar
python -m venv venv

# Ativar no Linux/Mac
source venv/bin/activate

# Ativar no Windows
venv\Scripts\activate
```

### Passo 3 — Instale as dependências
```bash
pip install -r requirements.txt
```

### Passo 4 — Configure as variáveis de ambiente
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

O arquivo `.env` deve conter:
```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=sua-chave-secreta-muito-segura
DATABASE_URL=sqlite:///flaskauth.db
```

### Passo 5 — Inicialize o banco de dados
```bash
flask init-db
```

Este comando irá:
- Criar todas as tabelas no banco de dados
- Inserir os perfis `user` e `admin`
- Criar um administrador padrão

**Credenciais do admin padrão:**
```
E-mail:  admin@admin.com
Senha:   Admin@123
```
> ⚠️ **Altere a senha do admin imediatamente após o primeiro login!**

### Passo 6 — Execute a aplicação
```bash
flask run
# ou
python run.py
```

Acesse: **http://localhost:5000**

---

## 🗄️ Banco de Dados

O sistema usa **SQLite** por padrão (arquivo `instance/flaskauth_dev.db`).

### Tabelas criadas:
| Tabela | Descrição |
|--------|-----------|
| `roles` | Perfis de acesso (user, admin) |
| `users` | Dados dos usuários |
| `activity_logs` | Registro de atividades |

### Migrações (Flask-Migrate)
Para alterações futuras no banco:
```bash
flask db init        # Apenas na primeira vez
flask db migrate -m "descrição da mudança"
flask db upgrade
```

---

## 🔐 Segurança

| Recurso | Implementação |
|---------|--------------|
| Hash de senha | `werkzeug.security.generate_password_hash` |
| Proteção CSRF | Flask-WTF (token em todos os forms) |
| Sessão segura | Flask-Login com `session_protection='strong'` |
| Token de reset | `itsdangerous.URLSafeTimedSerializer` (expira em 1h) |
| Validação de entrada | WTForms validators (front + back-end) |
| Acesso restrito | Decorators `@login_required` e `@admin_required` |
| Secret Key | Configurada via variável de ambiente |

---

## 👤 Perfis de Acesso

### Usuário Comum (`user`)
- Dashboard pessoal
- Editar perfil e foto
- Alterar senha
- Ver histórico de atividades

### Administrador (`admin`)
- Tudo do usuário comum
- Dashboard com métricas do sistema
- Listar e buscar usuários
- Criar novos usuários
- Editar dados e perfil de qualquer usuário
- Ativar/desativar contas
- Excluir usuários
- Visualizar todos os logs do sistema

---

## 🛠️ Comandos CLI Disponíveis

```bash
# Inicializa banco + cria admin padrão
flask init-db

# Cria um novo administrador interativamente
flask create-admin

# Shell interativo com contexto da aplicação
flask shell

# Migrações de banco (Flask-Migrate)
flask db migrate -m "mensagem"
flask db upgrade
flask db downgrade
```

---

## 📦 Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|-----------|--------|-----|
| Python | 3.9+ | Linguagem principal |
| Flask | 3.0 | Framework web |
| Flask-Login | 0.6 | Gerenciamento de sessão |
| Flask-WTF | 1.2 | Formulários + CSRF |
| Flask-SQLAlchemy | 3.1 | ORM |
| Flask-Migrate | 4.0 | Migrações de banco |
| Werkzeug | 3.0 | Hash de senhas |
| itsdangerous | 2.2 | Tokens seguros |
| Bootstrap | 5.3 | UI responsiva |
| Bootstrap Icons | 1.11 | Ícones |
| SQLite | — | Banco de dados |

---

## 🎨 Interface

- Design **dark moderno** com paleta personalizada
- Tipografia: **Syne** (display) + **DM Sans** (corpo)
- Sidebar com navegação contextual por perfil
- Cards de estatísticas com ícones coloridos
- Tabelas com paginação e busca
- Formulários validados com feedback visual
- Alertas com auto-dismiss após 6 segundos
- Indicador de força de senha
- Toggle para mostrar/ocultar senha
- Totalmente responsivo (mobile-first)

---

## 🌐 Rotas Disponíveis

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/` | Página inicial |
| GET/POST | `/auth/login` | Login |
| GET/POST | `/auth/register` | Cadastro |
| GET | `/auth/logout` | Logout |
| GET/POST | `/auth/reset-password` | Solicitar reset |
| GET/POST | `/auth/reset-password/<token>` | Redefinir senha |
| GET | `/user/dashboard` | Dashboard do usuário |
| GET | `/user/profile` | Perfil do usuário |
| GET/POST | `/user/profile/edit` | Editar perfil |
| GET/POST | `/user/change-password` | Alterar senha |
| GET | `/admin/dashboard` | Dashboard admin |
| GET | `/admin/users` | Lista de usuários |
| GET/POST | `/admin/users/create` | Criar usuário |
| GET/POST | `/admin/users/<id>/edit` | Editar usuário |
| POST | `/admin/users/<id>/toggle` | Ativar/desativar |
| POST | `/admin/users/<id>/delete` | Excluir usuário |
| GET | `/admin/logs` | Logs do sistema |

---

## 💡 Dicas de Desenvolvimento

### Para usar PostgreSQL em produção:
```env
DATABASE_URL=postgresql://usuario:senha@localhost/flaskauth
```
Instale também: `pip install psycopg2-binary`

### Para configurar e-mail real (recuperação de senha):
No `.env`:
```env
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=seu@gmail.com
MAIL_PASSWORD=sua-app-password
```
No Gmail, use uma **Senha de App** (não a senha normal).

### Para produção:
```env
FLASK_ENV=production
SECRET_KEY=chave-longa-aleatoria-minimo-32-caracteres
```

---

## 📄 Licença

Projeto de código aberto para fins educacionais e desenvolvimento.

---

*Desenvolvido com Flask · Bootstrap 5 · SQLAlchemy · Python*

