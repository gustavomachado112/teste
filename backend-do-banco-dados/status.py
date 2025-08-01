from dataclasses import dataclass

@dataclass
class Status:
    nome_evento: str
    nivel_urgencia: str
    tipo_evento: str
    nome_status: str
    descricao_status: str

def solicitar_nivel_urgencia():
  while True:
      print("\n--- Definição de Urgência ---")
      print("Agora bora classificar a urgência:")
      print("1 - Alta (É bem importante pra você!)")
      print("2 - Média (É importante, mas nem tanto...)")
      print("3 - Baixa (É algo que tu tem que fazer, mas tá levando pela barriga, né guri?)")
      
      nivel = input("Dê um nível de urgência para o teu status, né guri? (1, 2 ou 3): ")
      if nivel in ['1', '2', '3']:
          return {"1": "Alta", "2": "Média", "3": "Baixa"}[nivel]
      else:
          print("Bah, escolhe direito, guri! Tem que ser 1, 2 ou 3.")

print("\n--- Cadastro de Status da Tarefa ---")
nome_evento = input("Qual nome você dará a esse evento ou tarefa que você vai fazer, guri? Você vai fazer o que? ")

nivel_urgencia = solicitar_nivel_urgencia()

tipo_evento = input("\nQual é o tipo do evento? Aula, academia, festa, o que é? ")

print("\n--- Nome do Status ---")
nome_status = input("Digite o nome do status (Ex: Em andamento, Concluído): ")

print("\n--- Descrição do Status ---")
descricao_status = input("Descreva o status como se você estivesse em um restaurante: ")

status = Status(
 nome_evento=nome_evento,
 nivel_urgencia=nivel_urgencia,
 tipo_evento=tipo_evento,
 nome_status=nome_status,
 descricao_status=descricao_status
)


print("\n===== STATUS CRIADO COM SUCESSO PELO XANDÃO =====")
print(f"Evento/Tarefa: {status.nome_evento}")
print(f"Urgência: {status.nivel_urgencia}")
print(f"Tipo de Evento: {status.tipo_evento}")
print(f"Status: {status.nome_status}")
print(f"Descrição: {status.descricao_status}")
