
sicronizacoes = []
proximo_id = 1

def adicionar_sicronizacao(usuario_id, tipo_servico, token_acesso, sicronizacao_data):
    global proximo_id

    nova = {
        "sicronizacao_id": proximo_id,
        "usuario_id": usuario_id,
        "tipo_servico": tipo_servico,
        "token_acesso": token_acesso,
        "sicronizacao": sicronizacao_data
    }

    sicronizacoes.append(nova)
    print("Estamos fazendo sua sicronicacao, aguarde um pouco chefe.")
    proximo_id += 1

def mostrar_sicronizacoes():
    print("\n Todas as sicronizações:")
    for s in sicronizacoes:
        print(f"ID: {s['sicronizacao_id']}")
        print(f"Usuário ID: {s['usuario_id']}")
        print(f"Tipo de serviço: {s['tipo_servico']}")
        print(f"Token de acesso: {s['token_acesso']}")
        print(f"Data/Hora da sicronização: {s['sicronizacao']}")
        print("-" * 30)


# Mesma coisa dos 2 ultimos .
adicionar_sicronizacao(1, "Drive do google", "saopauloseireb", "25-09-11 16:45:00")
adicionar_sicronizacao(2, "draw.io", "Lula1234LL", "25-04-29 14:37:45")
mostrar_sicronizacoes()
