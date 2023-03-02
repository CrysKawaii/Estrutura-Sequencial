mb = int(input('Digite o tamanho do arquivo em MB: '))
velocity_link = int(input('Digite a velocidade da sua internet em MBps: '))
download_time = (mb / (velocity_link * 60))
print(f'Seu download levaria {download_time:.2f} mintuos')
