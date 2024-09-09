def calcular_despesa(custo_total, desconto=0, imposto=0):
    custo_final = ((1 + imposto) * custo_total) * (1 - desconto)
    return custo_final


print(calcular_despesa(100, 0.25, 0.15))
