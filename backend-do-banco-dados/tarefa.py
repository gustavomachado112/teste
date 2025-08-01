from dataclasses import dataclass
from typing import Optional
import datetime

@dataclass
class Tarefa:
    tarefa_id: int
    usuario_id: int
    nome_tarefa: str
    data_expirar: Optional[datetime.datetime] = None
    descricao_tarefa: Optional[str] = None

    def __str__(self):
        data_formatada = self.data_expirar.strftime('%d/%m/%Y %H:%M') if self.data_expirar else "Sem prazo"
        return (f"ID da Tarefa: {self.tarefa_id}\n"
                f"Usuário: {self.usuario_id}\n"
                f"Título: {self.nome_tarefa}\n"
                f"Prazo: {data_formatada}\n"
                f"Detalhes: {self.descricao_tarefa}\n")

def criar_tarefa():
    print("Cadastro de nova tarefa:\n")
    try:
        tarefa_id = int(input("ID da tarefa: "))
        usuario_id = int(input("ID do usuário: "))
        nome_tarefa = input("Nome da tarefa: ")

        prazo_input = input("Data de expiração (dd/mm/aaaa HH:MM) ou deixe vazio para sem prazo: ")
        if prazo_input:
            data_expirar = datetime.datetime.strptime(prazo_input, '%d/%m/%Y %H:%M')
        else:
            data_expirar = None

        descricao_tarefa = input("Descrição da tarefa (so se voce quiser): ") or None

        tarefa = Tarefa(
            tarefa_id=tarefa_id,
            usuario_id=usuario_id,
            nome_tarefa=nome_tarefa,
            data_expirar=data_expirar,
            descricao_tarefa=descricao_tarefa
        )

        print("\nTarefa cadastrada com sucesso:")
        print(tarefa)
    except ValueError:
        print("Erro: dados estao errados arume pfvr ,  tente novamente com os formatos certos.")

if __name__ == "__main__":
    criar_tarefa()
