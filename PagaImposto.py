earn_hour = float(input('Digite quanto você ganha por hora: R$'))
hour_month = float(input('Digite quantas horas trabalha por mês: '))
wage = earn_hour * hour_month
ir = wage - (wage - (wage * 11/100))
inss = wage - (wage - (wage * 8/100))
sindicato = wage - (wage - (wage * 5/100))
net_salary = wage - ir - inss - sindicato
print(f'''
+ Salário Bruto : R${wage}
- IR (11%) : R${ir}
- INSS (8%) : R${inss}
- Sindicato (5%) : R${sindicato}
= Salário Líquido : R${net_salary}''')
