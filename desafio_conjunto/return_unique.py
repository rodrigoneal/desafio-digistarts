from random import randint

'''
Modo mais simples usando o set que não aceita valores repetitos
'''


def unique_with_set(cont: int) -> list[int]:
    if isinstance(cont, int):
        lista = [randint(1, 1000) for _ in range(cont)]
        return sorted(set(lista))
    else:
        raise TypeError('The attribute must be of type int')


'''
Modo mais trabalhando usando for e verificando se o valor está na lista
'''


def unique_with_for(cont: int) -> list[int]:
    if isinstance(cont, int):
        lista = [randint(-1000, 1000) for _ in range(cont)]
        unique = list()
        for i in lista:
            if i not in unique:
                unique.append(i)
        unique.sort()
        return unique
    else:
        raise TypeError('The attribute must be of type int')