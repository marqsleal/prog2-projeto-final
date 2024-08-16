import csv
import json
import functools


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
    produtos_ativos = filter(lambda x: x['ativo'], produtos)
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
    produto_nome = input('Digite o nome do produto (caso inalterado, precione ENTER): ').lower()
    produto_quantidade = input('Digite a quantidade do produto no estoque (caso inalterado, precione ENTER): ')
    produto_valor = input('Digite o valor do produto (caso inalterado, precione ENTER): ')
    produto_categoria = input('Digite a categoria do produto (caso inalterado, precione ENTER): ').lower()

    for p in produtos:
        if p['id'] == produto_id:
            if produto_nome != '':
                p['nome'] = produto_nome
            if produto_quantidade != '':
                p['nome'] = produto_nome
            if produto_valor != '':
                p['valor'] = float(produto_valor)
            if produto_categoria != '':
                p['categoria'] = produto_categoria
            print(f'{p['id']} atualizado com sucesso!\n')
            break


def desativa_produto(produtos):
    produto_id = int(input('Digite o id do produto a ser excluído: '))
    for p in produtos:
        if p['id'] == produto_id:
            p['ativo'] = False
            print(f'{p['id']} excluído com sucesso!\n')
            break



def efetua_venda(produtos, vendas):
    return


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

    atualiza_produto(produtos)

    lista_produtos_ativos(produtos)


    print("Programa Finalizado!")

if __name__ == '__main__':
    main()

