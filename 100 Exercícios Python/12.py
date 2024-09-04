#12) escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo):

Fahrenheit = float(input("Insira a Temperatura em graus Fahrenheit: "))
calculo = (Fahrenheit - 32) / 9
conversao = 5 * calculo
print(f"A temperatura {Fahrenheit}° convertida para a temperatura celsiu é: {conversao}°")
