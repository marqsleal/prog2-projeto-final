import csv
import json
import functools
from datetime import datetime

# CSV
def carrega_produtos_csv(path):
    produtos = []
    with open(path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            produto = {
                'id': int(row['id']),
                'nome': row['nome'],
                'descricao': row['descricao'],
                'quantidade': int(row['quantidade']),
                'valor': float(row['valor']),
                'ativo': row['ativo'].lower() == 'true',
                'categoria': row['categoria']
            }
            produtos.append(produto)
    return produtos


def persistir_produtos_csv(produtos, path):
    fieldnames = ['id', 'nome', 'descricao', 'quantidade', 'valor', 'ativo', 'categoria']
    with open(path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for produto in produtos:
            writer.writerow(produto)


def carrega_vendas_csv(path):
    vendas = []
    with open(path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            produtos_str = row['produtos'].replace('""', '"')
            produtos = json.loads(produtos_str)
            venda = {
                'id': int(row['id']),
                'produtos': produtos,
                'valor_total': float(row['valor_total']),
                'data_hora': row['data_hora']
            }
            vendas.append(venda)
    return vendas


def persistir_vendas_csv(vendas, path):
    fieldnames = ['id', 'produtos', 'valor_total', 'data_hora']
    with open(path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for venda in vendas:
            venda['produtos'] = json.dumps(venda['produtos'], ensure_ascii=False)
            writer.writerow(venda)


# Produtos
def lista_produtos_ativos(produtos):
    produtos_ativos = list(filter(lambda x: x['ativo'], produtos))
    for produto in produtos_ativos:
        for chave, valor in produto.items():
            if chave == 'id':
                print(f'ID do Produto {chave}: {valor}')
            elif chave != 'ativo':
                print(f'    {chave}: {valor}')
        print("\n")


def cadastra_produto(produtos, produto_id, produto_nome, produto_descricao, produto_quantidade, produto_valor, produto_categoria):
    produto = {
        'id': produto_id,
        'nome': produto_nome,
        'descricao': produto_descricao,
        'quantidade': produto_quantidade,
        'valor': produto_valor,
        'ativo': True,
        'categoria': produto_categoria
    }
    produtos.append(produto)
    print(f'{produto['nome']} adicionado!\n')


def atualiza_produto(produtos, produto_id, **produto_atualizacao):
    for produto in produtos:
        if produto['id'] == produto_id and produto.get('ativo', False):
            for chave, valor in produto_atualizacao.items():
                if chave in produto:
                    if chave == 'valor':
                        produto[chave] = float(valor)
                    else:
                        produto[chave] = valor
            print(f"Produto ID {produto['id']} atualizado com sucesso!\n")
            break
    else:
        print("Produto não encontrado.\n")


def desativa_produto(produto_id, produtos):
    for produto in produtos:
        if produto['id'] == produto_id and produto.get('ativo', False):
            produto['ativo'] = False
            print(f'{produto['id']} excluído com sucesso!\n')
            break
    else:
        print("Produto não encontrado.\n")


# Vendas
def gera_recibo(venda):
    venda_id = venda['id']
    venda_produtos = json.dumps(venda['produtos'])
    venda_valor_total = venda['valor_total']
    venda_data_hora = venda['data_hora']

    path = f"recibos/{venda_id} {venda_data_hora.replace(':', '-').replace(' ', '_')}.csv"

    dados = [venda_id, venda_produtos, venda_valor_total, venda_data_hora]

    with open(path, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
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
    venda_valor_total = round(functools.reduce(lambda total, item: total + (item['valor'] * item['quantidade']), venda_produtos, 0.0), 2)

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
            if produto['quantidade'] >= produto_quantidade: #aq
                produto['quantidade'] -= produto_quantidade
                return True
            else:
                print(f'Produto {produto['nome']} com estoque insuficiente ({produto['quantidade']})')
                return False
    print(f'id {produto_id} inválido!')
    return False


def inicia_venda(produtos, vendas):
    proximo_produto = 'y'
    produtos_vendas = []
    produtos_ativos = list(filter(lambda x: x['ativo'], produtos.copy())) #aq

    while proximo_produto == 'y':
        produto_id = int(input("Digite o id do produto: "))
        produto_quantidade = int(input("Digite a quantidade do produto: "))

        if valida_produto(produtos_ativos, produto_id, produto_quantidade):
            produto = {
                'id': produto_id,
                'quantidade': produto_quantidade
            }
            produtos_vendas.append(produto)

        proximo_produto = input('Deseja adicionar outro produto? (Y/N').lower()

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

# User Interface
def user_interface(comando, path_produtos, path_vendas):
    produtos = carrega_produtos_csv(path_produtos)
    vendas = carrega_vendas_csv(path_vendas)

    match comando:
        case 1:
            print("Visualizando produtos: \n")
            lista_produtos_ativos(produtos)

        case 2:
            print("Cadastrando novo produto: \n")
            produto_id = (len(produtos)) + 1
            produto_nome = input("Digite o nome do produto: ").lower()
            produto_descricao = input("Digite a descrição do produto: ").lower()
            produto_quantidade = int(input("Digite a quantidade do produto no estoque: "))
            produto_valor = float(input("Digite o valor do produto: "))
            produto_categoria = input("Digite a categoria do produto: ").lower()

            cadastra_produto(produtos, produto_id, produto_nome, produto_descricao, produto_quantidade, produto_valor, produto_categoria)

        case 3:
            print("Atualizando produto existente: \n")
            produtos_atualizacao = {}
            produto_id = int(input('Digite o id do produto a ser atualizado: '))
            produto_nome = input('Digite para alterar o nome do produto (caso inalterado, precione ENTER): ').lower()
            produto_descricao = input('Digite para alterar a descrição do produto (caso inalterado, precione ENTER): ').lower()
            produto_quantidade = input('Digite para alterar a quantidade do produto no estoque (caso inalterado, precione ENTER): ')
            produto_valor = input('Digite para alterar o valor do produto (caso inalterado, precione ENTER): ')
            produto_categoria = input('Digite para alterar a categoria do produto (caso inalterado, precione ENTER): ').lower()

            if produto_nome != '':
                produtos_atualizacao['nome'] = produto_nome

            if produto_descricao != '':
                produtos_atualizacao['descricao'] = produto_descricao

            if produto_quantidade != '':
                produtos_atualizacao['quantidade'] = produto_quantidade

            if produto_valor != '':
                produtos_atualizacao['valor'] = produto_valor

            if produto_categoria != '':
                produtos_atualizacao['categoria'] = produto_categoria

            atualiza_produto(produtos, produto_id, **produtos_atualizacao)

        case 4:
            print("Excluindo produto: \n")
            produto_id = int(input('Digite o id do produto a ser excluído: '))
            desativa_produto(produto_id, produtos)

        case 5:
            print("Visualizando relatório de vendas: \n")
            lista_vendas(vendas)

        case 6:
            print("Efetuando venda: \n")
            inicia_venda(produtos, vendas)

        case _:
            return

    persistir_produtos_csv(produtos, path_produtos)
    persistir_vendas_csv(vendas, path_vendas)


def main():
    path_produtos = "dados/produtos.csv"
    path_vendas = "dados/vendas.csv"

    user_interface(1, path_produtos, path_vendas)
    user_interface(6, path_produtos, path_vendas)
    user_interface(5, path_produtos, path_vendas)
    user_interface(1, path_produtos, path_vendas)


    print("Programa Finalizado!")

if __name__ == '__main__':
    main()