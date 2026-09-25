clientes = [
    {"nome":"Ana", "cel":"676967", "empresa":"FIAT"},
    {"nome":"Pedro", "cel":"55287", "empresa":"INTEL"},
    {"nome":"Maria", "cel":"55326", "empresa":"SEBRAE"},
    {"nome":"Felipe", "cel":"44343", "empresa":"INTEL"}
]

resposta = str(input("Qual empresa voce quer ver os clientes?: "))

for cliente in clientes:
    if cliente ["empresa"] == resposta:
        print (cliente)

    novo_nome = str(input('qual o nome do cliente que voce quer adicionar?: '))
    novo_cel = str(input('qual o celular do cliente que voce quer adicionar?: '))
    nova_empre = str(input('qual é a empresa do cliente que voce quer adicionar?: '))
    clientes.append ({"nome":novo_nome, "cel": novo_cel, "empresa": nova_empre})

# excluir cliente

    excluir = str(input('que cliente voce quer remover?: '))
    for cliente in clientes:
        if cliente["nome"] == excluir:
            clientes.remove (cliente)
            print(clientes)
            break