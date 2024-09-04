#38) Faça um algoritmo para ler um número que é um código de usuário. Caso este código seja diferente de um código armazenado internamente no algoritmo (igual a 1234) deve ser apresentada a mensagem ‘Usuário inválido!’. Caso o Código seja correto, deve ser lido outro valor que é a senha. Se esta senha estiver incorreta (a certa é 9999) deve ser mostrada a mensagem ‘senha incorreta’. Caso a senha esteja correta, deve ser mostrada a mensagem ‘Acesso permitido’.


codigo = 2222
senha = 9999
cod = int(input("Digite o código: "))

while cod != codigo:
    print("Usuário inválido")
    cod = int(input("Digite o código: "))
        
sen = int(input("Digite a senha: "))

while sen != senha:
    print("Senha incorreta")
    sen = int(input("Digite a senha: "))
        
print("Acesso permitido")
