tarefas = [
    {"titulo": "estudar", "concluida": "Sim", "prioridade":"Alta"},
    {"titulo":"comer", "concluida":"Sim", "prioridade":"Muito Alta"},
    {"titulo":"treinar", "concluida":"Nao", "prioridade":"Media"},
    {"titulo":"jogar", "concluida":"Nao", "prioridade":"Baixa"},
    {"titulo":"lavar os pratos", "concluida":"Nao", "prioridade":"Media"}
]


def ver_tarefas():
    print("Tarefas:")
    for tarefa in tarefas:
        print(tarefa)


def ver_concluidas():
    print("Tarefas concluídas:")
    for tarefa in tarefas:
        if tarefa["concluida"] == "Sim":
            print(tarefa["titulo"])


def ver_pendentes():
    print("Tarefas pendentes:")
    for tarefa in tarefas:
        if tarefa["concluida"] == "Nao":
            print(tarefa["titulo"])


def ver_prioridade():
    prioridade = input("Digite a prioridade: ")

    for tarefa in tarefas:
        if tarefa["prioridade"] == prioridade:
            print(tarefa["titulo"])


def cadastrar_tarefa():
    nome = input("Nome da tarefa: ")
    prioridade = input("Prioridade: ")

    tarefa = {
        "titulo": nome,
        "prioridade": prioridade,
        "concluida": "Nao"
    }

    tarefas.append(tarefa)

    print("Tarefa cadastrada!")


def finalizar_tarefa():
    nome = input("Nome da tarefa para finalizar: ")

    for tarefa in tarefas:
        if tarefa["titulo"] == nome:
            tarefa["concluida"] = "Sim"
            print("Tarefa finalizada!")


def remover_tarefa():
    nome = input("Nome da tarefa para remover: ")

    for tarefa in tarefas:
        if tarefa["titulo"] == nome:
            tarefas.remove(tarefa)
            print("Tarefa removida!")
while True:
    print('')
    print('1. VER TAREFAS')
    print('2. VER CONCLUIDAS')
    print('3. VER PENDENTES')
    print('4. VER POR PRIORIDADE')
    print('5. CADASTRAR TAREFA NOVA')
    print('6. FINALIZAR TAREFA')
    print('7. REMOVER TAREFA')
    print('0. SAIR')
    opcao = input('escolha uma opção: ')

    if opcao == '1':
        ver_tarefas()
    elif opcao == '2':
        ver_concluidas()
    elif opcao == '3':
        ver_pendentes()
    elif opcao == '4':
        ver_prioridade()
    elif opcao == '5':
            cadastrar_tarefa()
    elif opcao == '6':
            finalizar_tarefa()
    elif opcao == '7':
            remover_tarefa()
    elif opcao == '0':
        print('Saindo do sistema...')
        break