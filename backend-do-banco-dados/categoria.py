from dataclasses import dataclass
from typing import Optional

@dataclass
class Categoria:
    categoria_id: int
    nome_categoria: str
    descricao_categoria: Optional[str]
    tipo_evento: str
    quantidade_categoria: int

if __name__ == "__main__":
    try:
        categoria_id = int(input("ID da Categoria: "))
        nome = input("Nome da Categoria: ")
        descricao = input("Descrição (Se voce quiser): ")
        tipo_evento = input("Tipo de Evento: ")
        quantidade = int(input("Quantidade de eventos nessa categoria: "))

        nova_categoria = Categoria(
            categoria_id=categoria_id,
            nome_categoria=nome,
            descricao_categoria=descricao or None,
            tipo_evento=tipo_evento,
            quantidade_categoria=quantidade
        )

        print("\nCategoria criada amigo:")
        print(nova_categoria)

    except ValueError:
        print("\nErro: ID e quantidade precisam ser números.")
