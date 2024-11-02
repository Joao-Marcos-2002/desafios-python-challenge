

# Author: Luiz Fernando

# resolver problema de nao calcular o que vem depois do maior numero
# Descobre o maior valor da lista e o maior index que guarda esse valor
def ultimomaior(lista: list) -> int:
    maior = 0
    maioridx = 0
    for idx, i in enumerate(lista):
        if i >= maior:
            maior = i
            maioridx = idx

    return maioridx


# Forma uma lista a partir do index do maior e vira esta lista
def listavirada(lista, maioridx) -> list:
    nvlista = []
    for idx, i in enumerate(lista):
        if idx >= maioridx:
            nvlista.append(i)
    nvlista.reverse()

    return nvlista


# calcula a agua acumulada dentro da lista(só funciona até o maior elemento)
def calcula_area(lista: list, maior1, idx1, maior2, idx2) -> int:
    blocos = 0
    larg = idx2 - idx1 - 1
    area = larg * min(maior1, maior2)
    for i in range(idx1+1, idx2):
        blocos += lista[i]
    agua = area - blocos
    print(f'blocos:{blocos}')
    print(f'area:{area}')
    print(f'agua na regiao: {agua}')
    return agua


# utiliza outras funções e controla o fluxo(faz funcionar td)
def funcao(lista: list) -> int:
    maior1 = 0
    idx1 = 0
    maior2 = 0
    idx2 = 0
    agua = 0
    for idx, i in enumerate(lista):

        if maior1 != 0 and maior2 == 0 and i >= maior1:
            maior2 = i
            idx2 = idx
            agua += calcula_area(lista, maior1, idx1, maior2, idx2)
            maior1 = maior2
            maior2 = 0

        if i >= maior1:
            maior1 = i
            idx1 = idx
    return agua


# utiliza todas funções acima para resolver o problema
def resolve(lista: list) -> int:
    maior = ultimomaior(lista)
    nvlista = listavirada(lista, maior)
    agua = funcao(nvlista)
    agua += funcao(lista)
    print(f'Total de agua acumulada: {agua}')
    return agua


# --Main--
lista = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
resolve(lista)
