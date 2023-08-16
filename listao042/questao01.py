'''
. Fazer um algoritmo que peça um número, e ao final, informe se o número digitado está acima de 1000 ou
abaixo de 1000
'''

num = int(input("Digite um número:"))

if ( num < 1000 ):
    print(num, " está abaixo de 1000.")
elif ( num > 1000 ):
    print(num, " está acima de 1000.")
