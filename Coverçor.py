# Função para converter Fahrenheit em Celsius
def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
# insira a temperatura em Fahrenheit
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
# Realiza a conversão
celsius = fahrenheit_para_celsius(fahrenheit)
# Exibe o resultado
print(f"A temperatura em Celsius é: {celsius:.2f} °C")