import os
from modulo_mensagens import menu
from modulo_interface import user_interface
from modulo_auxiliar import input_numero, sair

def main():
    # Path dos arquivos
    base_dir = os.getcwd()
    path_pasta = os.path.join(base_dir, 'dados')

    # caso a pasta não exista, vamos criá-la
    os.makedirs(path_pasta, exist_ok=True)

    path_produtos = os.path.join(path_pasta, 'produtos.csv')
    path_vendas = os.path.join(path_pasta, 'vendas.csv')

    while True:
        menu()
        opcao = input_numero('Digite a opção: ', valores_validos=[1, 2, 3, 4, 5, 6, 7])
        if user_interface(opcao, path_produtos, path_vendas):
            sair()


if __name__ == '__main__':
    main()