#25) faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

numero_da_conta_cliente = float(input("Insira o numero da conta do cliente: "))
saldo_cliente = float(input("Insira o numero do saldo do cliente: "))
debito_cliente = float(input("Insira o numero do debito do cliente: "))
credito_cliente = float(input("Insira o numero do credito do cliente: "))

saldo_atual = saldo_cliente - debito_cliente + credito_cliente

if saldo_atual >= 0:
    print("Saldo Positivo")
else:
    print("Saldo Negativo")
