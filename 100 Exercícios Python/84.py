#84) Faça um algoritmo para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois vetores A e B (de tamanho N cada um) e depois armazenar em um terceiro vetor Soma a soma dos elementos do vetor A com os do vetor B (respeitando as mesmas posições) e escrever o vetor Soma.

N = int(input("Digite o tamanho máximo:"))

A = []
B = []
Soma = []

for x in range(N):
    VA = int(input(f"Digite o {x+1}° valor da lista A: "))
    VB = int(input(f"Digite o {x+1}° valor da lista B: "))
    print("---"*15)
    VSoma = VA + VB

    A.append(VA)
    B.append(VB)
    Soma.append(VSoma)

print(Soma)