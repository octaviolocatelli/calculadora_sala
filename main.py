def soma():
    a = input("Digite o primeiro número a ser somado: ")
    b = input("Digite o segundo número a ser somado: ")
    print(a + b)
    print("Duda e Cauã, amor incondicional")

def subtracao(a,b):
    print(a-b)
    pass

def multiplicacao(a,b):
    a = input("Digite o primeiro número a ser multiplicado: ")
    b = input("Digite o segundo número a ser multiplicado: ")
    print(a * b)
    pass

def divisao(a,b):
    a = float(input('numerador:'))
    b = float(input('denominador'))
    if b == 0:
        print('não é possível dividir por 0')
    else:
        resultado = a/b
        print(resultado)

    pass

def exponencial(a,b):
    #arthur
    pass

def raiz(a,b):
    def raiz(a, b):

        if a == 0:
            return "Erro: O índice (a) não pode ser zero."

        if b < 0 and a % 2 == 0:
            return f"Erro: Não é possível calcular raiz de índice par ({a}) de um número negativo ({b})."

        try:
            resultado = b ** (1 / a)
            return resultado

        except Exception as e:

            return f"Erro ao calcular a raiz: {e}"

    print("--- Calculadora de Raiz Geral (Raiz 'a' de 'b') ---")

    try:
        a_texto = input("Por favor, digite o ÍNDICE da raiz (ex: 2 para raiz quadrada): ")
        b_texto = input(f"Por favor, digite o NÚMERO (o valor dentro da raiz): ")

        a_utilizador = float(a_texto)
        b_utilizador = float(b_texto)

        resultado = raiz(a_utilizador, b_utilizador)
        print(f"O resultado é: {resultado}")

    except ValueError:
        print("Erro: Valores inválidos. Por favor, digite apenas números.")


def log(a,b):
    #mateus
    pass

def fatorial(a):
    "Calculando a fatorial do número a: FATORIAL = N x N-1 X N-2 X N-3 ..." 
    if a < 0: 
        return "Fatorial não existe"
    elif a == 0 or a == 1: 
        return 1 
    else: 
        resultado = 1 
        for i  in range (2, a + 1): 
            resultado *= i
        return resultado 
    
    print(f" fatorial de 5 = {fatorial(5)}") 
    pass
def area_cir(r):
    #paulo
    pass

def area_ret(a,b):
    B = float(input("Diga a base: "))
    H = float(input("Diga a altura: "))
    resultado = B * H
    print(resultado)
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
