'''
Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a
metade deste número, senão, ele deverá exibir o número sem alterações.
'''

num1 = float(input("Informe um numero:"))
metade = num1/2

if (num1 > 20):
    print(metade)
else:
    print(num1)