import csv
import json
import functools
from datetime import datetime


def carrega_produtos_csv(path):
    produtos = []
    with open(path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            produto = {
                'id': int(row['id']),
                'nome': row['nome'],
                'quantidade': int(row['quantidade']),
                'valor': float(row['valor']),
                'ativo': row['ativo'].lower() == 'true',
                'categoria': row['categoria']
            }
            produtos.append(produto)
    return produtos


def persistir_produtos_csv(produtos, path):
    return


def carrega_vendas_csv(path):
    vendas = []
    with open(path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            venda = {
                'id': int(row['id']),
                'produtos': json.loads(row['produtos'].replace('""', '"')),
                'valor_total': float(row['valor_total']),
                'data_hora': row['data_hora']
            }
            vendas.append(venda)
    return vendas


def persistir_vendas_csv(vendas, path):
    return


def lista_produtos_ativos(produtos):
    print("Listando os produtos ativos: \n")
    produtos_ativos = list(filter(lambda x: x['ativo'], produtos))
    for produto in produtos_ativos:
        for chave, valor in produto.items():
            if chave == 'id':
                print(f'ID do Produto {chave}: {valor}')
            elif chave != 'ativo':
                print(f'    {chave}: {valor}')
        print("\n")


def cadastra_produto(produtos):
    produto_id = (len(produtos))+1
    produto_nome = input("Digite o nome do produto: ").lower()
    produto_quantidade = int(input("Digite a quantidade do produto no estoque: "))
    produto_valor = float(input("Digite o valor do produto: "))
    produto_categoria = input("Digite a categoria do produto: ").lower()
    produto = {
        'id': produto_id,
        'nome': produto_nome,
        'quantidade': produto_quantidade,
        'valor': produto_valor,
        'ativo': True,
        'categoria': produto_categoria
    }
    produtos.append(produto)
    print(f'{produto['nome']} adicionado!\n')


def atualiza_produto(produtos):
    produto_id = int(input('Digite o id do produto a ser atualizado: '))
    produto_nome = input('Digite para alterar o nome do produto (caso inalterado, precione ENTER): ').lower()
    produto_quantidade = input('Digite para alterar a quantidade do produto no estoque (caso inalterado, precione ENTER): ')
    produto_valor = input('Digite para alterar o valor do produto (caso inalterado, precione ENTER): ')
    produto_categoria = input('Digite para alterar a categoria do produto (caso inalterado, precione ENTER): ').lower()

    for p in produtos:
        if p['id'] == produto_id and p['ativo']:
            if produto_nome != '':
                p['nome'] = produto_nome
            if produto_quantidade != '':
                p['quantidade'] = produto_quantidade
            if produto_valor != '':
                p['valor'] = float(produto_valor)
            if produto_categoria != '':
                p['categoria'] = produto_categoria
            print(f'{p['id']} atualizado com sucesso!\n')
            break


def desativa_produto(produtos):
    produto_id = int(input('Digite o id do produto a ser excluído: '))
    for p in produtos:
        if p['id'] == produto_id and p['ativo']:
            p['ativo'] = False
            print(f'{p['id']} excluído com sucesso!\n')
            break



def efetua_venda(produtos, vendas):
    produtos_ativos = list(filter(lambda x: x['ativo'], produtos))
    proximo_produto = 'y'

    venda_id = (len(vendas)) + 1
    venda_valor_total = 0.0
    produtos_vendas = []

    while proximo_produto == 'y':
        produto_id = int(input("Digite o id do produto: "))
        produto_quantidade = int(input("Digite a quantidade do produto: "))

        for produto in produtos_ativos:
            if produto['id'] == produto_id:
                produto_nome = produto['nome']
                produto_valor = produto['valor']

                if produto_quantidade > produto['quantidade']:
                    print(f'{produto['id']} não possui quantidade o suficiente em estoque!\n')
                    break

                produto_venda = {
                    'id': produto_id,
                    'nome': produto_nome,
                    'quantidade': produto_quantidade,
                    'valor': produto_valor
                }

                produtos_vendas.append(produto_venda)

                venda_valor_total += float(produto_valor * produto_quantidade)

                produto['quantidade'] -= produto_quantidade

                print(f'{produto_venda['nome']} adicionado com {produto_venda['quantidade']} unidades\n')
                break

        proximo_produto = input('Deseja adicionar outro produto? (Y/N').lower()


    data_hora_atual = datetime.now()
    venda_data_hora = data_hora_atual.strftime('%Y-%m-%d %H:%M:%S')
    venda_valor_total = round(venda_valor_total, 2)
    venda = {
        'id': venda_id,
        'produtos': produtos_vendas,
        'valor_total': venda_valor_total,
        'data_hora': venda_data_hora
    }

    vendas.append(venda)

    produtos_vendas_str = json.dumps(produtos_vendas)
    venda_str = f'{venda_id},"{produtos_vendas_str}",{venda_valor_total},{venda_data_hora}'

    print(f'Venda registrada com sucesso: {venda_str}')



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


def user_interface(produtos, vendas):
    return


def main():
    path_produtos = "dados/produtos.csv"
    path_vendas = "dados/vendas.csv"
    produtos = carrega_produtos_csv(path_produtos)
    vendas = carrega_vendas_csv(path_vendas)

    efetua_venda(produtos, vendas)
    lista_vendas(vendas)

    print("Programa Finalizado!")

if __name__ == '__main__':
    main()

