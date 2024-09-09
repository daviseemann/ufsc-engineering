notas = {}
while True:
    print(
        """
                a) incluir nota\n
                b) excluir nota\n
                c) mostrar média da turma\n
                d) sair do programa
                """
    )
    opcao = input("Digite a opção desejada: ")
    if opcao == "a":
        nome = input("Digite o nome do aluno: ")
        nota = input("Digite a nota do aluno: ")
        notas[nome] = nota
        continue
    elif opcao == "b":
        try:
            nome = input("Digite o nome do aluno: ")
            nota = input("Digite a nota do aluno: ")
            del notas[nome]
            continue
        except:
            print("Aluno não encontrado")
            continue
    elif opcao == "c":
        media = sum(notas.values()) / len(notas)
        print(f"A média da turma é {media}")
        continue
    elif opcao == "d":
        break
    else:
        print("Opção inválida")
        continue
