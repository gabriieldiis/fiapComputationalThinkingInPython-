# Dada a quilometragem parcial de um carro e a quantidade de litros gastos ele para percorrer esta quilometragem, fazer um algoritmo que calcule quantos Km/l o carro percorreu

quilometragem = float(input("Quantos quilometros seu carro correu hoje? :"))

litros = float(input("Quanto você precisou colocar de litros em seu carro para percorre essa quilometragem? : "))

KML = quilometragem / litros

print("Seu carro percorre ", KML , "quilometros por litro!")