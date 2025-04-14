# Leandro Gridelli

import random

def matrix(n):
    m = []
    
    for i in range(n):
        r = []
        for j in range(n):
            r.append(random.randint(1, 10))
        m.append(r)
        
    return m

def format_matrix(m):
    for r in m:
        for c in r:
            print(c, end="\t")
        print()
        
def line_sum(m):
    s = []
    
    for l in m:
        s.append(sum(l))
        
    return s
        
# def invert(m):
#     m2 = []
#     
#     for line in m:
#         for el_index in line:
#             
    
def single_row_sum(m, r):
    s = 0
    
    for line in m:
        for el_index in range(len(line)):
            if el_index == r:
                s += line[el_index]
                
    return s

def row_sum(m):
    s = []
    
    for i in range(len(m)):
        s.append(single_row_sum(m, i))
        
    return s

def diag_sum(m):
    d = []
    s = 0
    
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == j:
                s += m[i][j]
                
    return s

def diag_2(m):
    m2 = []
    
    for row in m:
        r = list(reversed(row))
        m2.append(r)
        
    return diag_sum(m2)

# main

mat = matrix(3)
format_matrix(mat)
print("Somme righe:", line_sum(mat))
print("Somme colonne: ", row_sum(mat))
print("Somme diagonali: ", diag_sum(mat), ",", diag_2(mat))
