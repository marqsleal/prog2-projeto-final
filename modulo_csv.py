import os
import csv
import json

def carrega_produtos_csv(path):
    produtos = []
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Nenhum produto encontrado no banco de dados. Por favor, cadastre novos no sistema")

        with open(path, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
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
                    except (ValueError, KeyError) as e:
                        print(f"[ERRO]: Erro ao processar o produto {row}: {e}. Linha ignorada.\n")

    except FileNotFoundError as e:
        print(f"[AVISO]: {e}.\n")
    except PermissionError:
        print(f"[ERRO]: Permissão negada ao tentar abrir o arquivo {path}.\n")
    except Exception as e:
        print(f"[ERRO]: Erro inesperado: {e}.\n")
    return produtos


def persistir_produtos_csv(produtos, path):
    if not produtos:
        return

    fieldnames = ['id', 'nome', 'descricao', 'quantidade', 'valor', 'ativo', 'categoria']
    try:
        with open(path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for produto in produtos:
                writer.writerow(produto)
    except PermissionError:
        print(f"[ERRO]: Permissão negada ao tentar escrever no arquivo {path}.\n")
    except Exception as e:
        print(f"[ERRO]: Erro inesperado ao persistir produtos: {e}.\n")


def carrega_vendas_csv(path):
    vendas = []
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Nenhuma venda encontrada no banco de dados. Por favor, faça novas compras no sistema")

        with open(path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    produtos = json.loads(row['produtos'])
                    venda = {
                        'id': int(row['id']),
                        'produtos': produtos,
                        'valor_total': float(row['valor_total']),
                        'data_hora': row['data_hora']
                    }
                    vendas.append(venda)
                except (ValueError, KeyError, json.JSONDecodeError) as e:
                    print(f"[ERRO]: Erro ao processar a venda {row}: {e}. Linha ignorada.\n")
    except FileNotFoundError as e:
        print(f"[AVISO]: {e}.\n")
    except PermissionError:
        print(f"[ERRO]: Permissão negada ao tentar abrir o arquivo {path}.\n")
    except Exception as e:
        print(f"[ERRO]: Erro inesperado ao carregar vendas: {e}.\n")
    return vendas


def persistir_vendas_csv(vendas, path):
    if not vendas:
        return

    fieldnames = ['id', 'produtos', 'valor_total', 'data_hora']
    try:
        with open(path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for venda in vendas:
                venda['produtos'] = json.dumps(venda['produtos'], ensure_ascii=False)
                writer.writerow(venda)
    except PermissionError:
        print(f"[ERRO]: Permissão negada ao tentar escrever no arquivo {path}.\n")
    except Exception as e:
        print(f"[ERRO]: Erro inesperado ao persistir vendas: {e}.\n")