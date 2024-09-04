#22) A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).

Trabalho_semanal = 40#horas
extra = 0.5#50%
mes = 4#semanas


Hora_trabalhada_mes = int(input("Insira a horas trabalhadas em um mês: "))
Salario_por_hora = float(input("Insira o salário hora: "))

Trabalho_mes = Trabalho_semanal * mes
Salario_regular = Hora_trabalhada_mes * Salario_por_hora


if Hora_trabalhada_mes > Trabalho_mes:
    Hora_Extra = Hora_trabalhada_mes - Trabalho_mes
    Salario_extra = Hora_Extra * Salario_por_hora * (1 + extra)
    Salario_total = Salario_regular + Salario_extra
    print(f"O salario total é R${Salario_total}")
else:
    print(f"O salario total é R${Salario_regular}")
