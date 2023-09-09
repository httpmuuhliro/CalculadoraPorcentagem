print("--------------------------------")
print("CALCULADORA DE PORCENTAGEM")
print("--------------------------------")

numero = input("Insira o valor: ")
numero = int(numero)

porcentagem = input(f"Quantos porcento de {numero} você quer saber: ")
porcentagem = int(porcentagem)

resultado = float((porcentagem * numero) / 100 )

print("--------------------------------")
print(f"{porcentagem}% de {numero} é: {resultado}")
print("--------------------------------")