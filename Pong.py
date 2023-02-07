#Jogo de ping pong simples

import turtle # para gerar imagens gráfica
#funções para o jogo
def raquete_a_cima():
    y=raquete_a.ycor() #recebe a coordenada y da raquete
    y+= 20 #aumenta 20 pixels da coordenada y
    if y <= 300:
        raquete_a.sety(y)

def raquete_a_baixo():
    y=raquete_a.ycor()
    y-= 20
    if y >=-300:
        raquete_a.sety(y)

def raquete_b_cima():
    y=raquete_b.ycor() #recebe a coordenada y da raquete
    y+= 20 #aumenta 20 pixels da coordenada y
    if y <= 300:
        raquete_b.sety(y)

def raquete_b_baixo():
    y=raquete_b.ycor()
    y-= 20
    if y >=-300:
        raquete_b.sety(y)


janela = turtle.Screen() #cria a janela onde o jogo aparece
janela.title("Ping Pong") #da nome para a janela
janela.bgcolor("black")  #cor de fundo
janela.setup(width=800,height=600)
janela.tracer(0) # impede a janela de atualizar sozinha.

#definindo atalhos do teclado
janela.listen() # faz o jogo esperar ação de teclas do teclado
janela.onkeypress(raquete_a_cima,"w")  #ao pressionar w, a função chama raquete_a_cima sera ativada.
janela.onkeypress(raquete_a_baixo,"s")

janela.onkeypress(raquete_b_cima,"Up")  #ao pressionar w, a função chama raquete_a_cima sera ativada.
janela.onkeypress(raquete_b_baixo,"Down")

#placar
pontos_a = 0
pontos_b = 0

#Raquete a
raquete_a = turtle.Turtle() # recebe um objeto do modulo turtle
raquete_a.speed(0) #velocidade de animação no maximo
raquete_a.shape("square") #
raquete_a.shapesize(stretch_wid=5,stretch_len=1) #transforma em um retangulo
raquete_a.color("white")    #cor
raquete_a.penup()   #nao desenha traços por onde anda
raquete_a.goto(-350,0)

#Raquete b
raquete_b = turtle.Turtle() # recebe um objeto do modulo turtle
raquete_b.speed(0) #velocidade de animação no maximo
raquete_b.shape("square") #
raquete_b.shapesize(stretch_wid=5,stretch_len=1) #transforma em um retangulo
raquete_b.color("white")    #cor
raquete_b.penup()   #nao desenha traços por onde anda
raquete_b.goto(350,0)

#bola
bola = turtle.Turtle() # recebe um objeto do modulo turtle
bola.speed(0) #velocidade de animação no maximo
bola.shape("circle") #
bola.color("white")    #cor
bola.penup()   #nao desenha traços por onde anda
bola.goto(0,0)
bola.dx = 0.3
bola.dy = 0.3

#caneta obj turtle
caneta = turtle.Turtle()
caneta.speed(0)
caneta.color("white")
caneta.penup()
caneta.hideturtle()
caneta.goto(0,260)
caneta.write("{} - {}".format(pontos_a, pontos_b),align="center",font=("Courier",24,"normal"))


#loop principal
while True:
    janela.update() # att janela toda iteração

    #mexe a bola
    bola.setx(bola.xcor()+bola.dx)
    bola.sety(bola.ycor()+bola.dy)
    if bola.ycor() > 290:
         bola.dy *=-1
    elif bola.ycor() < -290:
        bola.dy *=-1
    
    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        pontos_a += 1
        caneta.clear()
        caneta.write("{} - {}".format(pontos_a, pontos_b),align="center",font=("Courier",24,"normal"))
        
    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        pontos_b += 1
        caneta.clear()
        caneta.write("{} - {}".format(pontos_a, pontos_b),align="center",font=("Courier",24,"normal"))
    
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < raquete_b.ycor() + 40 and bola.ycor() > raquete_b.ycor() - 40): #verifica se a bola esta em contato com a raquete
        bola.setx(340) #bola vai pro meio do jogo
        bola.dx += 0.001
        bola.dx *=-1
    if (bola.xcor() < - 340 and bola.xcor() > -350) and (bola.ycor() < raquete_a.ycor() + 40 and bola.ycor() > raquete_a.ycor() - 40): #verifica se a bola esta em contato com a raquete
        bola.setx(-340)
        bola.dx *=-1
        bola.dx += 0.001
    
    if pontos_a == 10 or pontos_b == 10: #encerra o jogo quando alguem atinge 10 pontos.
        exit(1)
