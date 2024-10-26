# Função parafatorial
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Solicita ao usuário que insira um número
numero = int(input("Digite um número para calcular o fatorial: "))

# Calcula o fatorial
resultado = fatorial(numero)

# Exibe o resultado
print(f"O fatorial de {numero} é: {resultado}")

