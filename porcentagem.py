print("--------------------------------")
print("CALCULADORA DE PORCENTAGEM")   #-- > Mensagem de boas vindas
print("--------------------------------")

numero = input("Insira o valor: ")  # --> Pede o valor
numero = int(numero)  #--> Passa o valor de str para int

porcentagem = input("Quantos porcento: ")  #--> Pega o valor da porcentagem
porcentagem = int(porcentagem) #--> Passa o valor de str para int

resultado = float((porcentagem * numero) / 100 )  #--> Calculo para saber a porcentagem

print("--------------------------------")
print(f"{porcentagem}% de {numero} é: {resultado}")  #--> Exibi o resultado
print("--------------------------------")