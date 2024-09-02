def aplicar_funcao(valor_1, lista_funcoes):
    resultados = []
    for funcao in lista_funcoes:
        valor = funcao(valor_1)
        resultados.append(valor)
    print(resultados)


def addition(num1):
    return num1 + 10


def subtraction(num1):
    return num1 - 2


def multiplication(num1):
    return num1 * 7


def division(num1):
    return num1 / 4


###
# Testando a função aplicar_funcao
###
lista_funcoes = [addition, subtraction, multiplication, division]
aplicar_funcao(3, lista_funcoes)
aplicar_funcao(3, lista_funcoes)
aplicar_funcao(3, lista_funcoes[:3])
