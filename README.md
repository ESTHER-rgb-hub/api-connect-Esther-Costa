# API-Connect

## 🎯 Objetivo
Esta API foi desenvolvida como MVP para gerenciamento de usuários.  
Ela permite criar, listar, buscar, atualizar e excluir registros de usuários, servindo como base para aplicações maiores.

---

## 🛠️ Tecnologias utilizadas
- **Python 3.12**
- **Flask** (framework web)
- **Thunder Client / Postman / Insomnia** (testes de API)
- **Git + GitHub** (versionamento e compartilhamento)

---

## 🚀 Como executar localmente

### 1. Clonar o repositório

git clone https://github.com/ESTHER-rgb-hub/api-connect-Esther-Costa.git
cd api-connect-Esther-Costa

### 2. Criar ambiente virtual

python -m venv venv

### 3. Ativar ambiente virtual
   
Windows (PowerShell):
.\venv\Scripts\activate
Linux/Mac:
source venv/bin/activate

### 4. Instalar dependências

pip install -r requirements.txt

### 5. Rodar servidor
   
python run.py

Servidor disponível em:
http://127.0.0.1:5000/

## 📌 Endpoints da API
Método	Rota	Descrição	Exemplo de corpo JSON
GET	/users	Lista todos os usuários	—
POST	/users	Cria novo usuário	{ "name": "Ana", "email": "ana@email.com" }
GET	/users/<id>	Busca usuário por ID	—
PUT	/users/<id>	Atualiza usuário existente	{ "name": "Novo Nome" }
DELETE	/users/<id>	Remove usuário	—

## ✅ Exemplos de testes
Criação com sucesso: POST /users com nome e email → 201 Created

Falha na criação: POST /users sem email → 400 Bad Request

Listagem geral: GET /users → 200 OK

Falha na busca: GET /users/999 → 404 Not Found

Esther Costa da Silva 
Universidade Cruzeiro do sul 
Ciência da computação
