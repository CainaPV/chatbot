import os
import datetime


def chat():
    print("Olá, Bem-vindo ao Top 4 Curiosidades sobre mim!")
    while True:
        try:
            nome = input("Informe o seu Nome: ")
            if nome in " ":
                continue
            if nome.isalpha():
                pass
            else:
                print("Ops, Algo deu errado, informe o seu nome sem utilizar números!")
                continue
            email = input(
                f"{nome}, caso tenha interesse de ampliar o seu Network, informe o seu email para contato, caso contrário pule para próxima etapa.: ")
        except ValueError:
            pass
        while True:
            print("Escolha uma das opções abaixo que tenha interesse de saber sobre mim!")
            top = int(input(
                f" [1] - Nome Completo ?{os.linesep} [2] - Aniversário e Idade ? {os.linesep} [3] - Qual curso estou fazendo ? {os.linesep} [4] - Carreira profissional que pretendo seguir ? {os.linesep} Informe a sua opção: "))
            resposta(nome, top)

            while True:
                try:
                    sn = str(
                        input("Deseja continuar [S/N] ? ")).upper().strip()[0]
                    if sn == "S":
                        break
                    elif sn == "N":
                        print("Encerrando...")
                        return
                    else:
                        raise ValueError("Algo deu Errado!")
                except Exception as erro:
                    print(
                        f"Algo deu Errado! \nInforme [SIM] para continuar e [NÃO] para sair.")


def resposta(nome, top):
    ano = 2002
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano
    if top == 1:
        print(f"{os.linesep} Nome Completo: Cainã Pinhero Verona. {os.linesep}")
    elif top == 2:
        print(f"{os.linesep} {nome}, eu faço aniversário no dia 11/09 e no atual ano de {ano_atual} eu tenho {idade} anos.  {os.linesep}")
    elif top == 3:
        print(f"{os.linesep} {nome}, estou cursando Sistemas de Informação, me formo em 2025. {os.linesep}")
    elif top == 4:
        print(f"{os.linesep} {nome}, pretendo seguir na carreiro como Desenvolvedor Full Stack com foco em desenvolvimento Web,Banco de Dados e Automações.  {os.linesep}")


chat()
