"""Zadanie 2 lista 4"""
import random


def dfs_traverse(lista):
    """Funkcja wyswietlajaca drzewo w porzadku inorder"""
    yield from dfs_traverse(lista[1]) if lista[1] is not None else ()
    yield lista[0]
    yield from dfs_traverse(lista[2]) if lista[2] is not None else ()


def binary_tree(lista, i):
    """Funkcja pomocnicza, ktora uklada posortowana liste w drzewo"""
    if i < len(lista):
        return [lista[i], binary_tree(lista, 2 * i + 1), binary_tree(lista, 2 * i + 2)]
    else:
        return None


def tree_generator(k):
    """Funkcja generujaca drzewo o podanej wysokosci"""
    elements = sum(2 ** n for n in range(0, k + 1))
    random_list = random.sample(range(1, elements * 2), elements)

    random_list = sorted(random_list)

    return binary_tree(random_list, 0)


def bfs_traverse(lista):
    """Przejscie bfs"""
    nodes = [lista[1], lista[2]]

    yield lista[0]
    for q in nodes:
        yield q[0] if q[0] is not None else ()
        nodes.append(q[1]) if q[1] is not None else ()
        nodes.append(q[2]) if q[2] is not None else ()


LISTA = ["1", ["2", ["4", ["8", None, None], ["9", None, None]], ["5", None, None]],
         ["3", ["6", None, None], ["7", None, None]]]

print(tree_generator(3))
print(list(bfs_traverse(LISTA)))
