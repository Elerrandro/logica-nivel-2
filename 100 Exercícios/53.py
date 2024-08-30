#53) Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive). Considere que o N será sempre maior que ZERO.

N = int(input("Insira um número inteiro: "))

for x in range(1, N + 1):
    print(x)