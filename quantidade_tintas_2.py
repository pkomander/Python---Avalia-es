def tintacustolata(calculo_lata, custo_tinta, calculo_galao, custo_galao, soma):
    print('Em compras de latas de 18 litros')
    print(f'Deveram ser compradas ', '%.0f' % calculo_lata, 'latas de tinta')
    print(f'E o valor e de R$', '%.2f' % custo_tinta)
    print('Em compras de galoes de 3.6 litros')
    print(f'Deveram ser compradas ','%.0f' % calculo_galao, 'galoes de tinta')
    print(f'E o valor e de R$', '%.2f' % custo_galao)
    print('Em compras de latas e galoes')
    print(f'Deveram ser compradas ', '%.0f' % mistura_lg, 'latas e ', '%.0f' % mistura_gl, 'galoes de tinta')
    print(f'E o valar e de R$', '%.2f' % soma)



comprimento= float(input('Digite o comprimento da area a ser pintada: '))
largura = float(input('Digite a largura da area a ser pintada: '))

#1 litro para 6 metros quadrados
litro = 6

#uma lata contem 18 litros
latas = 18
valor_lata = 80 * 0.10

#um galão de tinta contem 3.6 litros
galao = 3.6
valor_galao = 25 * 0.10


#metro quadrado da area
metro_quadrado = comprimento * largura



# calculo de tinta por metro quadrado
calculo_litro = metro_quadrado / litro




#calculo de latas por litros de tinta
if latas <= calculo_litro and galao <= calculo_litro:
    calculo_lata = calculo_litro / latas
    calculo_galao = calculo_litro / galao

custo_tinta = valor_lata * calculo_lata

custo_galao = valor_galao * calculo_galao


#mistura de latas e galoes a serem comprados juntos
mistura_lg = calculo_lata / 2
mistura_gl = calculo_galao / 2

#custo_mistural = custo_tinta * mistura_lg
#custo_misturag = custo_galao * mistura_gl

#total_custo = (custo_mistural + custo_misturag)
#desconto = total_custo * 0.10
#total_custo_mistura = total_custo - desconto

#if calculo_lata > int:









custo_ml = (custo_tinta * mistura_lg)
custo_mg = (custo_galao * mistura_gl)
soma = custo_ml + custo_mg



tintacustolata(calculo_lata, custo_tinta, calculo_galao, custo_galao, soma)
