# Do not modify the classes below
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, representation: str):
        '''
        representation: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        if not representation:
            return
        nodes = []
        for i, value in enumerate(representation):
            node = None
            if value is not None:
                node = TreeNode(value)
                if i > 0:
                    if i % 2 == 1:
                        parent = nodes[(i - 1) // 2]
                        parent.left = node
                    else:
                        parent = nodes[(i - 2) // 2]
                        parent.right = node
            nodes.append(node)
        self.root = nodes[0]


class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.adjacent = []


class Graph:
    def __init__(self, adjacency: list[list[bool]]):
        '''
        adjacency: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        self.nodes = [GraphNode(i) for i in range(1, len(adjacency) + 1)]
        for node1, row in zip(self.nodes, adjacency):
            for node2, adjacent in zip(self.nodes, row):
                if adjacent and node1 is not node2:
                    node1.adjacent.append(node2)


# Implement the functions below

def pre_order_recursive(root: TreeNode) -> None:
    if root is None:
        return True
    
    print(root.value)
    pre_order_recursive(root.left)
    pre_order_recursive(root.right)

def pre_order_iterative(root: TreeNode) -> None:
    pilha = list()
    
    while root is not None:
        print(root.value)
        pilha.append(root.right)
        root = root.left
    
    while pilha:
        root = pilha.pop()
        while root is not None:
            print(root.value)
            pilha.append(root.right)
            root = root.left


def in_order_recursive(root: TreeNode) -> None:
    if root is None:
        return
    in_order_recursive(root.left)
    print(root.value)
    in_order_recursive(root.right)


def post_order_recursive(root: TreeNode) -> None:
    if root is None:
        return
    post_order_recursive(root.left)
    post_order_recursive(root.right)
    print(root.value)

def breadth_first(root: TreeNode) -> None:
    if root is None: return
    
    fila = list()
    fila.append(root)
    
    while fila:
        primeiro = fila.pop(0)
        print(primeiro.value)
        if primeiro.left: fila.append(primeiro.left) 
        if primeiro.right: fila.append(primeiro.right)
        
    
def graph_depth_first_recursive(node: GraphNode, visited=None) -> None:
    if visited is None:
        visited = set()
    
    if node is None:
        return
    
    print(node.value)
    visited.add(node)
    
    for adj in node.adjacent:
        if adj not in visited:
            graph_depth_first_recursive(adj, visited)
    

def graph_depth_first_iterative(node: GraphNode) -> None:
    if node is None: return
    
    visited = set()
    stack = [node]
    
    while stack:
        this_node = stack.pop()
        print(this_node.value)
        visited.add(this_node)
        for adj in this_node.adjacent:
            if adj not in visited and adj not in stack: 
                stack.append(adj)
    

def graph_breadth_first(node: GraphNode) -> None:
    if node is None: return

    visited = set()
    fila = [node]
    
    while fila:
        this_node = fila.pop(0)
        print(this_node.value)
        visited.add(this_node)
        for adj in this_node.adjacent:
            if adj not in visited and adj not in fila:
                fila.append(adj)
    
