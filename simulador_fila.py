fila = [{"nome": "Guilherme",
              "idade": 23,
              "gestante": False,
              "crianca_de_colo": True,
              "prioridade": 1
              },
        {"nome": "Maria",
         "idade": 23,
         "gestante": True,
         "crianca_de_colo": False,
         "prioridade": 2
         }
        ]

def calculo_prioridade(idade, gestante, crianca_de_colo):
    if crianca_de_colo:
        return 1  # Maior prioridade
    elif gestante:
        return 2  # Segunda prioridade
    elif idade >= 60:
        return 3  # Terceira prioridade (idosos)
    else:
        return 4  # Menor prioridade (adultos)

def tempo_atendimento(crianca_de_colo, gestante, idade):
    if crianca_de_colo:
        return 7
    elif gestante:
        return 4
    elif idade >= 60:
        return 7
    else:
        return 2


def adicionando_na_fila(nome, idade, gestante, crianca_de_colo):
    prioridade = calculo_prioridade(idade, gestante, crianca_de_colo)
    pessoa = {"nome": nome,
              "idade": idade,
              "gestante": gestante,
              "crianca_de_colo": crianca_de_colo,
              "prioridade": prioridade
              }
    fila.append(pessoa)

def atender_proxima_pessoa():
    if not fila:
        print("Fila vazia.")
        return

    # Encontra o índice da pessoa com maior prioridade (menor número)
    indice = min(range(len(fila)), key=lambda i: fila[i]["prioridade"])
    proxima = fila.pop(indice)

    tempo = tempo_atendimento(proxima["crianca_de_colo"], proxima["gestante"], proxima["idade"])
    print(f"Atendendo {proxima['nome']}... (tempo: {tempo} min)")

def mostrar_fila():
    if not fila:
        print("Fila vazia.")
        return

    # Cria uma cópia ordenada da fila para exibição
    fila_ordenada = sorted(fila, key=lambda p: p["prioridade"])

    print("Fila (por prioridade e ordem de chegada):")
    for i, pessoa in enumerate(fila_ordenada, 1):
        print(f"{i}. {pessoa['nome']} (Prioridade {pessoa['prioridade']})")


def buscar_pessoa():
    nome = input('Digite nome da pessoa que deseja encontrar: ')
    for pessoa in fila:
        if pessoa["nome"].lower() == nome.lower():
            return pessoa
    return None

def mostrar_estatisticas(fila):
    if not fila:
        print("Fila vazia.")
        return

    total = len(fila)
    idosos = sum(1 for p in fila if p.get("idade", 0) >= 60)
    gestantes = sum(1 for p in fila if p.get("gestante", False))
    criancas_colo = sum(1 for p in fila if p.get("crianca_de_colo", False))

    # Contagem por prioridade
    prioridades = {}
    for pessoa in fila:
        prio = pessoa.get("prioridade", 4)
        prioridades[prio] = prioridades.get(prio, 0) + 1

    # Idade média
    soma_idades = sum(p.get("idade", 0) for p in fila)
    idade_media = soma_idades / total

    # Próxima pessoa (maior prioridade = menor número)
    proxima = sorted(fila, key=lambda x: x.get("prioridade", 4))[0]

    print(f"📊 Estatísticas da Fila:")
    print(f"Total de pessoas: {total}")
    print(f" - Idosos: {idosos}")
    print(f" - Gestantes: {gestantes}")
    print(f" - Crianças de colo: {criancas_colo}")
    print(f"Idade média: {idade_media:.1f} anos")
    print(f"Distribuição por prioridade:")
    for nivel in sorted(prioridades):
        print(f" - Prioridade {nivel}: {prioridades[nivel]} pessoa(s)")
    print(f"Próxima pessoa a ser atendida: {proxima['nome']} (Prioridade {proxima['prioridade']})")


while True:
    print("""===== MENU =====

1. Adicionar pessoa na fila
2. Atender próxima pessoa
3. Mostrar fila
4. Buscar pessoa por nome
5. Estatísticas
6. Sair
""")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            gestante = input("Gestante? (s ou n): ").lower() in ["s", "sim"]
            crianca_de_colo = input("Criança de colo? (s ou n): ").lower() in ["s", "sim"]
            adicionando_na_fila(nome, idade, gestante, crianca_de_colo)
        case "2":
            atender_proxima_pessoa()
        case "3":
            mostrar_fila()
        case "4":
            busca = buscar_pessoa()
            if busca == None:
                print("Esta pessoa não está na fila.")
            else:
                print(f"""=== Dados ===
Nome: {busca["nome"]}
Idade: {busca["idade"]}
Gestante: {"Sim" if busca["gestante"] else "Não"}
Criança de colo: {"Sim" if busca["crianca_de_colo"] else "Não"}
Prioridade: {busca["prioridade"]}
""")
        case "5":
            mostrar_estatisticas(fila)
        case "6":
            print('Muito obrigado por usar nosssos serviços!')
            break
        case _:
            print('Digite um valor entre 1 e 6')
            continue