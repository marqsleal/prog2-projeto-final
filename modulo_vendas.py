import csv
import json
import os
from functools import reduce
from datetime import datetime
from modulo_auxiliar import input_numero, input_texto


def gera_recibo(venda):
    venda_id = venda['id']
    venda_produtos = json.dumps(venda['produtos'])
    venda_valor_total = venda['valor_total']
    venda_data_hora = venda['data_hora']

    base_dir = os.getcwd()
    path_pasta = os.path.join(base_dir, 'recibos')

    # caso a pasta de recibos não exista, vamos criá-la
    os.makedirs(path_pasta, exist_ok=True)

    nome_arquivo = f"{venda_id}_{venda_data_hora.replace(':', '-').replace(' ', '_')}.csv"
    path = os.path.join(path_pasta, nome_arquivo)

    colunas = ['ID da Venda', 'Produtos', 'Valor Total', 'Data e Hora']
    dados = [venda_id, venda_produtos, venda_valor_total, venda_data_hora]

    with open(path, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(colunas)
        writer.writerow(dados)


# Atualiza o estoque de produtos, carregado e inicializado no começo do programa.
def atualiza_estoque(produtos, produtos_venda):
    for produto_venda in produtos_venda:
        produto_id = produto_venda['id']
        quantidade_vendida = produto_venda['quantidade']
        for produto in produtos:
            if produto['id'] == produto_id:
                if produto['quantidade'] >= quantidade_vendida:
                    produto['quantidade'] -= quantidade_vendida
                break


def finaliza_venda(produtos, vendas, *venda_produtos):
    venda_id = len(vendas) + 1
    data_hora_atual = datetime.now()
    venda_data_hora = data_hora_atual.strftime('%Y-%m-%d %H:%M:%S')
    venda_valor_total = round(reduce(lambda total, item: total + (item['valor'] * item['quantidade']), venda_produtos, 0.0), 2)

    venda = {
        'id': venda_id,
        'produtos': venda_produtos,
        'valor_total': venda_valor_total,
        'data_hora': venda_data_hora
    }

    atualiza_estoque(produtos, venda_produtos)
    gera_recibo(venda)
    vendas.append(venda)

    venda_str = f'{venda_id} - {venda_data_hora}'

    print(f'Venda registrada com sucesso: {venda_str}')


def gera_venda(produtos, produtos_ativos, vendas, *produtos_vendas):
    venda_produtos = []

    for item in produtos_vendas:
        produto_id = item['id']
        produto_quantidade = item['quantidade']

        for produto in produtos_ativos:
            if produto['id'] == produto_id:
                produto_nome = produto['nome']
                produto_valor = produto['valor']
                produto_descricao = produto['descricao']

                produto_venda = {
                    'id': produto_id,
                    'nome': produto_nome,
                    'descricao': produto_descricao,
                    'quantidade': produto_quantidade,
                    'valor': produto_valor
                }

                venda_produtos.append(produto_venda)
                break

    finaliza_venda(produtos, vendas, *venda_produtos)


# Valida o produto e atualiza na memoria da lista produtos_ativos o estoque
# Eu fiz isso caso nosso maior inimigo resolva comprar o mesmo produto 2 vezes
def valida_produto(produtos_ativos, produto_id, produto_quantidade):
    for produto in produtos_ativos:
        if produto['id'] == produto_id:
            if produto['quantidade'] >= produto_quantidade: # >= não apenas >
                return True
            else:
                print(f"Produto {produto['nome']} com estoque insuficiente ({produto['quantidade']})")
                return False
    print(f'id {produto_id} inválido!')
    return False


def inicia_venda(produtos, vendas):
    proximo_produto = 'y'
    produtos_vendas = []
    produtos_ativos = list(filter(lambda x: x['ativo'], produtos.copy())) # .copy() resolve a questão do ponteiro
    produtos_ids = list(map(lambda x: x['id'], produtos_ativos))

    while proximo_produto == 'y':
        produto_id = input_numero("Digite o id do produto: ", valores_validos=produtos_ids)
        produto_quantidade = input_numero("Digite a quantidade do produto: ")

        if valida_produto(produtos_ativos, produto_id, produto_quantidade):
            produto = {
                'id': produto_id,
                'quantidade': produto_quantidade
            }
            produtos_vendas.append(produto)

        proximo_produto = input_texto('Deseja adicionar outro produto? (Y/N)', valores_validos=['y', 'n'])

    if produtos_vendas:
        gera_venda(produtos, produtos_ativos, vendas, *produtos_vendas)
    else:
        print('Nenhum produto válido foi inserido, venda não pode ser iniciada!')


def lista_vendas(vendas):
    print('Relatório de vendas: \n')
    for venda in vendas:
        print(f'ID da Venda: {venda["id"]}')
        produtos = venda['produtos']
        print(f'    Produtos:')
        for produto in produtos:
            for chave, valor in produto.items():
                if chave == 'id':
                    print(f'        ID do Produto {chave}: {valor}')
                else:
                    print(f'            {chave}: {valor}')
        print(f'    Valor Total: {venda["valor_total"]:.2f}')
        print(f'    Data e Hora da venda: {venda["data_hora"]}\n')