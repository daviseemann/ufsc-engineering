def converter_string(valor):
    if valor.startswith("0b"):
        return int(valor, 2)
    elif valor.startswith("0o"):
        return int(valor, 8)
    elif valor.startswith("0x"):
        return int(valor, 16)
    else:
        return int(valor)


valores = ["10", "0b10", "0o10", "0x10"]
resultado = list(map(converter_string, valores))
print(list(resultado))
