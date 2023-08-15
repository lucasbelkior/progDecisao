'''
 Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido.
'''

valor1 = int(input("Digite o primeiro valor numérico inteiro: "))
valor2 = int(input("Digite o segundo valor numérico inteiro: "))


if valor1 > valor2:
    diferenca = valor1 - valor2
else:
    diferenca = valor2 - valor1

print(f"A diferença entre os valores é: {diferenca}")
