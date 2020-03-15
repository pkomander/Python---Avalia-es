def tintacustolata(calculo_lata, custo_tinta):
    print(f'Foram compradas ', '%.0f' % calculo_lata, 'latas de tinta')
    print(f'E o valor e de R$', '%.2f' % custo_tinta)



comprimento= float(input('Digite o comprimento da area a ser pintada: '))
largura = float(input('Digite a largura da area a ser pintada: '))

#1 litro para 3 metros quadrados
litro = 3

#uma lata contem 18 litros
latas = 18
valor_lata = 80

#metro quadrado da area
metro_quadrado = comprimento * largura

# calculo de tinta por metro quadrado
calculo_litro = metro_quadrado / litro

#calculo de latas por litros de tinta
if latas <= calculo_litro:
    calculo_lata = calculo_litro / latas

custo_tinta = valor_lata * calculo_lata
tintacustolata(calculo_lata, custo_tinta)
