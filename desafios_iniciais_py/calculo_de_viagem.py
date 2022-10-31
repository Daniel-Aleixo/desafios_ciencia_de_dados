valores = input().split()

consumo_carro = 12
tempo_gasto = int(valores[0])
velocidade_media = int(valores[1])

distacia_percorrida = velocidade_media * tempo_gasto

#print(distacia_percorrida)

litros = distacia_percorrida / consumo_carro

print(f"{litros:2.3f}")