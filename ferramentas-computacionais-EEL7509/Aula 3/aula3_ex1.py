# Exercício 1: Escreva uma função que simule a jogada ou rolagem de um dado.
# Sua função deve considerar, por padrão, um dado de 6 faces, mas deve também
# permitir a escolha do número de faces do dado. Em seguida, simule 10 rolagens
# de um dado de 6 faces e calcule o valor médio obtido (usando a função mean do
# módulo statistics). Simule ainda 1000 rolagens do dado e calcule novamente
# o valor médio obtido.
# ## Resolução
import numpy as np
import random
import statistics
import matplotlib.pyplot as plt


def dado(n_faces=6):
    return random.randint(1, n_faces)


# Simulando 10 rolagens de um dado de 6 faces
def rolagens(n_faces=6, n_rolagens=10):
    rolagens = [dado(6) for _ in range(n_rolagens)]
    media = statistics.mean(rolagens)
    return (rolagens, media)


def medias_de_rodagens(n_faces=6, start=1, stop=1000, step=10):
    medias = []
    for n_rolagens in range(start, stop, step):
        rolagens = [dado(n_faces) for _ in range(int(n_rolagens))]
        media = statistics.mean(rolagens)
        medias.append(media)
    return medias


# Simulando 10 rolagens de um dado de 6 faces
dez_vezes = rolagens()
# Simulando 1000 rolagens de um dado de 6 faces
mil_vezes = rolagens(n_rolagens=1000)
# Simulando 10000 rolagens de um dado de 6 faces
dez_mil_vezes = rolagens(n_rolagens=10000)
# plotando as medias conforme aumenta os numeros de rolagens
medias = medias_de_rodagens(stop=10000)

# Criando uma figura para cada gráfico
fig1, ax1 = plt.subplots(figsize=(9, 5))
ax1.hist(dez_vezes[0], bins=range(1, 8), edgecolor="black")
ax1.set_title("Simulação de 10 rolagens de um dado de 6 faces")
ax1.annotate(f"Média: {dez_vezes[1]:.2f}", xy=(0.1, 0.9), xycoords="axes fraction")
plt.tight_layout()
plt.show()

fig2, ax2 = plt.subplots(figsize=(9, 5))
ax2.hist(mil_vezes[0], bins=range(1, 8), edgecolor="black")
ax2.set_title("Simulação de 1000 rolagens de um dado de 6 faces")
ax2.annotate(f"Média: {mil_vezes[1]:.2f}", xy=(0.1, 0.9), xycoords="axes fraction")
plt.tight_layout()
plt.show()

fig3, ax3 = plt.subplots(figsize=(9, 5))
ax3.hist(dez_mil_vezes[0], bins=range(1, 8), edgecolor="black")
ax3.set_title("Simulação de 10000 rolagens de um dado de 6 faces")
ax3.annotate(f"Média: {dez_mil_vezes[1]:.2f}", xy=(0.1, 0.9), xycoords="axes fraction")
plt.tight_layout()
plt.show()

fig4, ax4 = plt.subplots(figsize=(9, 5))
ax4.hist(medias, bins=100, edgecolor="black")
ax4.set_title("Médias obtidas conforme o número de rolagens aumenta")
ax4.set_xlabel("médias")
plt.show()
