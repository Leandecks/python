# Leandro Gridelli

import random

def get_surnames(filename):
    cognomi = []

    with open("cognomi.txt") as file:
        for nome in file:
            cognomi.append(nome.strip("\n"))

    return cognomi

def matrix(x, y):
    m = []

    for line in range(y):
        l = []
        for row in range(x):
            l.append(random.randint(0, 10))
        m.append(l)

    return m

def analyzer(surnames, classes, grades):
    i = 0

    for student_grades in grades:
        best_class_index = student_grades.index(max(student_grades))
        best_class = classes[best_class_index]
        student_name = surnames[i]

        print(f"Studente: {student_name}, voti: {student_grades}, materia migliore: {best_class}")

        i += 1

# main

my_surnames = get_surnames("cognomi.txt")
my_classes = ["italiano", "mate", "info", "fisica", "filosofia"]
my_grades = matrix(len(my_classes), len(my_surnames))

analyzer(my_surnames, my_classes, my_grades)
