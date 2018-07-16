'''
    Suponha que o preço de capa de um livro seja R$ 24,95,
    mas as livrarias recebem um desconto de 40%.
    O transporte custa R$ 3,00 para o primeiro
    exemplar e 75 centavos para cada exemplar adicional.
    Qual é o custo total de atacado para 60 cópias?



'''

valor_capa = float(24.95)
preco1 = valor_capa * float(0.4)+ 3
preco2 = valor_capa * float(0.4) + 0.75

print(" Na compra de 60 unidade o 1 ficaria {} e os demaais ficaria {} cada". format(preco1, preco2))
print ("Na compra de 60 total: {}" . format(round(preco2 * 60),2))
