quilos_pescados = float(input('Digite a quantidade de quilos pescado: '))

quilos = quilos_pescados - 50
excesso = quilos

if quilos == 0:
        print ('Nao sera cobrado multa pois esta no limite estabelecido pela lei!')

else:
    multa = excesso * 4
    print ('A quantidade em quilos pescados foi ', quilos_pescados ,'e a multa por exceder o limite de 50 e de R$', multa ,'por quilo excedente!')