# Lista para armazenar os 50 números
numeros = []

# Leitura dos 50 números
print("Digite 50 números:")
for i in range(50):
    valor = int(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

# Dicionário para armazenar os números e suas posições
ocorrencias = {}

# Preenche o dicionário com posições de cada número
for i, num in enumerate(numeros):
    if num in ocorrencias:
        ocorrencias[num].append(i)
    else:
        ocorrencias[num] = [i]

# Verifica e exibe números repetidos
print("\nNúmeros repetidos e suas posições:")
repetidos = False
for num, posicoes in ocorrencias.items():
    if len(posicoes) > 1:
        print(f"Número {num} aparece nas posições: {posicoes}")
        repetidos = True

if not repetidos:
    print("Não há números repetidos na lista.")