#30) ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

n1 = int(input("Insira um valor: "))
n2 = int(input("Insira outro valor: "))
n3 = int(input("Insira outro valor: "))
ordem = [n1, n2, n3]
crescente = sorted(ordem)
print(crescente)
