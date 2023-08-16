'''
. Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

numero = input("Digite a sigla de um estado brasileiro: ")

if numero == "Sp":
    print("Sao Paulo esta na regiao Sudeste")
elif numero == "Rj":
    print("Rio de janeiro esta na regiao Sudeste")
elif numero == "Mg":
    print("Minas Gerais Esta na regiao sudeste")
elif numero == "Es":
    print("Espirito Santo esta na regiao Sudeste")

else:
    print("O estado inserido não pertence a regiao Sudeste")

