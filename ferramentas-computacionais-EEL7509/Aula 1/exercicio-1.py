###Escreva um programa que funcione como um mini gerenciador de
# notas para uma turma de uma disciplina. O programa deve oferecer
#  três opções ao usuário:
# a) incluir nota,
# b) excluir nota,
# c) mostrar média da turma,
# d) sair do programa.
# Se o usuário selecionar a opção a),
# o programa deve solicitar o nome do aluno e a nota,
# armazenando esses valores em um dicionário.
# Para opção b),
# o programa deve solicitar o nome do aluno e fazer a
# exclusão do registro correspondente no dicionário.
# No caso da opção escolhida ser c),
# o programa deve calcular e imprimir a média da turma.
# Finalmente, para opção d), o programa deve ser finalizado.
###


class Notas:
    def __init__(self):
        self.notas = {}

    def incluir_nota(self):
        nome = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        self.notas[nome] = nota
        self.menu()

    def excluir_nota(self):
        try:
            nome = input("Digite o nome do aluno: ")
            del self.notas[nome]
            self.menu()
        except:
            print("Aluno não encontrado")
            self.menu()

    def mostrar_media(self):
        media = sum(self.notas.values()) / len(self.notas)
        print(f"A média da turma é {media}")
        self.menu()

    def sair(self):
        exit()

    def menu(self):
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
                self.incluir_nota()
            elif opcao == "b":
                self.excluir_nota()
            elif opcao == "c":
                self.mostrar_media()
            elif opcao == "d":
                self.sair()
            else:
                print("Opção inválida")


if __name__ == "__main__":
    notas = Notas()
    notas.menu()
