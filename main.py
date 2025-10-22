def soma(a,b):
    #guilherme
    pass

def subtracao(a,b):
    #duda
    pass

def multiplicacao(a,b):
    #caua
    pass

def divisao(a,b):
    #melissa
    pass

def exponencial(a,b):
    #arthur
    pass

def raiz(a,b):
    #gabriel
    pass

def log(a,b):
    #mateus
    pass

def fatorial(a):
    #lucas
    pass

def area_cir(r):
    #paulo
    pass

def area_ret(a,b):
    #matheus
    pass

def exibir_menu():
    print("Escolha uma das opções:")
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("5 - Exponencial")
    print("6 - Raiz")
    print("7 - Log")
    print("8 - Fatorial")
    print("9 - Área círculo")
    print("10 - Área retângulo")
    print("11 - Sair")

while True:
    exibir_menu()
    opcao = input("Digite a opção desejada:")
    if opcao == "1":
        soma()
    elif opcao == "2":
        subtracao()
    elif opcao == "3":
        multiplicacao()
    elif opcao == "4":
        divisao()
    elif opcao == "5":
        exponencial()
    elif opcao == "6":
        raiz()
    elif opcao == "7":
        log()
    elif opcao == "8":
        fatorial()
    elif opcao == "9":
        area_cir()
    elif opcao == "10":
        area_ret()
    elif opcao == "11":
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")