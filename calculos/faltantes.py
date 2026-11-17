from calculos.frequencia import gerar_frequencia
from random import choice, choices


def ultimo_jogos(base_dados):
    """
    Encontra a quantidade de jogos realizados posteriormente ao último ciclo fechado.

    :param base_dados: DataFrame da base de dados.

    :return: a quantidade de jogos.
    """

    dados = base_dados.copy()

    if 'Ciclo' in dados.columns and not dados['Ciclo'].empty:
        maior = max(dados['Ciclo'])
        if maior > 0:
            ciclo = int(dados.query(f'Ciclo == {maior}')['Concurso'].index[0])
            jogos = len(dados.iloc[ciclo + 1:])
            if jogos > 0:
                return jogos

    return max(1, min(5, len(dados) % 5 or 1))


def numeros_faltantes_ciclo(base_dados):
    """
    Obtem o(s) número(s) faltante(s) para fechar o ciclo das dezenas.

    :param base_dados: DataFrame da base de dados.

    :return: o(s) número(s) faltante(s) sorteado(s) e o percentual de reajuste de peso.
    """

    dados = base_dados.copy()
    jogos = ultimo_jogos(dados)
    frequencia = gerar_frequencia(dados)

    maior_peso = 0
    for chave, valor in frequencia[0].items():
        maior_peso = valor
        break

    colunas_falta = [f'F{i}' for i in range(1, 11)]
    if all(coluna in dados.columns for coluna in colunas_falta):
        relacao_numeros = list(dados.iloc[-1, 22:32].values)
        num_faltantes = [numero for numero in relacao_numeros if numero > 0]
        numeros = num_faltantes[:]
        qtde_faltantes = len(numeros)

        pesos = list()
        peso = dict()
        jogo = list()
        faltantes = list()

        if jogos == 1:
            for i in range(1, 8):
                jogo.append(i)
                peso[i] = len(dados.query(f'Jogo == 2 & Falta == {i}'))

            for k, v in peso.items():
                pesos.append(v)

            n_dz = choices(jogo, weights=pesos, k=1)

            for j in range(n_dz[0]):
                numero_sorteado = choice(numeros)
                numeros.remove(numero_sorteado)
                faltantes.append(numero_sorteado)

            restantes = [numero for numero in num_faltantes if numero not in faltantes]
            return faltantes, maior_peso, restantes, maior_peso // 2

        elif jogos == 2:
            for i in range(0, qtde_faltantes + 1):
                jogo.append(i)
                peso[i] = len(dados.query(f'Jogo == 3 & Falta == {i}'))

            for k, v in peso.items():
                pesos.append(v)

            n_dz = choices(jogo, weights=pesos, k=1)

            for j in range(n_dz[0]):
                numero_sorteado = choice(numeros)
                numeros.remove(numero_sorteado)
                faltantes.append(numero_sorteado)

            if qtde_faltantes == n_dz[0] or n_dz[0] == 0:
                return num_faltantes, maior_peso

            elif 1 < qtde_faltantes != n_dz[0] and n_dz[0] > 0:
                restantes = [numero for numero in num_faltantes if numero not in faltantes]
                return faltantes, maior_peso, restantes, maior_peso // 2

        elif jogos == 3:
            for i in range(0, qtde_faltantes + 1):
                jogo.append(i)
                peso[i] = len(dados.query(f'Jogo == 4 & Falta == {i}'))

            for k, v in peso.items():
                pesos.append(v)

            n_dz = choices(jogo, weights=pesos, k=1)

            for j in range(n_dz[0]):
                numero_sorteado = choice(numeros)
                numeros.remove(numero_sorteado)
                faltantes.append(numero_sorteado)

            if qtde_faltantes == n_dz[0] or n_dz[0] == 0:
                return num_faltantes, maior_peso

            elif 1 < qtde_faltantes != n_dz[0] and n_dz[0] > 0:
                restantes = [numero for numero in num_faltantes if numero not in faltantes]
                return faltantes, maior_peso, restantes, maior_peso // 2

        elif jogos == 4:
            for i in range(0, qtde_faltantes + 1):
                jogo.append(i)
                peso[i] = len(dados.query(f'Jogo == 5 & Falta == {i}'))

            for k, v in peso.items():
                pesos.append(v)

            n_dz = choices(jogo, weights=pesos, k=1)

            for j in range(n_dz[0]):
                numero_sorteado = choice(numeros)
                numeros.remove(numero_sorteado)
                faltantes.append(numero_sorteado)

            if qtde_faltantes == n_dz[0] or n_dz[0] == 0:
                return num_faltantes, maior_peso

            elif 1 < qtde_faltantes != n_dz[0] and n_dz[0] > 0:
                restantes = [numero for numero in num_faltantes if numero not in faltantes]
                return faltantes, maior_peso, restantes, maior_peso // 2

        return num_faltantes, maior_peso

    ultimos = [int(numero) for numero in dados.iloc[-1, 2:17].tolist()]
    conjunto_total = set(range(1, 26))
    faltantes = sorted(conjunto_total.difference(ultimos))
    if not faltantes:
        faltantes = list(range(1, 11))

    return [faltantes[:10]], maior_peso

