
recorrencias = []
proximo_id = 1  

def adicionar_recorrencia(evento_id, tipo, intervalo, data_final):
    global proximo_id

    nova = {
        "recorrencia_id": proximo_id,
        "evento_id": evento_id,
        "tipo_da_recorrencia": tipo, 
        "intervalo": intervalo,
        "data_final_da_recorrencia": data_final
    }

    recorrencias.append(nova)
    print("recorrência adicionada com sucesso!")
    proximo_id += 1

def mostrar_recorrencias():
    print("Todas as recorrências cadastradas:")
    for r in recorrencias:
        print(f"ID: {r['recorrencia_id']}")
        print(f"Evento: {r['evento_id']}")
        print(f"Tipo: {r['tipo_da_recorrencia']}")
        print(f"Intervalo: {r['intervalo']}")
        print(f"Data final: {r['data_final_da_recorrencia']}")
        print("-" * 20)


# Luiz e esse e um exemplo de como vc faz aparecer algo no terminal , vc pode trocar tudo isso que ta dentro dos parenteses ,e colocar outra coisa .
adicionar_recorrencia(101, 'semanal', 1, '2008-04-11')
adicionar_recorrencia(102, 'mensal', 2, '2026-04-11')
mostrar_recorrencias()
