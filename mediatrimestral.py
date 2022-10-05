from pyparsing import null_debug_action


ativ = int(input("Escreva ao lado o número de atividades realizadas com a turma: "))

if ativ == 4:
    A = float(input("Escreva ao lado a nota da primeira atividade com peso 2: "))
    B = float(input("Escreva ao lado a nota da segunda atividade com peso 2: "))
    C = float(input("Escreva ao lado a nota da terceira atividade com peso 3: "))
    D = float(input("Escreva ao lado a nota da quarta atividade com peso 3: "))
    
    import math
    from symtable import Symbol
    import sympy
    w, x, y, z = sympy.symbols('w, x, y, z')

    valorA = w = A*2/10
    valorB = x = B*2/10
    valorC = y = C*3/10
    valorD = z = D*3/10

    notafinal = valorA + valorB + valorC + valorD
    
    print("Atividade 1 - Nota: ", valorA, " | Atividade 2 - Nota: ", valorB)
    print("Atividade 3 - Nota: ", valorC, " | Atividade 4 - Nota: ", valorD)
    print("A nota final do aluno foi de: ", notafinal)
    input()
    exit()
    

elif ativ == 5:
    A = float(input("Escreva ao lado a nota da primeira atividade - peso 3: "))
    B = float(input("Escreva ao lado a nota da segunda atividade - peso 2: "))
    C = float(input("Escreva ao lado a nota da terceira atividade - peso 2: "))
    D = float(input("Escreva ao lado a nota da quarta atividade - peso 2: "))
    E = float(input("Escreva ao lado a nota da quarta atividade - peso 1: "))
import sympy   
v, w, x, y, z = sympy.symbols('v, w, x, y, z')

valorA = v = A*3/10
valorB = w = B*2/10
valorC = x = C*2/10
valorD = y = D*2/10
valorE = z = E*1/10

notafinal = valorA + valorB + valorC + valorD + valorE
print("Atividade 1 - Nota: ", valorA, " | Atividade 2 - Nota: ", valorB, " | Atividade 3 - Nota: ", valorC)
print("Atividade 4 - Nota: ", valorD, " | Atividade 5 - Nota: ", valorE)
print("A nota final do aluno foi de: ", notafinal)
input("aperte enter para sair")
input()

    
    
