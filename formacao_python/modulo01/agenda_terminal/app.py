from os import system

lista_de_contatos = list()

while True:
    print("""
    [0] Sair
    [1] Salvar contato
    [2] Editar contato
    [3] Deletar contato
    [4] Buscar contato
    [5] Visualizar todos os contatos
    [6] Visualizar os contatos favoritos \n
""")
    opcao = int(input("O que deseja fazer? "))
    if opcao == 0:
        system("cls")
        print("Até mais!")
        break

    elif opcao == 1:

        contato = dict()

        nome: str = input("Digite o nome: ")
        contato["nome"] = nome
        telefone: str = input("Digite o telefone: ")
        contato["telefone"] = telefone
        email: str = input("Digite o email: ")
        contato["email"] = email
        favorito: bool = input("Quer adicionar como favorito? (Sim/Não): ")
        contato["favorito"] = True if favorito == "Sim" or favorito == "S" else False
        lista_de_contatos.append(contato)
        system("cls")

    elif opcao == 2:
        system("cls")
        opcao_editar = input("Digite o nome do contato que deseja editar: ")
        for i, opcoes_contato in enumerate(lista_de_contatos):
            if opcoes_contato["nome"] == opcao_editar:
                novo_nome: str = input("Digte o novo nome: ")
                lista_de_contatos[i]["nome"] = novo_nome
                novo_telefone: str = input("Digte o novo telefone: ")
                lista_de_contatos[i]["telefone"] = novo_telefone
                novo_email: str = input("Digte o novo email: ")
                lista_de_contatos[i]["email"] = novo_email
                novo_favorito: str = input("Adicionar para favorito? (Sim/Não): ")
                lista_de_contatos[i]["favorito"] = (
                    True if novo_favorito.lower() in ("sim", "s") else False
                )
                print("Contato Atualizado com sucesso!")
    elif opcao == 3:
        system("cls")
        opcao_deletar = input("Digite o nome do contato que quer remover: ")
        for i, opcoes_contato in enumerate(lista_de_contatos):
            if opcoes_contato["nome"] == opcao_deletar:
                lista_de_contatos.pop(i)

    elif opcao == 4:
        opcao_buscar = input("Digite o nome do contato que deseja buscar: ")
        for i, opcoes_contato in enumerate(lista_de_contatos):
            if opcoes_contato["nome"] == opcao_buscar:
                print(f""" 
                Nome: {opcoes_contato['nome']}
                Telefone: {opcoes_contato['telefone']}
                Email: {opcoes_contato['email']}
                \n""")

    elif opcao == 5:
        system("cls")
        for visualiar_contato in lista_de_contatos:
            print(f""" 
Nome: {visualiar_contato['nome']}
Telefone: {visualiar_contato['telefone']}
Email: {visualiar_contato['email']}
\n""")

    elif opcao == 6:
        for visualizar_favorito in lista_de_contatos:
            if visualizar_favorito["favorito"]:
                print(f""" 
                Nome: {visualizar_favorito['nome']}
                Telefone: {visualizar_favorito['telefone']}
                Email: {visualizar_favorito['email']}
                \n""")
    else:
        system("cls")
        print("Opção invalida, tente novamente!")
