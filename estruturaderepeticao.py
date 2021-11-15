#1
contador = 0
while contador < 10:
    contador = contador + 1
    if contador == 1:
        print(contador, "Item limpo")
    else:
            print(contador, "itens limpos")
print("Fim da louça")
#2
contador = 0

while True:
    if contador < 10:
        contador = contador + 1
        if contador == 1:
            print(contador, "item limpo")
        else:
            print(contador, "itens limpos")
    else:
        break
    #3
    texto = input('Digite sua senha: ')
while texto != "hilorena":
    texto = input("Senha incorreta! Digite novamente: ")
    if texto == "hilorena":
        print("Acesso liberado")