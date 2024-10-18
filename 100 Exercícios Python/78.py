#78) Escreva um algoritmo que permita a leitura dos nomes de 10 pessoas e armaze os nomes lidos em um vetor. Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de pessoa e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário. 

nomes = []

for x in range(1, 11):
    nomes.append(input(f"Digite o {x}° nome: "))

print("---"*15)
procurando_nome = input("Digite o nome que deseja procurar: ")

if procurando_nome in nomes:
    print("ACHEI")
else:
    print("NÃO ACHEI")