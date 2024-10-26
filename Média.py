# Função para calcular a média
def calcular_media(notas):
    return sum(notas) / len(notas)

# Lista para armazenar as notas
notas = []

# Solicita ao usuário que insira as notas
quantidade = int(input("Quantas notas você deseja inserir? "))

for i in range(quantidade):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

# Calcula a média
media = calcular_media(notas)

# Exibe o resultado da média
print(f"A média das notas é: {media:.2f}")

# Verifica se o aluno está aprovado ou reprovado
if media >= 7:
    print("Aprovado!")
else:
    print("Reprovado!")
