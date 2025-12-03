# src/avl.py
class AVLNode:
    """
    Classe que representa um nó em uma árvore AVL (balanceada).
    Cada nó tem chave, valor, filhos esquerdo/direito e altura para balanceamento.
    """
    def __init__(self, key, value):
        # Inicializa o nó com chave, valor, filhos nulos e altura 1
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """
    Classe que implementa uma árvore AVL balanceada.
    Usada para organizar seleções por pontos, mantendo o balanceamento.
    """ 
    def __init__(self):
        # Inicializa a árvore com raiz nula
        self.root = None

    def insert(self, key, value):
        # Insere um novo nó na AVL, realizando rotações se necessário para manter o balanceamento
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        # Método auxiliar recursivo para inserir e balancear a árvore
        if not node:
            return AVLNode(key, value)
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        # Atualiza a altura do nó atual
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        # Calcula o fator de balanceamento
        balance = self._get_balance(node)

        # Realiza rotações para balancear a árvore
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)
        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def _left_rotate(self, z):
        # Realiza uma rotação à esquerda para balancear a árvore
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _right_rotate(self, z):
        # Realiza uma rotação à direita para balancear a árvore
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        return y

    def _get_height(self, node):
        # Retorna a altura de um nó (0 se nulo)
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        # Calcula o fator de balanceamento de um nó
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def height(self):
        # Retorna a altura da árvore (altura da raiz)
        return self._get_height(self.root)
