# ==========================================
# CONTADOR DE VOGAIS
# ==========================================

# Função responsável por contar as vogais
def contar_vogais(texto):

    # Lista contendo todas as vogais
    vogais = "aeiou"

    # Variável que armazena a quantidade total
    contador = 0

    # Percorre cada letra do texto
    for letra in texto.lower():

        # Verifica se a letra é uma vogal
        if letra in vogais:

            # Soma +1 ao contador
            contador += 1

    # Retorna o total encontrado
    return contador


# ==========================================
# ENTRADA DE DADOS
# ==========================================

print("=" * 50)
print("      CONTADOR DE VOGAIS")
print("=" * 50)

# Permite ao usuário digitar uma frase grande
frase = input("\nDigite uma frase:\n> ")

# Chama a função
resultado = contar_vogais(frase)

# ==========================================
# SAÍDA
# ==========================================

print("\n" + "=" * 50)
print("RESULTADO")
print("=" * 50)

print(f"\nFrase digitada:")
print(f'"{frase}"')

print(f"\nQuantidade de vogais: {resultado}")

print("\nPrograma finalizado!")