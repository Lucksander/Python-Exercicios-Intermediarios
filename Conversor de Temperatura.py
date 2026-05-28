# Função que converte temperatura de Celsius para Fahrenheit
def celsius_para_farenheit(c):
    
    # Fórmula da conversão:
    # Multiplica a temperatura em Celsius por 9/5 e soma 32
    return (c * 9/5) + 32


# Função que converte temperatura de Fahrenheit para Celsius
def farenheit_para_celcius(f):
    
    # Fórmula da conversão:
    # Subtrai 32 da temperatura em Fahrenheit
    # e multiplica o resultado por 5/9
    return (f - 32) * 5/9


# Exibe o menu de opções para o usuário
print("Escolha a conversão:")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")


# Recebe a opção digitada pelo usuário
opcao = input("Digite 1 ou 2: ")


# Recebe a temperatura que será convertida
# float() permite digitar números com casas decimais
temperatura = float(input("Digite a temperatura a ser convertida: "))


# Verifica se o usuário escolheu a opção 1
if opcao == "1":
    
    # Chama a função de conversão Celsius -> Fahrenheit
    resultado = celsius_para_farenheit(temperatura)
    
    # Exibe o resultado da conversão
    print("Resultado:", resultado, "°F")


# Verifica se o usuário escolheu a opção 2
elif opcao == "2":
    
    # Chama a função de conversão Fahrenheit -> Celsius
    resultado = farenheit_para_celcius(temperatura)
    
    # Exibe o resultado da conversão
    print("Resultado:", resultado, "°C")


# Caso o usuário digite qualquer outra opção
else:
    
    # Exibe mensagem de erro
    print("Opção inválida")