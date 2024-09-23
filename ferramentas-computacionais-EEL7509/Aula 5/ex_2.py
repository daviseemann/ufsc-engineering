import matplotlib.pyplot as plt
import numpy as np


# Solving the system of equations
A = np.array([[1, 1], [1, 3]])
B = np.array([3, 6])
solution = np.linalg.solve(A, B)

# Plotting the lines
x = np.linspace(-10, 10, 100)


def reta_A(x):
    return 3 - x


def reta_B(x):
    return (6 - x) / 3


fig, ax = plt.subplots()

ax.scatter(solution[0], solution[1], color="red", zorder=5)
ax.plot(x, reta_A(x), label="x+y=3")
ax.plot(x, reta_B(x), label="x+3y=6")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("x+y = 3, x+3y = 6")
ax.grid()
ax.legend()
plt.show()
