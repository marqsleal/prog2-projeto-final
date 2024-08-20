from modulo_mensagens import msg

def lista_produtos_ativos(produtos):
    produtos_ativos = list(filter(lambda x: x['ativo'], produtos.copy()))
    for produto in produtos_ativos:
        for chave, valor in produto.items():
            if chave == 'id':
                print(f'\tID do Produto: {valor}')
            elif chave != 'ativo':
                print(f'\t{chave}: {valor}')
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
    msg('sucesso', f"{produto['nome']} adicionado!\n")


def atualiza_produto(produtos, produto_id, **produto_atualizacao):
    for produto in produtos:
        if produto['id'] == produto_id and produto.get('ativo', False):
            for chave, valor in produto_atualizacao.items():
                if chave in produto:
                    if chave == 'valor':
                        produto[chave] = float(valor)
                    else:
                        produto[chave] = valor
            msg('sucesso', f"Produto de ID {produto['id']} atualizado com sucesso!\n")
            break
    else:
        msg('erro', "Produto não encontrado.\n")


def desativa_produto(produto_id, produtos):
    for produto in produtos:
        if produto['id'] == produto_id and produto.get('ativo', False):
            produto['ativo'] = False
            msg('sucesso', f"Produto excluído com sucesso!\n")
            break
    else:
        msg('erro', "Produto não encontrado.\n")