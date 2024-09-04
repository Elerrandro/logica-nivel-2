#19) ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

n1 = int(input("Insira um valor: "))
n2 = int(input("Insira um valor diferente: "))

if n1 > n2:
    print(f"O valor {n1} é maior que {n2}")
else:
    print(f"O valor {n2} é maior que {n1}")
