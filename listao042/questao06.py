'''
 Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”.
'''

nascimento = int(input("Qual e o seu ano de nascimento?:"))
ano = int(input("Qual e o ano atual?:"))
ida = ano - nascimento

if (nascimento > ano):
    print("Dados inseridos estao incorretos")

else:
    print("Sua idade é ", ida , "anos")