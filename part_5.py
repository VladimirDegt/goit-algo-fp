import matplotlib.pyplot as plt
import networkx as nx
from collections import deque


class Node:
    def __init__(self, value):
        """
        Ініціалізація вузла бінарного дерева.

        :param value: Значення, яке зберігається в вузлі.
        """
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value):
        """
        Ініціалізація бінарного дерева.

        :param root_value: Значення кореневого вузла.
        """
        self.root = Node(root_value)

    def add_left(self, parent, value):
        """
        Додає лівий нащадок до заданого батьківського вузла.

        :param parent: Батьківський вузол.
        :param value: Значення для нового лівого нащадка.
        """
        parent.left = Node(value)

    def add_right(self, parent, value):
        """
        Додає правий нащадок до заданого батьківського вузла.

        :param parent: Батьківський вузол.
        :param value: Значення для нового правого нащадка.
        """
        parent.right = Node(value)

    def depth_first_search(self):
        """
        Обхід дерева в глибину (DFS) за допомогою стека.

        :return: Список значень у порядку обходу.
        """
        visited = []
        stack = [self.root]

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        return visited

    def breadth_first_search(self):
        """
        Обхід дерева в ширину (BFS) за допомогою черги.

        :return: Список значень у порядку обходу.
        """
        visited = []
        queue = deque([self.root])

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return visited


def visualize_tree(traversal_order, tree):
    """
    Візуалізує бінарне дерево з кольоровою зміною вузлів за порядком обходу.

    :param traversal_order: Порядок обходу дерева.
    :param tree: Об'єкт бінарного дерева.
    """
    G = nx.Graph()
    pos = {}  # Позиції вузлів на графі

    # Створення графа на основі дерева
    def add_edges(node, pos_x=0, pos_y=0, layer=1):
        if node is not None:
            G.add_node(node.value, pos=(pos_x, pos_y))
            pos[node.value] = (pos_x, pos_y)
            if node.left:
                G.add_edge(node.value, node.left.value)
                add_edges(node.left, pos_x - 1 / layer, pos_y - 1, layer + 1)
            if node.right:
                G.add_edge(node.value, node.right.value)
                add_edges(node.right, pos_x + 1 / layer, pos_y - 1, layer + 1)

    add_edges(tree.root)

    # Підготовка кольорів для вузлів
    node_colors = []
    color_step = 1 / len(traversal_order)  # Шаг для кольору

    for i, node in enumerate(traversal_order):
        color_value = int(255 * (1 - i * color_step))  # Визначення відтінку
        node_colors.append(f"#{color_value:02X}96F0")

    # Візуалізація графа
    plt.figure(figsize=(12, 8))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2000,
        node_color=node_colors,
        font_size=16,
        font_weight="bold",
    )
    plt.show()


if __name__ == "__main__":
    # Створення бінарного дерева
    tree = BinaryTree(1)
    tree.add_left(tree.root, 2)
    tree.add_right(tree.root, 3)
    tree.add_left(tree.root.left, 4)
    tree.add_right(tree.root.left, 5)
    tree.add_left(tree.root.right, 6)
    tree.add_right(tree.root.right, 7)

    # Візуалізація обходу дерева в глибину
    dfs_order = tree.depth_first_search()
    print("DFS Order:", [node.value for node in dfs_order])
    visualize_tree(dfs_order, tree)

    # Візуалізація обходу дерева в ширину
    bfs_order = tree.breadth_first_search()
    print("BFS Order:", [node.value for node in bfs_order])
    visualize_tree(bfs_order, tree)
