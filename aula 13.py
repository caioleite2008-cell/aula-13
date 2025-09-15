# Função para somar dois números
def somar(num1, num2):
    return num1 + num2

# Pede ao usuário dois números
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

# Chama a função para somar
resultado = somar(n1, n2)

# Mostra o resultado
print(f"A soma de {n1} + {n2} é: {resultado}")