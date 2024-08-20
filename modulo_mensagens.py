cores = {
    'verde': '\033[92m',
    'amarelo': '\033[93m',
    'azul': '\033[94m',
    'vermelho': '\033[91m',
    'reset': '\033[0m'
}

def msg(tipo, texto):
    match tipo:
        case 'erro':
            print(f"{cores['vermelho']}[ERRO]{cores['reset']}: {texto}\n")
        case 'sucesso':
            print(f"{cores['verde']}[INFO]{cores['reset']}: {texto}\n")
        case 'aviso':
            print(f"{cores['amarelo']}[AVISO]{cores['reset']}: {texto}\n")

def menu():
    print(cores['verde'] + "\nBem-vindo ao Sistema de Gerenciamento de Inventário!\n\n" + cores['reset'])
    print(cores['amarelo'] + "Escolha uma das opções do menu abaixo:\n" + cores['reset'])
    print(cores['azul'] + "-------------- PRODUTOS --------------" + cores['reset'])
    print("| 1. Visualizar produtos")
    print("| 2. Cadastrar novo produto")
    print("| 3. Atualizar produto existente")
    print("| 4. Excluir produto")
    print(cores['azul'] + "--------------- VENDAS ---------------" + cores['reset'])
    print("| 5. Visualizar relatório de vendas")
    print("| 6. Realizar uma nova venda")
    print(cores['azul'] + "--------------------------------------" + cores['reset'])
    print("| 7. Sair do sistema")
    print(cores['azul'] + "--------------------------------------" + cores['reset'])
    print(f"Obs.: digite {cores['vermelho']}'SAIR'{cores['reset']} para sair do sistema a qualquer momento.\n")
