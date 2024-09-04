#20) ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

n1 = int(input("Insira um número: "))
n2 = int(input("Indira outro número: "))

if n1 < n2:
    print(f"{n1} e {n2}")
else:
    print(f"{n2} e {n1}")
