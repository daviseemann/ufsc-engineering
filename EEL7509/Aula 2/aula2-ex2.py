def avaliar_nota_aluno(nome, *notas):
    media = sum(notas) / len(notas)
    if media >= 9:
        msg = "Excelente"
    elif media >= 7:
        msg = "Bom"
    elif media >= 5:
        msg = "Médio"
    else:
        msg = "Abaixo da média"

    print(f"O aluno {nome} teve média = {media}, o desempenho está {msg}")


avaliar_nota_aluno("joao", 10, 9, 10, 9)
avaliar_nota_aluno("jose", 10, 8, 10, 2)
avaliar_nota_aluno("diego", 6)
avaliar_nota_aluno("george", 4)
