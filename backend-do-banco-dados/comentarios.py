import datetime

comentarios = []

def agendinha_comentario():
    print("Comentario Do Mito ")
    tarefa_id = input("Nome Da Tarefa: ")
    tem_comentario = input("Tarefa tem comentário?  ")
    texto = input("Comentário: ")
    
    novo_comentario = {
        "tarefa_id": tarefa_id,
        "tarefa_tem_comentario": "Sim" if tem_comentario == "S" else "Não",
        "texto_comentario": texto,
        "data_comentario": datetime.datetime.now().strftime("%d/%m")
    }
    
    comentarios.append(novo_comentario)
    print("Comentário registrado com sucesso!")

def visualizar_comentarios():
    print("comentarios alheios")
    if not comentarios:
        print("ninguem comenteu kkkkk.")
        return
    
    for i, comentario in enumerate(comentarios, 1):
        print(f"Comentário #{i}")
        print(f"Tarefa ID: {comentario['tarefa_id']}")
        print(f"Tem comentário: {comentario['tarefa_tem_comentario']}")
        print(f"Data: {comentario['data_comentario']}") 
        print(f"Texto: {comentario['texto_comentario']}")


while True:
    print("tarefinha")
    print("1. comentar")
    print("2. Ver comentários")
    print("3. Sair da tarefinha")
    
    opcao = input("Escolha agora: ")
    
    if opcao == "1":
        agendinha_comentario()
    elif opcao == "2":
        visualizar_comentarios()
    elif opcao == "3":
        print("nao quer mais ver fofoca.")
        break
    else:
        print("Eita Deu problema .")
