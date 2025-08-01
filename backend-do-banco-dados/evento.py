from dataclasses import dataclass
from typing import Optional
import datetime

@dataclass
class Evento:
    evento_id: int
    agenda_id: int
    nome_evento: str
    data_inicio_evento: datetime.datetime
    data_fim_evento: Optional[datetime.datetime] = None

    def __str__(self):
        inicio_formatado = self.data_inicio_evento.strftime('%d/%m/%Y %H:%M')
        
        if self.data_fim_evento:
            if self.data_fim_evento.date() == self.data_inicio_evento.date():
                fim_formatado = self.data_fim_evento.strftime('%H:%M')
            else:
                fim_formatado = self.data_fim_evento.strftime('%d/%m/%Y %H:%M')
        else:
            fim_formatado = "Não informado"
        
        return (f"ID do Evento: {self.evento_id}\n"
                f"ID da Agenda: {self.agenda_id}\n"
                f"Nome do Evento: {self.nome_evento}\n"
                f"Início: {inicio_formatado}\n"
                f"Fim: {fim_formatado}\n")

if __name__ == "__main__":
    print("--- Crie seu Novo Evento na Agenda Inteligente! ---\n")

    try:
        ano_atual = datetime.datetime.now().year
        mes_atual = datetime.datetime.now().month

        evento_id = int(input("ID do evento: "))
        agenda_id = int(input("ID da agenda: "))
        nome_evento = input("Nome do evento/tarefa: ")

        print("\n--- INÍCIO da tarefa/evento (Ano e Mês são os atuais) ---")
        dia_inicio = int(input("Dia do início: "))
        hora_inicio = int(input("Hora do início: "))
        minuto_inicio = int(input("Minuto do início: "))
        
        data_inicio_obj = datetime.datetime(ano_atual, mes_atual, dia_inicio, hora_inicio, minuto_inicio)

        data_fim_obj = None 
        tem_fim = input("\nA tarefa/evento tem hora ou data de FIM? (s/n): ").lower()
        
        if tem_fim == 's':
            mesmo_dia = input("O FIM é no MESMO DIA do INÍCIO? (s/n): ").lower()
            if mesmo_dia == 's':
                print("--- FIM da tarefa/evento (mesmo dia) ---")
                hora_fim = int(input("Hora do fim: "))
                minuto_fim = int(input("Minuto do fim: "))
                data_fim_obj = datetime.datetime(ano_atual, mes_atual, dia_inicio, hora_fim, minuto_fim)
            else:
                print("--- FIM da Resenha (outro dia, mesmo mês/ano) ---")
                dia_fim = int(input("Dia do fim: "))
                hora_fim = int(input("Hora do fim: "))
                minuto_fim = int(input("Minuto do fim: "))
                data_fim_obj = datetime.datetime(ano_atual, mes_atual, dia_fim, hora_fim, minuto_fim)

        novo_evento = Evento(
            evento_id=evento_id,
            agenda_id=agenda_id,
            nome_evento=nome_evento,
            data_inicio_evento=data_inicio_obj,
            data_fim_evento=data_fim_obj
        )

        print("\n--- Evento da galera , Feito piazada . ---")
        print(novo_evento)

    except ValueError:
        print("\nErro: Por favor, digite APENAS números inteiros onde solicitado.")

    print("\n--- Xandao vai ficar feliz , ele esta orgulhoso! ---")
