
agendas = [] 

def cadastrar_agenda():
    print("Nova_Agendinha ")
    nova_agenda = {
        "nome_usuario": input("nome so usuario: "),
        "nome_agenda": input(" Nome para a agenda: "),
        "descricao": input("Descrição : "),
        "tamanho_agenda": 0  
    }
    agendas.append(nova_agenda)
    print(f"agenda '{nova_agenda['nome_agenda']}' criada para {nova_agenda['nome_usuario']}!")

def listar_agendas():
    print("Agendia")
    if not agendas:
        print("Nenhuma agenda cadastrada ainda.")
        return
    
    for i, agenda in enumerate(agendas, 1):
        print(f"\nAgenda {i}:")
        print(f"Dono: {agenda['nome_usuario']}")
        print(f"Nome: {agenda['nome_agenda']}")
        print(f"Descrição: {agenda['descricao']}")
        print(f"Total de itens: {agenda['tamanho_agenda']}")

l
while True:
    print("Criar Agenda")
    print("1. Criar nova agenda")
    print("2. Ver agendas")
    print("3. Sair")
    
    opcao = input("Escolha: ")
    
    if opcao == "1":
        cadastrar_agenda()
    elif opcao == "2":
        listar_agendas()
    elif opcao == "3":
        print("Até logo!")
        break
})
