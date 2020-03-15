pergunta =int(input('Responda para calcular o seu peso 1 -> homem , 2 -> mulher: '))
altura = float(input('Digite a sua altura: '))
if pergunta == 1:
    calculo_peso_h = (72.7 * altura) - 58
    print ('O seu peso ideal para um homem e de ', '%.2f' % calculo_peso_h)
else:
    calculo_peso_m = (62.1 * altura) - 44.7
    print ('O seu peso ideal para uma mulher e de ', '%.2f' % calculo_peso_m)