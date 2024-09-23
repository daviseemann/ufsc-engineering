import matplotlib.pyplot as plt
import numpy as np

# Dados
coeficientes = {"a": 1, "b": -2, "c": -5}
# coeficientes["a"] = input("Digite o coeficiente a: ")
# coeficientes["b"] = input("Digite o coeficiente b: ")
# coeficientes["c"] = input("Digite o coeficiente c: ")

coef = np.array([coeficientes["a"], coeficientes["b"], coeficientes["c"]])


# Função
def f(x):
    a = coeficientes["a"]
    b = coeficientes["b"]
    c = coeficientes["c"]
    return float(a) * x**2 + float(b) * x + float(c)


roots = np.roots(coef)
zenith = -coeficientes["b"] / (2 * coeficientes["a"])
vertex_y = f(zenith)


fig, ax = plt.subplots()
# Plot
x = np.linspace(-5, 5, 1000)
y = f(x)
ax.plot(x, y)
ax.plot(
    roots,
    [0, 0],
    "ro",
    label=f"As raízes da função são: {roots[0]:.2f} e {roots[1]:.2f}",
)
ax.plot(zenith, vertex_y, "go", label=f"O vértice da função é: {zenith:.2f}")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.set_title(
    "f(x) = {}x^2 + {}x + {}".format(
        coeficientes["a"], coeficientes["b"], coeficientes["c"]
    )
)
ax.legend()
plt.grid()
plt.show()
