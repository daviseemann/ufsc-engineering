students = [
    {"nome": "Alice", "idade": 20, "nota": 85},
    {"nome": "Bob", "idade": 21, "nota": 70},
    {"nome": "Charlie", "idade": 19, "nota": 92},
    {"nome": "David", "idade": 22, "nota": 65},
    {"nome": "Eve", "idade": 20, "nota": 88},
]

maior_que_vinte = lambda x: x["idade"] >= 20
nota_maior_que_setenta = lambda x: x["nota"] >= 70

resultado = [
    student
    for student in students
    if maior_que_vinte(student) and nota_maior_que_setenta(student)
]
print(resultado)
