from datetime import datetime

notificacoes_tb = []

def adicionar_notificacao(notificacao_id, usuario_id, evento_id, mensagem_notificacao, data_hora_notificacao):
 notificacoes_tb.append({
 "notificacao_id": notificacao_id,
 "usuario_id": usuario_id,
 "evento_id": evento_id,
 "mensagem_notificacao": mensagem_notificacao,
 "data_hora_notificacao": data_hora_notificacao
 })
# professor nesse dois adicionar e aonde voce muda a informacao que vai pro terminal , entao voce pode colocar qualquer hora , numero ou nome nele.
adicionar_notificacao(1, 101, 504, "Evento disponível!", "2025-07-23 16:30:00")
adicionar_notificacao(2, 102, 504, "Seu evento começa em 1h.", "2025-07-23 17:00:00")

print("Notificações:")
for n in notificacoes_tb:
 print("ID:",n["notificacao_id"])
 print("Usuario:",n["usuario_id"])
 print("Evento:",n["evento_id"])
 print("Mensagem:",n["mensagem_notificacao"])
 print("Data:",n["data_hora_notificacao"])
 print()
