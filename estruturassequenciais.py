#estrutura sequencial = algoritmo
#input = permite o usuario inserir dados
#output = imprime na tela
salariomensal = input("Qual o seu salário? Digite-o aqui: ")
salariomensal = float(salariomensal)

gastomensal = input("Qual seu gasto mensal: Digite-o aqui: ")
gastomensal = float(gastomensal) 

salarioanual = salariomensal * 12
gastoanual = gastomensal * 12

montanteanual = salarioanual - gastoanual
print("O seu saldo anual é de ", montanteanual)