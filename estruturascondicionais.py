valor_passagem = 4.70
valor_passagem = float(valor_passagem)
valor_uber = input("Qual o valor da sua corrida? ")
valor_uber = float(valor_uber)
if valor_uber <= valor_passagem * 5:
    print("Vá de Uber")
elif valor_uber <=  valor_passagem * 6:
    print("Aguarde, o valor pode abaixar")
else:
    print("Vá de onibus")