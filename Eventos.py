# criar_evento
# listar_eventos
# reservar_vaga
# cancelar_reserva
# visualizar_detalhes_evento
# salvar_dados
# carregar_dados


def criar_evento (eventos, nome, data, capacidade,localizacao):
    novo_evento = {}
    novo_evento ["data"] = data
    novo_evento ["capacidade"] = capacidade
    novo_evento ["localização"] = localizacao

    eventos[nome] = novo_evento



def reserva_eventos():
    while True:
        print("\n__EVENTOS__\n")
        print("1. - criar evento")
        print("2. - listar eventos")
        print("3. - reservar vaga")
        print("4. - cancelar reserva")
        print("5. - visualizar detalhes do evento")
        print("8. - sair\n")   
        user_op = input("Escolha uma opção:")

        if user_op == "1":
            nome_evento = input ("Nome do evento: ")
            if nome_evento not in eventos:
                data_evento = input("Data do evento: ")
                capacidade_evento = input("Qual a capacidade máxima de pessoas no evento: ")
                localizacao_evento = input("Onde o evento será realizado: ")
                criar_evento(eventos, nome_evento, data_evento, capacidade_evento, localizacao_evento)
            else:
                print(f"Evento {nome_evento} já existe!")
if __name__ == "__main__":
    reserva_eventos()