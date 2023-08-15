'''
 Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas.
'''


numero = int(input("Digite um número inteiro de 3 algarismos: "))


if 100 <= numero <= 999:
    algarismo_centenas = numero // 100
    print(f"O algarismo das centenas é: {algarismo_centenas}")
else:
    print("O número não tem 3 algarismos.")
