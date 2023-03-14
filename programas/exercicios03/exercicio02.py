valor_hora = float(5.0)

tempo_estacionado = float(input("Quantas horas a mais o usuário ficou no estacionamento? "))

hora_adicional = valor_hora + tempo_estacionado * 2

if(hora_adicional > 35.0):
    print("Voce deve pagar R$ 35,00")
else:
    print("Voce deve pagar", hora_adicional)