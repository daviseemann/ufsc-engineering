def process_arguments(**kwargs):
    for arg in kwargs:
        print(arg, kwargs[arg])
    if kwargs["operacao"] == "soma":
        # Sum all integer values
        result = sum(value for value in kwargs.values() if type(value) is int)
        print("resultado da soma:", result)

    elif kwargs["operacao"] == "multiplicacao":
        # Multiply all float values
        result = 1.0
        for value in kwargs.values():
            if value is float:
                result *= value
        print("resultado da multiplicacao:", result)


process_arguments(operacao="soma", a=1, b=2, c=3, d=4)
process_arguments(operacao="multiplicacao", a=1.1, b=2.1, c=3.4, d=0.6)
