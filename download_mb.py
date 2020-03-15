tamanho_arquivo = float(input('Digite o tamanho do arquivo em MB: '))
velocidade_do_link = float(input('Digite a velocidade do link de internet: '))

calculo = tamanho_arquivo / (velocidade_do_link / 8)
resto = int(calculo) % 86400
horas = resto // 3600
minutos = resto // 60
print ('O tempo aproximado de download do arquivo e de ', minutos, 'minutos')