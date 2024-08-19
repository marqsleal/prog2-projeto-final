from typing import Type

def converte_numero(num):
    if ('.' in num and ',' in num):
        return num.replace('.', '').replace(',', '.')

    if (',' in num):
        return num.replace(',', '.')

    return num


def input_numero(prompt, opcional=False, tipo: Type = int,
                 valores_validos=None, tam_min=0, tam_max=9999999):
    while True:
        try:
            entrada = input(prompt).strip()

            if not entrada and opcional:
                return ''

            if not entrada:
                raise ValueError("Este campo não pode ficar vazio")

            if tipo == float:
                entrada = converte_numero(entrada)

            valor = tipo(entrada)

            if valor < tam_min:
                raise ValueError(f"O valor não pode ser menor do que {tam_min}")

            if valor > tam_max:
                raise ValueError("O valor inserido é muito grande")

            if valores_validos and valor not in valores_validos:
                raise ValueError(f"Valor inválido. Escolha um destes: {', '.join(map(str, valores_validos))}")

            return valor

        except ValueError as e:
            if "int()" in str(e) or "float" in str(e):
                print("[ERRO]: O valor digitado não é um número ou não é válido. Por favor, tente novamente.\n")
            else:
                print(f"[ERRO]: {e}. Por favor, tente novamente.\n")
        except Exception as e:
            print(f"[ERRO]: Erro inesperado: {e}.\n")


def input_texto(prompt, opcional=False, valores_validos=None, tam_max=100):
    while True:
        try:
            valor = input(prompt).strip().lower()

            if not valor and not opcional:
                raise ValueError("Este campo não pode ficar vazio")

            if valores_validos and valor not in valores_validos:
                raise ValueError(f"Valor inválido. Escolha um destes: {', '.join(valores_validos)}")

            if len(valor) > tam_max:
                raise ValueError(f"O valor não pode conter mais de {tam_max} caracteres")

            return valor

        except ValueError as e:
            print(f"[ERRO]: {e}. Por favor, tente novamente.\n")
        except Exception as e:
            print(f"[ERRO]: Erro inesperado: {e}.\n")