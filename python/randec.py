import random

def choice(li) -> tuple:
    """
    Escoge entre una lista de cosas
    :param params: lista separada por comas
    :rtype: tuple
    """
    li = [i.strip() for i in li.split(',')]
    li = list(filter(None, li))
    return random.choices(li)[0]

print(choice(input("Lista: ")))
