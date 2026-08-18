# Estrutura de dados em memória para simular persistência
users = []

# Função para gerar IDs incrementais
def generate_id():
    if users:
        # Pega o último ID e soma 1
        return users[-1]["id"] + 1
    else:
        # Primeiro usuário começa com ID 1
        return 1
