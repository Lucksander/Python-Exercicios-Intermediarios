# Lista onde os contatos serão armazenados
contatos = []

# Função para adicionar um novo contato
def adicionar_contato():

    # Solicita os dados do usuário
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    # Cria um dicionário com as informações do contato
    contato = {
        "Nome": nome,
        "Telefone": telefone,
        "Email": email
    }

    # Adiciona o contato na lista
    contatos.append(contato)

    print("Contato adicionado com sucesso!")


# Função para listar todos os contatos
def listar_contatos():

    # Verifica se a lista está vazia
    if len(contatos) == 0:
        print("Nenhum contato encontrado.")

    else:
        print("\n--- Lista de Contatos ---")

        # Percorre cada contato da lista
        for contato in contatos:

            # Exibe os dados do contato
            print("\nNome:", contato["Nome"])
            print("Telefone:", contato["Telefone"])
            print("Email:", contato["Email"])


# Função para buscar um contato pelo nome
def buscar_contato():

    # Pede o nome que será pesquisado
    nome_busca = input("Digite o nome para buscar: ")

    # Percorre a lista de contatos
    for contato in contatos:

        # Compara os nomes ignorando maiúsculas/minúsculas
        if contato["Nome"].lower() == nome_busca.lower():

            print("\nContato encontrado:")
            print("Nome:", contato["Nome"])
            print("Telefone:", contato["Telefone"])
            print("Email:", contato["Email"])

            return

    # Caso não encontre o contato
    print("Contato não encontrado.")


# Função para apagar um contato
def apagar_contato():

    # Solicita o nome do contato
    nome_apagar = input("Digite o nome do contato que deseja apagar: ")

    # Percorre a lista de contatos
    for contato in contatos:

        # Verifica se o nome existe
        if contato["Nome"].lower() == nome_apagar.lower():

            # Remove o contato da lista
            contatos.remove(contato)

            print("Contato apagado com sucesso!")

            return

    # Caso o contato não exista
    print("Contato não encontrado.")


# Loop principal do programa
while True:

    # Menu principal
    print("\n--- Agenda de Contatos ---")
    print("1 - Adicionar Contato")
    print("2 - Listar Contatos")
    print("3 - Buscar Contato")
    print("4 - Apagar Contato")
    print("5 - Sair")

    # Usuário escolhe uma opção
    opcao = input("Escolha uma opção: ")

    # Executa a função correspondente
    if opcao == "1":
        adicionar_contato()

    elif opcao == "2":
        listar_contatos()

    elif opcao == "3":
        buscar_contato()

    elif opcao == "4":
        apagar_contato()

    elif opcao == "5":
        print("Saindo da Agenda. Até logo!")
        break

    # Caso a opção seja inválida
    else:
        print("Opção inválida. Tente novamente.")