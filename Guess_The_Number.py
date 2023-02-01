'''
"Escreva um programa em Python que permita ao usuário adivinhar um número inteiro escolhido aleatoriamente pelo computador. 
O programa deve exibir mensagens ao usuário indicando se o número escolhido é maior ou menor do que o número adivinhado pelo usuário. 
O programa deve continuar pedindo ao usuário para adivinhar até que ele acerte o número correto, e então exibir uma mensagem de 
sucesso e o número de tentativas que foram necessárias."
'''
import random

chute =-1;
tentativas = 0
opcao = int(input("Informe a dificuldade do jogo\nDigite (1) Para ter que adivinhar um numero de 0 a 10\nDigite (2) para ter que adivinhar um numero de 0 a 100\nDigite (3) para ter que adivinhar um numero de 0 a 1000\n"))
num = random.randint(0,10**opcao)
acertou = False

while acertou == False:
    chute = int(input("Chute um numero entre 0 e "+str(10**opcao)+ " : "))
    if(chute == num):
        print("Parabens, voce acertou o número em "+str(tentativas)+ " tentativas")
        acertou = True
    elif(chute<num):
        print("O numero secreto é maior que "+str(chute))
        tentativas+=1
    elif(chute > num):
        print("O numero secreto é menor que "+str(chute))
        tentativas+=1;

