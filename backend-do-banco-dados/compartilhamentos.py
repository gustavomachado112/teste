from dataclasses import dataclass

@dataclass
class Compartilhamento:
    compartilhamento_id: int
    agenda_id: int
    usuario: str
    compartilhar_tarefa: str
    permissao: str 
def cadastrar_compartilhamento():
    try:
        compartilhamento_id = int(input("ID da tarefa que voce quer compartilhar: "))
        agenda_id = int(input("ID da Agenda: "))
        usuario = input("Usuário: ")
        compartilhar_tarefa = input("Compartilhar tarefa (nome da tarefa): ")
        permissao = input("Permissão (leitura, escrita ou total): ").lower()

        permissoes_validas = ["leitura", "escrita", "total"]
        if permissao not in permissoes_validas:
            print("negado , so pode usar leitura , escritaou totla")
            return

        compartilhamento = Compartilhamento(
            compartilhamento_id=compartilhamento_id,
            agenda_id=agenda_id,
            usuario=usuario,
            compartilhar_tarefa=compartilhar_tarefa,
            permissao=permissao
        )

        print("\nCompartilhamento feito com sucesso , xandao esta feliz com voce!")
        print(compartilhamento)

    except ValueError:
        print("Erro: digite numero validos , se nao xandao fica triste")
