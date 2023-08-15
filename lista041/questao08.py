'''
 Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10.
'''


numero = int(input("Digite um número inteiro: "))


if numero >= 1 and numero <= 10:
    print(f"O número {numero} está na faixa de 1 a 10.")
else:
    print(f"O número {numero} não está na faixa de 1 a 10.")
