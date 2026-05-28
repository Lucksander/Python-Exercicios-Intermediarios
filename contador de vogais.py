# Função que conta quantas vogais existem em um texto
def contar_vogais(texto):
    
    # Variável que vai armazenar a quantidade de vogais encontradas
    contador = 0

    # Percorre cada letra do texto
    # lower() transforma tudo em minúsculo
    # para facilitar a comparação
    for letra in texto.lower():

        # Verifica se a letra atual é uma vogal
        if letra in "aeiou":

            # Se for vogal, soma 1 ao contador
            contador += 1

    # Retorna a quantidade total de vogais
    return contador


# Pede para o usuário digitar uma frase
frase = input("Digite uma frase: ")

# Chama a função e guarda o resultado
resultado = contar_vogais(frase)

# Exibe o total de vogais encontradas
print("Número de vogais na frase:", resultado)