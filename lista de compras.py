# Cria uma lista vazia que será usada para armazenar os itens da compra
lista = []

# Loop infinito para manter o programa funcionando até o usuário escolher sair
while True:

    # Exibe o menu de opções
    print("\n --- Lista de Compras ---")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Exibir lista")
    print("4 - Sair")

    # Pede ao usuário para escolher uma opção
    opcao = input("Escolha uma opção: ")

    # =========================
    # OPÇÃO 1 - ADICIONAR ITEM
    # =========================
    if opcao == "1":

        # Solicita o nome do item que será adicionado
        item = input("Digite o nome do Item: ")

        # Adiciona o item digitado dentro da lista
        lista.append(item)

        # Mensagem de confirmação
        print("Item Adicionado Com Sucesso!")

    # ========================
    # OPÇÃO 2 - REMOVER ITEM
    # ========================
    elif opcao == "2":

        # Pede o nome do item que o usuário deseja remover
        item = input("Digite o nome do item a ser removido: ")

        # Verifica se o item existe dentro da lista
        if item in lista:

            # Remove o item da lista
            lista.remove(item)

            # Mensagem de confirmação
            print("Item Removido Com Sucesso!")

        else:
            # Caso o item não exista, exibe mensagem de erro
            print("Item não Encontrado na Lista!")

    # ========================
    # OPÇÃO 3 - EXIBIR LISTA
    # ========================
    elif opcao == "3":

        # Verifica se a lista está vazia
        if len(lista) == 0:

            # Se estiver vazia, informa ao usuário
            print("Lista Vazia!")

        else:
            # Caso existam itens, exibe todos eles
            print("Itens na lista:")

            # Percorre cada item da lista usando um laço for
            for item in lista:

                # Mostra cada item com um traço na frente
                print("- " + item)

    # =================
    # OPÇÃO 4 - SAIR
    # =================
    elif opcao == "4":

        # Exibe mensagem de encerramento
        print("Saindo da Lista De Compras.")

        # Encerra o loop e finaliza o programa
        break

    # ==========================
    # OPÇÃO INVÁLIDA
    # ==========================
    else:

        # Executa caso o usuário digite algo diferente das opções válidas
        print("Opção Invalida! Tente Novamente.")