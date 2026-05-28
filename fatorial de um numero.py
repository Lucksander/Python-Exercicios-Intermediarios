# Este programa calcula o fatorial de um número inteiro positivo fornecido pelo usuario
def calcular_fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# O 'int()' converte o texto digitado pelo usuário em um número inteiro
numero_usuario = int(input("Digite um número inteiro positivo: "))

# Validação: garante que o número não seja negativo
if numero_usuario < 0:
    print("Por favor, digite apenas números maiores ou iguais a zero.")
else:
    # Chama a função passando o número que o usuário digitou
    resultado_final = calcular_fatorial(numero_usuario)
    print(f"O fatorial de {numero_usuario} é: {resultado_final}")