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

# Menu: Carlos
