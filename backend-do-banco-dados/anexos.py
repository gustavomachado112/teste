from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Anexo:
    anexo_id: int
    evento_id: Optional[int] 
    tarefa_id: Optional[int]  
    nome_arquivo: str
    tipo_arquivo: str
    tamanho_arquivo: str


class GerenciadorAnexos:
    def __init__(self):
        self.anexos: List[Anexo] = []

    def adicionar_anexo(self, evento_id: Optional[int], tarefa_id: Optional[int],
                        nome_arquivo: str, tipo_arquivo: str, tamanho_arquivo: str):
        novo_id = len(self.anexos) + 1
        anexo = Anexo(anexo_id=novo_id,
                      evento_id=evento_id,
                      tarefa_id=tarefa_id,
                      nome_arquivo=nome_arquivo,
                      tipo_arquivo=tipo_arquivo,
                      tamanho_arquivo=tamanho_arquivo)
        self.anexos.append(anexo)
        print(f"Anexo '{nome_arquivo}' adicionado com sucesso!")

    def listar_anexos(self):
        for anexo in self.anexos:
            print(f"[{anexo.anexo_id}] {anexo.nome_arquivo} - {anexo.tipo_arquivo} ({anexo.tamanho_arquivo})")

    def buscar_anexos_por_evento(self, evento_id: int):
        return [anexo for anexo in self.anexos if anexo.evento_id == evento_id]

    def buscar_anexos_por_tarefa(self, tarefa_id: int):
        return [anexo for anexo in self.anexos if anexo.tarefa_id == tarefa_id]
# Luiz e esse codigo abaixo e um exmeplo de uso pra poder aparecer algo depois que der run no codigo , por exemplo vc pode colocar qualquer outra coisa  , nome do arquitvo  o tipo do arquivo e etc .
gerenciador = GerenciadorAnexos()
gerenciador.adicionar_anexo(
    evento_id=1,
    tarefa_id=None,
    nome_arquivo="aulaxandao.PDF",
    tipo_arquivo="PDF",
    tamanho_arquivo="100Teras"
)
gerenciador.listar_anexos()
