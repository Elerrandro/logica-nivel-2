#33) ler dois valores e imprimir uma das três mensagens a seguir:

#‘Números iguais’, caso os números sejam iguais
#‘Primeiro é maior’, caso o primeiro seja maior que o segundo;
#‘Segundo maior’, caso o segundo seja maior que o primeiro.

n1 = int(input("Insira um numero: "))
n2 = int(input("Insira outro numero: "))

if n1 == n2:
    print("Números iguais")
elif n1 > n2:
    print("Primeiro maior")
else:
    print("Segundo maior")
