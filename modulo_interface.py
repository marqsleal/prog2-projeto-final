from modulo_csv import carrega_produtos_csv, persistir_produtos_csv, carrega_vendas_csv, persistir_vendas_csv
from modulo_vendas import lista_vendas, inicia_venda
from modulo_auxiliar import input_numero, input_texto
from modulo_crud import lista_produtos_ativos, cadastra_produto, atualiza_produto, desativa_produto
from modulo_mensagens import msg

def user_interface(comando, path_produtos, path_vendas):

    produtos = carrega_produtos_csv(path_produtos)
    produtos_ativos = []
    vendas = carrega_vendas_csv(path_vendas)

    if produtos:
        produtos_ativos = list(filter(lambda x: x['ativo'], produtos))

    match comando:
        case 1:
            if not produtos_ativos:
                msg('aviso', 'Não é possível visualizar os produtos, pois não há produtos cadastrados no sistema.\n')
                return

            print("Visualizando produtos...")
            msg('aviso', f"Existem {len(produtos_ativos)} produtos no sistema!")
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
            if not produtos_ativos:
                msg('aviso', 'Não é possível atualizar, pois não há produtos cadastrados no sistema.\n')
                return

            print("Atualizando produto existente: \n")
            produtos_atualizacao = {}
            produtos_ids = list(map(lambda x: x['id'], produtos_ativos))
            produto_id = input_numero('Digite o id do produto a ser atualizado: ', valores_validos=produtos_ids)
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
            if not produtos_ativos:
                msg('aviso', 'Não é possível excluir um produto, pois não há produtos cadastrados no sistema.\n')
                return

            msg('aviso', "Excluindo produto...")
            produto_id = input_numero('Digite o id do produto a ser excluído: ')
            desativa_produto(produto_id, produtos)

        case 5:
            if not vendas:
                msg('aviso', 'Não é possível visualizar o relatório, pois não há vendas cadastradas no sistema.\n')
                return

            print("Visualizando relatório de vendas: \n")
            lista_vendas(vendas)

        case 6:
            msg('aviso', "Efetuando venda: \n")
            inicia_venda(produtos, vendas)

        case 7:
            return True

    persistir_produtos_csv(produtos, path_produtos)
    persistir_vendas_csv(vendas, path_vendas)