meters = float(input('Digite quantos metros quadrados tem a área a ser pintada: '))
can_of_paint = meters / (18 * 3)
price = can_of_paint * 80
print(f'Você deve comprar {can_of_paint:.1f} latas de tinta, que sairá no preço de R${price:.2f}')
