#1) Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20 em uma variável B. A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o valor que está em A passe para B e vice-versa. Ao final, escrever os valores que ficaram armazenados nas variáveis.

A = 10
B = 20

print(f"A variável 'A' armazena:{A}")
print(f"A variável 'B' armazena:{B}")
print("Vamos trocar os conteúdos fazendo com que o valor que está em 'A' passe para 'B' e vice-versa.")

C = A
A = B
B = C

print(f"Agora os valores são 'A' = {A} e 'B' = {B}")