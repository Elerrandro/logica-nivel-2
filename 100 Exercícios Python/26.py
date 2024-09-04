#26) faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2). Se a quantidade em estoque for maior ou igual a quantidade média, escrever a mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

quantidade_atual = int(input("Insira a quantidade em estoque atual: "))
quantidade_maxima = int(input("Insira a quantidade maxima em estoque: "))
quantidade_minima = int(input("Insira a quantidade minima em estoque: "))

quantidade_media = (quantidade_maxima + quantidade_minima)/2

if quantidade_atual >= quantidade_media:
    print("Não efetuar compra")
else:
    print("Efetuar compra")
