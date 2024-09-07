#74) Escreva um algoritmo que imprima a tabuada (de 1 a 10) para os números de 1 a 10.


numero = 0 # Inicializa a variável 'numero' com 0

# Primeiro loop, para os números de 1 a 10
for x in range(10):
    numero = numero + 1 # Incrementa o número a cada iteração
    
    # Segundo loop, para gerar a tabuada de cada número de 1 a 10
    for x in range(1, 11):
        # Imprime a multiplicação do 'numero' atual por 'x'
        print(numero, " x ", x, " = ", numero * x) 
    
    print("-----" * 15) # Separador visual entre as tabuadas