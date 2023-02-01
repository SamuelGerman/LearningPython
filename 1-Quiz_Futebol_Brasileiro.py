nomeJogador ="abv"
numeroPergunta = 1
respostaJogador ="inicia"
gabarito = ["Palmeiras","Gremio","Fred, Diego Souza e Paulo Baier","Cruzeiro","Washington","Internacional"] # Lista que armazenará a resposta de cada pergunta, a posição na lista é a posição da pergunta no quiz.
perguntas = ["Qual o campeao brasileiro de 2022?\n","Qual o primeiro campeão da copa do Brasil?\n","Quem são os 3 maiores artilheiros do brasileirão na era dos pontos corridos?\n","Qual e o maior campeao da copa do brasil?\n","Quem fez mais gols em uma unica edicao do brasileirao de pontos corridos?\n","Qual foi o unico time a vencer o brasileirao de forma invicta?\n"]
acertos = 0
opcao ="a"
i=0

print("Bem vindo ao quiz sobre futebol brasileiro!\n")
nomeJogador = input("Informe o nome do jogador: ")

print(nomeJogador+", voce esta pronto para comecar o quiz?\n")
opcao = input("Digite (S) para começar a jogar\nDigite (N) para encerrar o quiz\n")
if(opcao == "S" or opcao =="s"):
    print("Comecando quiz\n")
    for i in range(0,5,1):
        print(perguntas[i])
        respostaJogador = input("Digite sua resposta: ")
        if(respostaJogador.lower() == gabarito[i].lower()):
            acertos+=1
            print("Parabens, voce acertou essa pergunta.\n")
        else:
            print("Voce errou esta pergunta. A resposta correta era "+gabarito[i])
    print("--------------------------------------------------------------------------------------\n")
    print("Fim do Quiz\nVoce acertou " +str(acertos)+" de "+str((i+1))+" possiveis")
    print("\nVoce acertou " +str(acertos/i *100 )+"% do quiz ")
