from dataclasses import dataclass
from typing import Optional

@dataclass
class Usuario:
    usuario_id: int
    nome_completo: str
    email: str
    senha: str
    telefone: Optional[int] = None
    cpf: Optional[int] = None

    def __str__(self):
        return (f"ID do Usuário: {self.usuario_id}\n"
                f"Nome Completo: {self.nome_completo}\n"
                f"Email: {self.email}\n"
                f"Senha: ********\n"
                f"Telefone: {self.telefone if self.telefone is not None else 'Não informado'}\n"
                f"CPF: {self.cpf if self.cpf is not None else 'Não informado'}\n")

if __name__ == "__main__":
    print("--- Criar Novo Usuário ---")

    try:
        usuario_id = int(input("ID do Usuário: "))
        nome_completo = input("Nome Completo: ")
        email = input("Email: ")
        senha = input("Senha: ")

        telefone_input = input("Telefone (se não quiser, só dar Enter para pular): ")
        telefone = int(telefone_input) if telefone_input else None

        cpf_input = input("CPF (se não quiser, só dar Enter para pular): ")
        cpf = int(cpf_input) if cpf_input else None

        novo_usuario = Usuario(
            usuario_id=usuario_id,
            nome_completo=nome_completo,
            email=email,
            senha=senha,
            telefone=telefone,
            cpf=cpf
        )

        print("\n--- Usuário está no sistema ---")
        print(novo_usuario)

    except ValueError:
        print("\nErro: apenas números, amigo.")
    except Exception as e:
        print(f"\nOcorreu um erro: {e}")

    print("\n--- Acabou xandão, está feliz. ---")
