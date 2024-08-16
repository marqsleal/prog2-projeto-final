
# Funções: 

## Carregar produtos CSV
    Recebe produtos.csv
    Retorna : dicionario de produtos

## Persistir produtos CSV
    Recebe dicionario de produtos
    Write dict produtos em produtos.csv

## Carregar vendas CSV
    Recebe vendas.csv
    Retorna : dicionario de vendas

## Persistir vendas CSV
    Recebe dicionario de vendas
    Write dict vendas em vendas.csv
    Retorna : Nada

## Listar Produtos (Ativos)
    Listar todos
    por Categoria
    Imprime produtos
    Retorna : Nada

## Buscar Produto (Ativos)
    por ID
    por Nome
    Retorna : Produto

## Cadastrar Produto
    Recebe dicionario produtos
    Nome, Categoria, Quantidade e Valor
    update dicionario
    Imprime produto
    Retorna : Nada

## Atualizar Produto
    Recebe ID e dicionario produtos
    update dicionario
    imprime produto atualizado
    Retorna : Nada

## Excluir Produto (Desativar Produto/Exclusão lógica)
    Recebe ID e dicionario produtos
    Busca produto por id
    Imprime produto
    update dicionario
    Retorna : Nada

## Listar Vendas
    Listar todas
    Imprime vendas
    Retorna : nada

## Buscar Venda
    por ID
    Retorna : Venda

## Realizar Venda
    Recebe dicionario de produtos, dicionario de vendas
    Escolher produto, listar produto escolhido, confirmar e adicionar quantidade
    update no dict produtos pra ajudar o estoque
    gerar e update no dict vendas
    Imprime a venda
    Retorna : nada

## Rowback
    Carregar produtos CSV
    Carregar vendas CSV
    Retorna : nada

# Variáveis: 

## Produto:
    Dict
    id : Int
    nome : String
    categoria : String
    quantidade : Int
    valor: Float
    ativo : Boolean

## Vendas:
    Dict
    id : Int
    produtos : Lista de Produto
    valor : Float