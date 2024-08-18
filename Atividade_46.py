from colorama import init, Fore
init(autoreset=True)

lista = []

def adicionar_item(item):
    lista.append(item)
    print(Fore.GREEN + f"Item '{item}' adicionado com sucesso!")

def remover_item(item):
    if item in lista:
        lista.remove(item)
        print(Fore.RED + f"Item '{item}' removido com sucesso!")
    else:
        print(Fore.YELLOW + f"Item '{item}' não encontrado na lista.")


while True:
    print("\nEscolha uma opção:")
    print("1. Adicionar item")
    print("2. Remover item")
    print("3. Mostrar lista")
    print("4. Sair")

    escolha = input("Digite o número da sua escolha: ")

    if escolha == '1':
        item = input("Digite o item a ser adicionado: ")
        adicionar_item(item)
    elif escolha == '2':
        item = input("Digite o item a ser removido: ")
        remover_item(item)
    elif escolha == '3':
        print("Itens na lista:", lista)
    elif escolha == '4':
        print("Saindo...")
        break
    else:
        print(Fore.RED + "Opção inválida, tente novamente.")
