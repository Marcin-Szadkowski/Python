"""Zadanie 3 lista 4"""
import random
from random import randint


class Node(object):
    """Klasa reprezentująca węzeł w drzewie"""
    def __init__(self, value, *args):
        self.value = value
        self.children = list(args)

    def insert_child(self, child):
        """Funkcja dodająca potomka"""
        self.children.append(child)


def bfs_traverse(root):
    """Funkcja przechodzaca drzewo w porządku bfs"""
    not_visited = [root]
    while not_visited:
        current_node = not_visited.pop(0)
        yield current_node.value
        for child in current_node.children:
            not_visited.append(child)


def dfs_traverse(root):
    """Funkcja przechodząca drzewo w porządku dfs"""
    if root.value is not None:
        yield root.value
    for child in root.children:
        yield from dfs_traverse(child)
    

def tree_generator(k):
    """Generator losowego drzewa"""
    elements = sum(2**n for n in range(0, k+1))
    random_list = random.sample(range(1, elements+1), elements)

    root = Node(randint(1, 20))
    nodes = [root]
    """Najpierw do listy dodajemy k wezlow tak aby drzewo na pewno mialo wysoksoc k"""
    for i in range(0, k):
        nodes.append(Node(randint(1, elements)))
        nodes[i].insert_child(nodes[i+1])

    for i in range(0, elements-k):
        """wybieramy wezel, do ktorego zrobimy dowiazanie"""
        j = randint(0, len(nodes)-1)
        node = Node(random_list.pop(0))
        nodes[j].insert_child(node)
        """dodajemy wierzcholek do listy"""
        nodes.append(node)
    return root


tree = tree_generator(3)

print(list(dfs_traverse(tree)))
print(list(bfs_traverse(tree)))
