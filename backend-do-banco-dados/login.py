

usuarios = {}

print("Sistema de login da agendinha")
print("Cadastro")

nome_usuario = input("Nome de usuário: ")
email = input("Email: ")
cpf = input("CPF : ")
telefone = input("Telefone : ")
senha = input("Crie sua senha: ")


usuario_existente = False
for user in usuarios.values():
    if user['email'] == email:
        print("Erro: Email já cadastrado(Faz o L")
        usuario_existente = True
        break
    if user['cpf'] == cpf:
        print("Erro: CPF já cadastrado!")
        usuario_existente = True
        break
    if user['nome_usuario'].lower() == nome_usuario.lower():
        print("Erro: Nome de usuário já existe(tenha criatividade)")
        usuario_existente = True
        break

if not usuario_existente:
    usuarios[email] = {
    'nome_usuario': nome_usuario,
    'cpf': cpf,
    'telefone': telefone,
'senha': senha
    }
    print("Login")
    print(f"Bem-vindo(a), {nome_usuario} ")
    print(f"Username: {nome_usuario}")
    print(f"Email: {email}")
    print(f"CPF: {cpf}")
    print(f"Telefone: {telefone}")
    print("voce fez o cadastro e o login ja .")
