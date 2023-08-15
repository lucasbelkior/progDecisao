'''
Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”
'''


valor = int(input("Digite um valor numérico inteiro: "))


if valor % 4 == 0 and valor % 5 == 0:
    print(f"O valor {valor} é divisível por 4 e 5.")
else:
    print(f"O valor {valor} não é divisível por 4 e 5.")
