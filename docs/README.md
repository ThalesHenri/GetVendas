# GetVendas

Sistema web para **gestão de pedidos comerciais**, desenvolvido em **Django Fullstack**, focado em simplicidade, agilidade e organização do fluxo entre vendedores e central administrativa.

> MVP desenvolvido para centralizar pedidos, organizar produtos e facilitar o faturamento externo.

---

## 📌 Visão Geral

O **GetVendas** permite que:

- **Vendedores** criem e acompanhem pedidos
- **Central** gerencie produtos, pedidos e status
- Pedidos sejam **exportados em PDF**
- O faturamento seja feito em **plataforma externa**

⚠️ O sistema **não realiza pagamentos**.

---

## 👥 Perfis de Usuário

### Central (Backoffice)
- Cadastro e edição de produtos
- Visualização de todos os pedidos
- Alteração de status dos pedidos
- Exportação de pedidos em PDF
- Visualização de estatísticas gerais

### Vendedor
- Criação de pedidos
- Envio de pedidos para a Central
- Acompanhamento do status
- Visualização de estatísticas pessoais

---

## 🚀 Funcionalidades do MVP

- Autenticação por e-mail e senha
- Controle de usuários por perfil (Central / Vendedor)
- CRUD de produtos
- Criação e gerenciamento de pedidos
- Status do pedido (Rascunho, Enviado, Faturando, Faturado)
- Exportação de pedidos em PDF
- Dashboard simples por tipo de usuário

---

## 🛠️ Stack Tecnológica

- **Backend:** Django
- **Frontend:** Django Templates + CSS puro
- **Banco de Dados:** SQLite (MVP)
- **PDF:** ReportLab
- **Autenticação:** Django Auth
- **API:** ❌ Não utiliza API (Fullstack)

---

## 📂 Estrutura do Projeto
# GetVendas

Sistema web para **gestão de pedidos comerciais**, desenvolvido em **Django Fullstack**, focado em simplicidade, agilidade e organização do fluxo entre vendedores e central administrativa.

> MVP desenvolvido para centralizar pedidos, organizar produtos e facilitar o faturamento externo.

---

## 📌 Visão Geral

O **GetVendas** permite que:

- **Vendedores** criem e acompanhem pedidos
- **Central** gerencie produtos, pedidos e status
- Pedidos sejam **exportados em PDF**
- O faturamento seja feito em **plataforma externa**

⚠️ O sistema **não realiza pagamentos**.

---

## 👥 Perfis de Usuário

### Central (Backoffice)
- Cadastro e edição de produtos
- Visualização de todos os pedidos
- Alteração de status dos pedidos
- Exportação de pedidos em PDF
- Visualização de estatísticas gerais

### Vendedor
- Criação de pedidos
- Envio de pedidos para a Central
- Acompanhamento do status
- Visualização de estatísticas pessoais

---

## 🚀 Funcionalidades do MVP

- Autenticação por e-mail e senha
- Controle de usuários por perfil (Central / Vendedor)
- CRUD de produtos
- Criação e gerenciamento de pedidos
- Status do pedido (Rascunho, Enviado, Faturando, Faturado)
- Exportação de pedidos em PDF
- Dashboard simples por tipo de usuário

---

## 🛠️ Stack Tecnológica

- **Backend:** Django
- **Frontend:** Django Templates + CSS puro
- **Banco de Dados:** SQLite (MVP)
- **PDF:** ReportLab
- **Autenticação:** Django Auth
- **API:** ❌ Não utiliza API (Fullstack)

---

## 📂 Estrutura do Projeto

project/
│
├── core/ # usuários, autenticação e permissões
├── produtos/ # gestão de produtos
├── pedidos/ # pedidos e itens de pedido
├── templates/ # templates HTML
├── static/ # arquivos estáticos (CSS)
├── media/ # uploads (ignorado no git)
└── manage.py


---

## ⚙️ Instalação e Execução

### 1. Clone o repositório
```bash
git clone <url-do-repositorio>
cd getvendas


2. Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

3. Instale as dependências
pip install -r requirements.txt

4. Rode as migrações
python manage.py migrate

5. Crie um superusuário
python manage.py createsuperuser

6. Inicie o servidor
python manage.py runserver


Acesse em:
👉 http://127.0.0.1:8000

📄 Exportação de PDF

Cada pedido pode ser exportado individualmente

O PDF contém:

Dados do vendedor

Produtos e quantidades

Valores

Status do pedido

📌 Regras de Negócio

Vendedor visualiza apenas seus pedidos

Central visualiza todos os pedidos

Produtos inativos não podem ser usados em novos pedidos

Preço do produto é congelado no momento do pedido

Pedidos faturados não podem ser editados

Pagamentos não são processados no sistema

🔒 O que não faz parte do MVP

Pagamentos

Integração automática com sistemas fiscais

Notificações por e-mail

Relatórios avançados

Multi-empresa

🧪 Observações

Este projeto é um MVP, focado em validar o fluxo real do negócio.
Novas funcionalidades podem ser adicionadas conforme a evolução da necessidade do cliente.

📄 Licença

Projeto de uso privado, desenvolvido sob demanda.


---
