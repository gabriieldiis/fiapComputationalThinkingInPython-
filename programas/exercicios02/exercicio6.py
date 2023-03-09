# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

eleitores = int(input("Quantos eleitores existem na sua cidade ficticia"))

brancos = int(input("Quantas pessoas votaram em branco? "))

nulo = int(input("Quantas pessoas votaram em nulo? "))

valido = int(input("Quantas pessoas tiveram votos válidos? "))

porcetagem_votos_brancos = brancos * 100 / eleitores

porcetagem_votos_nulo = nulo * 100 / eleitores

porcetagem_votos_validos = valido * 100 / eleitores


print("votos em branco ", porcetagem_votos_brancos)

print("votos em nulo ", porcetagem_votos_brancos)

print("votos validos ", porcetagem_votos_brancos)