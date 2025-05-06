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
    passed_subj = []
    failed_subj = []
    subj = {}
    
    for cl in classes:
        subj[cl] = 0
    
    for student_grades in grades:
        for grade in student_grades:
            subject = classes[student_grades.index(grade)]
            
            if grade > 6:
                subj[subject] += 1
            else:
                subj[subject] += 1
        
    return subj

def analyzer2(subj):
    print("Materia migliore:", max(subj))
    print("Materia peggiore:", min(subj))

# main

my_surnames = get_surnames("cognomi.txt")
my_classes = ["italiano", "mate", "info", "fisica", "filosofia"]
my_grades = matrix(len(my_classes), len(my_surnames))
my_subjects = analyzer(my_surnames, my_classes, my_grades)
analyzer2(my_subjects)
