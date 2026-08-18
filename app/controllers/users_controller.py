from app.data.users_data import users, generate_id

# Função para listar todos os usuários
def list_users():
    return users

# Função para criar um novo usuário
def create_user(name, email):
    new_user = {
        "id": generate_id(),
        "name": name,
        "email": email
    }
    users.append(new_user)
    return new_user
