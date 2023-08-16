'''
 Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo
'''



nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota da prova 1: "))
nota2 = float(input("Digite a nota da prova 2: "))

media = (nota1 + nota2) / 2
if(media < 3.0):
    print("Sinto muito, mas infelizmente você está reprovado. Tente se esforçar mais na próxima.")
else:
    if(media < 6.9):
        print("Parece que você está por um triz, ficou de Prova Final. Se dedique nessa reta final.")
    else:
        print("Você está aprovado! Meus parabéns Guerreiro.")


print(f"Sua média equivale a {media}.")

