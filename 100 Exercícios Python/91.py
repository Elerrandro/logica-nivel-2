# 91) Faça um algoritmo para ler 50 números e armazenar em um vetor VET, verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.

VET = []

for x in range(50):
    numeros = int(input(f"Digite o {x+1}° valor: "))
    VET.append(numeros)

# \n imprimi uma linha em branco
print("\nNúmeros repetidos e suas posições:")
repetidos = False

for x in range(len(VET)):
    for i in range(x + 1, len(VET)):
        if VET[x] == VET[i]:
            if not repetidos:
                repetidos = True
            print(f"Número {VET[x]} encontrado nas posições: {x} e {i}")

if not repetidos:
    print("Nenhum número repetido foi encontrado.")