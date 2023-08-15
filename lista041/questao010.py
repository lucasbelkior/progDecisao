'''
 Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado.
'''

numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))


if numero1 % numero2 == 0:
    print(f"{numero2} é um divisor de {numero1}.")
else:
    print(f"{numero2} não é um divisor de {numero1}.")
