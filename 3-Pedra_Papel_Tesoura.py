'''Desenvolva um programa em Python que simule o jogo "Pedra, Papel, Tesoura". O programa deve permitir que o usuário faça 
uma jogada e escolha entre "Pedra", "Papel" ou "Tesoura". O programa também deve gerar uma jogada aleatória para o computador. 
Em seguida, o programa deve comparar as jogadas do usuário e do computador e informar qual jogada ganhou. O jogo deve ser repetido 
até que o usuário decida sair. Além disso, o programa deve contar o número de vitórias, empates e derrotas do usuário e exibir 
essas informações ao final do jogo.'''

import random
vitorias_usuario = 0
vitorias_maquina = 0
empates = 0

possiveis_jogadas = ["pedra","papel","tesoura"]

while True:
    opcao = input("Escolha Pedra, Papel, ou Tesoura para jogar ou digite 'Q' para parar de jogar: ").lower() #pega a string toda minuscula da resposta
    if opcao == 'q':
        break
    elif opcao not in possiveis_jogadas:
        # volta para o inicio do loop
        continue
    else:
        jogada_maquina = possiveis_jogadas[random.randint(0,2)] # vai escolher um dos indices da lista de possiveis jogadas
        # 0 = pedra , 1 = papel , 2 = tesoura.
        if opcao == "pedra" and jogada_maquina == "tesoura":
            print("A maquina jogou",jogada_maquina)
            print("Usuario venceu!")
            vitorias_usuario+=1
        elif opcao == "papel" and jogada_maquina == "pedra":
            print("A maquina jogou",jogada_maquina)
            print("Usuario venceu!")
            vitorias_usuario+=1
        elif opcao == "tesoura" and jogada_maquina =="papel":
            print("A maquina jogou",jogada_maquina)
            print("Usuario venceu!")
            vitorias_usuario+=1
        elif opcao == jogada_maquina:
            print("A maquina jogou",jogada_maquina)
            print("Empate!")
            empates+=1
        else:
            vitorias_maquina+=1
            print("A maquina jogou",jogada_maquina)
            print("Computador venceu!")
print("O usuario venceu",vitorias_usuario,"vezes")
print("A maquina venceu",vitorias_maquina,"vezes")
print("Os jogadores empataram ",empates,"vezes")
