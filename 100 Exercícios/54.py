#54) Modifique o exercício anterior para aceitar somente valores maiores que 0 para N. Caso o valor informado (para N) não seja maior que 0, deverá ser lido um novo valor para N.

N = int(input("Insira um número inteiro: "))

while N <= 0:
    print("VALOR INVALIDO, POR FAVOR INSERIR UM VALOR MAIOR QUE 0")
    N = int(input("Insira um número inteiro: "))

for x in range(1, N + 1):
    print(x)