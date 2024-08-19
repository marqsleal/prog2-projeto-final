from modulo_crud import lista_produtos_ativos, cadastra_produto, atualiza_produto, desativa_produto
from modulo_csv import carrega_produtos_csv, persistir_produtos_csv, carrega_vendas_csv, persistir_vendas_csv
from modulo_vendas import lista_vendas, inicia_venda
from modulo_auxiliar import input_numero, input_texto

def menu():
    cores = {
        'verde': '\033[92m',
        'amarelo': '\033[93m',
        'azul': '\033[94m',
        'vermelho': '\033[91m',
        'reset': '\033[0m'
    }

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
    print(cores['azul'] + "--------------------------------------\n\n" + cores['reset'])


def user_interface(comando, path_produtos, path_vendas):
    produtos = carrega_produtos_csv(path_produtos)
    vendas = carrega_vendas_csv(path_vendas)

    match comando:
        case 1:
            if not produtos:
                print('Não é possível visualizar os produtos, pois não há produtos cadastrados no sistema.\n')
                return

            print("Visualizando produtos: \n")
            lista_produtos_ativos(produtos)

        case 2:
            print("Cadastrando novo produto: \n")
            produto_id = (len(produtos)) + 1
            produto_nome = input_texto("Digite o nome do produto: ")
            produto_descricao = input_texto("Digite a descrição do produto (caso não tenha, pressione ENTER): ", opcional=True, tam_max=250)
            produto_quantidade = input_numero("Digite a quantidade do produto no estoque: ")
            produto_valor = input_numero("Digite o valor do produto: ", tipo=float, tam_min=0.05)
            produto_categoria = input_texto("Digite a categoria do produto: ", tam_max=50)

            cadastra_produto(produtos, produto_id, produto_nome, produto_descricao, produto_quantidade, produto_valor, produto_categoria)

        case 3:
            if not produtos:
                print('Não é possível atualizar, pois não há produtos cadastrados no sistema.\n')
                return

            print("Atualizando produto existente: \n")
            produtos_atualizacao = {}
            produto_id = input_numero('Digite o id do produto a ser atualizado: ')
            produto_nome = input_texto('Digite para alterar o nome do produto (caso inalterado, pressione ENTER): ', opcional=True)
            produto_descricao = input_texto('Digite para alterar a descrição do produto (caso inalterado, pressione ENTER): ', opcional=True, tam_max=250)
            produto_quantidade = input_numero('Digite para alterar a quantidade do produto no estoque (caso inalterado, pressione ENTER): ', opcional=True)
            produto_valor = input_numero('Digite para alterar o valor do produto (caso inalterado, pressione ENTER): ', opcional=True, tipo=float, tam_min=0.05)
            produto_categoria = input_texto('Digite para alterar a categoria do produto (caso inalterado, pressione ENTER): ', opcional=True, tam_max=50)

            if produto_nome:
                produtos_atualizacao['nome'] = produto_nome

            if produto_descricao:
                produtos_atualizacao['descricao'] = produto_descricao

            if produto_quantidade:
                produtos_atualizacao['quantidade'] = produto_quantidade

            if produto_valor:
                produtos_atualizacao['valor'] = produto_valor

            if produto_categoria:
                produtos_atualizacao['categoria'] = produto_categoria

            atualiza_produto(produtos, produto_id, **produtos_atualizacao)

        case 4:
            if not produtos:
                print('Não é possível excluir um produto, pois não há produtos cadastrados no sistema.\n')
                return

            print("Excluindo produto: \n")
            produto_id = input_numero('Digite o id do produto a ser excluído: ')
            desativa_produto(produto_id, produtos)

        case 5:
            if not vendas:
                print('Não é possível visualizar o relatório, pois não há vendas cadastradas no sistema.\n')
                return

            print("Visualizando relatório de vendas: \n")
            lista_vendas(vendas)

        case 6:
            print("Efetuando venda: \n")
            inicia_venda(produtos, vendas)

        case 7:
            return True

    persistir_produtos_csv(produtos, path_produtos)
    persistir_vendas_csv(vendas, path_vendas)