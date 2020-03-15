def descontos(salario_mes, imposto_de_renda, desconto_inss, desconto_sindicato, desconto_total, salario_liquido):
    print (f'O seu salario bruto e de R$ {salario_mes}')
    print (f'Foi descontado para o imposto de renda R$ {imposto_de_renda}')
    print (f'Foi descontado para o INSS o valor de R$ {desconto_inss}')
    print (f'Foi descontado para o sindicato o valor de R$ {desconto_sindicato}')
    print (f'O seu salario liquido e de R$ {salario_liquido}')




salario = float(input('Digite o valor de uma hora de trabalho: '))
hora_mes = int(input('Digite a quantidade de horas trabalhadas no mes: '))

salario_mes = salario * hora_mes

imposto_de_renda = salario_mes * 0.11

desconto_inss = salario_mes * 0.08

desconto_sindicato = salario_mes * 0.05

desconto_total = imposto_de_renda + desconto_inss + desconto_sindicato
salario_liquido = salario_mes - desconto_total

descontos(salario_mes, imposto_de_renda, desconto_inss, desconto_sindicato, desconto_total, salario_liquido)