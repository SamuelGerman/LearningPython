'''
Esse é o código de uma aplicação de gerenciamento de estoque, que consiste em duas classes:
"Estoque" e "Produto". A classe "Estoque" tem como responsabilidade gerenciar a lista de produtos,
com métodos como adicionar_produto, remover_produto, verificar_produtos_em_falta, etc. Já a classe "Produto"
define um produto com seus atributos, como nome, preço, quantidade em estoque e código do produto. Ela também possui 
um método adicionar_estoque para aumentar a quantidade em estoque do produto, e outro método remover_estoque para diminuir 
a quantidade em estoque.
'''
class Estoque: #estoque é uma lista de produtos
    def __init__(self):
        self.produtos = []
        return None

    def add_novo_produto(self,produto): 
    # se achar um produto ja estocado com o mesmo nome do novo produto ele nao será adicionado.
        for item in self.produtos:
            if produto.nome_produto.lower() == item.nome_produto.lower:
                print("Produto com o mesmo nomne ja consta no estoque")
                return 1
        self.produtos.append(produto)
        print("O produto",produto.nome_produto,"foi adicionado ao estoque")
        return 1

    def remover_produto_estoque(self,codigo_produto):#tira um produto do estoque.
    #acha o produto que sera removido baseado no codigo que o usuario colocará, caso nao ache um produto com o codiog fornecido, nada sera removido
        for item in self.produtos:
            if int(item.codigo_produto)==int(codigo_produto):
                print("O produto",item.nome_produto,"foi removido do estoque")
                self.produtos.remove(item)
        return 1

    def verificar_produtos_faltando(self):
    #adiciona os produtos que possuem zero unidades em estoque em uma lista de produtos em falta e depois retorna essa lista
        prod_em_falta = []
        tem_faltando = False
        for produto in self.produtos:
            if produto.quantidade_estoque == 0:
                tem_faltando = True
                prod_em_falta.append(produto)
        if tem_faltando == True:
            for item in prod_em_falta:
                print(item.nome_produto,"esta em falta!")
            return prod_em_falta
        else:
            print("Nenhum produto está em falta.")
            return 1

    def printar_estoque(self):
        print("--------------------------------------------------")
        for item in self.produtos:
            print("Nome:",item.nome_produto)
            print("Quantidade em estoque:",item.quantidade_estoque)
            print("Preco:",item.preco)
            print("Codigo:",item.codigo_produto)
            print("--------------------------------------------------")
        return 1
    
    def informar_valor_total_estoque(self):
        valor_total =0.00
        for item in self.produtos:
            valor_total += item.quantidade_estoque * item.preco
        return valor_total

class Produto:
    def __init__(self,nome_produto,quantidade_estoque,preco,codigo_produto):
        self.nome_produto = nome_produto
        self.quantidade_estoque = quantidade_estoque
        self.preco = preco
        self.codigo_produto = codigo_produto
        return None
    
    def adicionar_estoque(self,codigo_produto,quantidade,lista_produtos):
    #adiciona x unidades de um produto baseado no codigo que o usuario pedir
        for item in lista_produtos:
            if int(item.codigo_produto) == codigo_produto:
                item.quantidade_estoque+= quantidade
                print("Adicionado",quantidade,item.nome_produto)
                return 1
        print("Item nao registrado no estoque.")
        return 0

    def remover_estoque(self,codigo_produto,quantidade,lista_produtos):
        for item in lista_produtos:
            if int(item.codigo_produto) == codigo_produto:
                if int(item.quantidade_estoque) - quantidade < 0:
                    print("Nao foi possivel remover",quantidade,item.nome_produto,"pois so existem",item.quantidade_estoque,"disponiveis")
                    return 1
                elif int(item.quantidade_estoque) - quantidade >= 0:
                    item.quantidade_estoque -= quantidade
                    print(quantidade,item.nome_produto,"retirados com sucesso do estoque. Voce tem",item.quantidade_estoque,"restantes")
                    return 1
                else:
                    print("Item nao encontrado no estoque.")
                    return 0

    def verificar_dados_produto(self,codigo_produto,lista_produtos):
        for item in lista_produtos:
            if int(item.codigo_produto) == codigo_produto:
                print("--------------------------------------------------")
                print("Nome:",item.nome_produto)
                print("Quantidade em estoque:",item.quantidade_estoque)
                print("Preco:",item.preco)
                print("Codigo:",item.codigo_produto)
                print("--------------------------------------------------")
        return 1

#inicializando os produtos.
arquivo = open("Produtos.txt", "r")
linhas = arquivo.readlines() # a função retorna uma lista de string, onde cada string é uma linha do arquivo
arquivo.close()
estoque = Estoque()
codigo = 0

for item in linhas:
    campos = item.strip().split(",") #divide a linha em strings separadas por virgulas e retorna todas as substrings recortadas
    nome_produto = campos[0]
    quantidade_estoque = int(campos[1])
    preco = float(campos[2])
    codigo_produto = campos[3]
    produto = Produto(nome_produto,quantidade_estoque,preco,codigo_produto)
    estoque.add_novo_produto(produto)
    codigo += 1 # a cada vez que um produto é adicionado o codigo aumenta para saber qual foi o ultimo codigo definido

opcao = -1
while opcao !=0:
    print("\n ---------- MENU ----------\n")
    print("1. Visualizar o estoque") #printar_estoque()
    print("2. Adicionar um produto ja registrado no estoque") #adicionar_estoque()
    print("3. Retirar um produto ja registrado no estoque do estoque")   #remover_estoque()
    print("4. Verificar dados de um produto no estoque") #verificar_quantia_estoque()
    print("5. Registrar um produto novo no estoque ") #add_novo_produto(self,produto):
    print("6. Excluir um produto do estoque ") #remover_produto_estoque(self,produto)
    print("7. Verificar produtos em falta no estoque ") #verificar_produtos_faltando(self):
    print("8. Informar o valor total do estoque") #buscar_produto(self,codigo_produto):
    print("0. Sair")
    opcao = int(input("Digite sua escolha: "))
    if opcao == 1:
        estoque.printar_estoque()
    elif opcao == 2:
        codigo_produto = int(input("Informe o codigo do produto que sera adicionado: "))
        quantidade = int(input("Informe a quantidade do produto que sera adicionado: "))
        produto.adicionar_estoque(codigo_produto,quantidade,estoque.produtos)
    elif opcao == 3:
        codigo_produto = int(input("Informe o codigo do produto que sera retirado: "))
        quantidade = int(input("Informe a quantidade do produto que sera retirado: "))
        produto.remover_estoque(codigo_produto,quantidade,estoque.produtos)
    elif opcao == 4:
        codigo_produto =  int(input("Informe o codigo do produto que sera verificado: "))
        produto.verificar_dados_produto(codigo_produto,estoque.produtos)
    elif opcao == 5:
        codigo += 1
        nome_produto = input("Informe o nome do novo produto: ")
        quantidade_estoque = int(input("Informe a quantidade que sera adicionada do novo produto: "))
        preco =float(input("Informe o preco do novo produto: "))
        codigo_produto = codigo
        produto = Produto(nome_produto,quantidade_estoque,preco,codigo_produto)
        estoque.add_novo_produto(produto)
    elif opcao == 6:
        codigo_produto = input("Informe o codigo do produto que deseja remover: ")
        estoque.remover_produto_estoque(codigo_produto)
    elif opcao == 7:
        estoque.verificar_produtos_faltando()
    elif opcao == 8:
            valor = estoque.informar_valor_total_estoque()
            print("O valor total do estoque atualmente e de",valor,"reais")
    elif opcao == 0:
        print("Atualizando arquivo de estoque...")
        arquivo = open("Produtos.txt","w")
        for item in estoque.produtos:
            arquivo.write(item.nome_produto)
            arquivo.write(", ")
            arquivo.write(str(item.quantidade_estoque))
            arquivo.write(", ")
            arquivo.write(str(item.preco))
            arquivo.write(", ")
            arquivo.write(str(item.codigo_produto))
            arquivo.write("\n")
            arquivo.close()
        print("Saindo...")
    else:
        print("Opção inválida, escolha novamente.")
