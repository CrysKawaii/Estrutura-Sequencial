weight = float(input('Digite quantos quilos de peixe você tem: '))
excess = weight - 50
traffic_ticket = excess * 4
print(f'Você excedeu {excess}Kg de peso a mais do que é permitido')
print(f'Você deve pagar uma multa de R${traffic_ticket}')
