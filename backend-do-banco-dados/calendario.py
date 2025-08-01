from dataclasses import dataclass

@dataclass
class Calendario:
    calendario_id: int
    usuario_id: int
    nome_calendario: str
    descricao_calendario: str
    link: str

def cadastrar_calendario():
    try:
        calendario_id = int(input("ID do Calendário: "))
        usuario_id = int(input("ID do Usuário: "))
        nome = input("Nome do Calendário: ")
        descricao = input("Descrição do Calendário: ")
        link = input("Link do Calendário (opcional): ")

        calendario = Calendario(
            calendario_id=calendario_id,
            usuario_id=usuario_id,
            nome_calendario=nome,
            descricao_calendario=descricao,
            link=link
        )

        print("\nCalendário cadastrado com sucesso:")
        print(calendario)

    except ValueError:
        print("\nErro: Os campos de ID precisam ser números inteiros.")

if __name__ == "__main__":
    cadastrar_calendario()
