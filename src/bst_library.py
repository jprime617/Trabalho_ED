class Node:
    def __init__(self, team):
        self.team = team    # objeto Team
        self.left = None
        self.right = None


class BST_A:
    def __init__(self, key):
        """
        key: função que define como os nós serão ordenados
        ex: lambda t: t.name   (ordem alfabética)
            lambda t: t.score  (ordem por gols)
        """
        self.root = None
        self.key = key

    # ---------------------------
    # INSERÇÃO
    # ---------------------------P
    def insert(self, team):
        self.root = self._insert(self.root, team)

    def _insert(self, node, team):
        if node is None:
            return Node(team)

        if self.key(team) < self.key(node.team):
            node.left = self._insert(node.left, team)
        else:
            node.right = self._insert(node.right, team)

        return node

    # ---------------------------
    # INORDER
    # ---------------------------
    def inorder(self):
        lista = []
        self._inorder(self.root, lista)
        return lista

    def _inorder(self, node, lista):
        if node:
            self._inorder(node.left, lista)
            lista.append(node.team)
            self._inorder(node.right, lista)
