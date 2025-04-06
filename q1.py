# Leitura do primeiro valor
valor1 = int(input("Digite o primeiro valor (inteiro): "))

# Leitura do segundo valor, garantindo que seja maior que o primeiro
while True:
    valor2 = int(input("Digite o segundo valor (maior que o primeiro): "))
    if valor2 > valor1:
        break
    else:
        print("O segundo valor deve ser maior que o primeiro. Tente novamente.")

# Cálculo da soma incluindo os valores lidos
soma = 0
for i in range(valor1, valor2 + 1):
    soma += i

# Exibição do resultado
print(f"A soma dos valores entre {valor1} e {valor2} é: {soma}")
