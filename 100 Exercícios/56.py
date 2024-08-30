#56) Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.

valor = int(input("Insira um valor inteiro: "))

while valor <= 0 or valor >= 11:
    print("VALOR INVALIDO")
    print("POR FAVOR INSERIR UM VALOR ENTRE 1 E 10 ")
    valor = int(input("Insira um valor inteiro: "))
    
for x in range(1, 11):
    print(valor, " x ", x, " = ", valor * x)       