from dataclasses import dataclass

@dataclass
class Prioridade:
    propriedade_id: int
    nome_prioridade: str
    nivel_urgencia: str
    descricao_prioridade: str
    lista_prioridade: str

def cadastrar_prioridade():
    try:
        propriedade_id = int(input("ID da Prioridade: "))
        nome = input("Nivel da Prioridade (E: Alta, Média, Baixa): ")
        nivel = input("Nível de Urgência (E: urgente, moderado, baixo): ")
        descricao = input("Descreva a  Prioridade: ")
        lista = input("Nome da Lista que essa prioridade pertence: ")

        prioridade = Prioridade(
            propriedade_id=propriedade_id,
            nome_prioridade=nome,
            nivel_urgencia=nivel,
            descricao_prioridade=descricao,
            lista_prioridade=lista
        )

        print("\nPrioridade cadastrada com sucesso:")
        print(prioridade)

    except ValueError:
        print("\nErro: O ID precisa ser um número inteiro por favor.")


if __name__ == "__main__":
    cadastrar_prioridade()
