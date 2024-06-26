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
            self.root = None
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


class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self, values):
        self.root = None
        if not values:
            return
        prev = None
        for value in values:
            node = LinkedListNode(value)
            if prev:
                prev.next = node
            if self.root is None:
                self.root = node
            prev = node


# Implement the functions below

def list_sum(l: list[int]) -> int:
    """
    returns the sum of the elements. Must use the method pop and can't use loops (while or for).
    """
    if len(l) > 0:
        element = l.pop()
        return list_sum(l) + element
    return 0


def digit_sum(n: int) -> int:
    """
    returns the sum of the digits.
    For example: digit_sum(123) should return 6. Your function can't convert the number to a string. 
    It must use only mathematical operations.
    """
    if n > 0:
        print(n % 10)
        return digit_sum(n//10) + n % 10
    return 0


def tree_sum(root: TreeNode) -> int:
    """
    returns the sum of the node values of the binary tree.
    """
    if root is None:
        return 0

    if root.value is None:
        return 0

    return root.value + tree_sum(root.left) + tree_sum(root.right)


def tree_max(root: TreeNode) -> int:
    """
    returns the maximum value of the binary tree (it is not sorted in any way).
    """
    if root is None:
        return float("-inf")
    if root.value is None:
        return float("-inf")
    return max(root.value, tree_max(root.left), tree_max(root.right))


def k_combinations(l: list[int], k: int) -> list[list[int]]:
    """
    returns a list with all possible combinations of k elements (the order doesn't matter).
    Example: for l = [1, 2, 3, 4] and k = 2 your function must return 
    [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]].
    l = [1, 2, 3, 4]
    k = 1
    [1], [2], [3], [4]

    """
    if k == 0:
        return [[]]
    if len(l) == 0 or len(l) < k:
        return []

    with_first = [
        [l[0]] + combo for combo in k_combinations(l[1:], k - 1)]
    without_first = k_combinations(l[1:], k)

    return with_first + without_first


def all_strictly_increasing_sequences(k: int, n: int, start=1) -> list[list[int]]:
    """
    returns all strictly increasing sequences of length k such that all elements belong 
    to the first n natural numbers. You can use the kwargs however you see fit.

    Example: for k=2 and n=3 your function must return [[1,2],[1,3],[2,3]].
    """
    if k == 1:
        return [[i] for i in range(start, n + 1)]

    sequences = []
    for i in range(start, n + 1):
        next_sequences = all_strictly_increasing_sequences(k - 1, n, i + 1)
        for seq in next_sequences:
            sequences.append([i] + seq)

    return sequences


def create_pattern(n: int) -> list[int]:
    """
    returns a list that follows the pattern below without using a loop (for or while)
    and only appending elements to the end of the pattern.

    n=16 should return [16, 11, 6, 1, -4, 1, 6, 11, 16];
    n=10 should return [10, 5, 0, 5, 10].

    Essentially, the sequence subtracts 5 until a negative number (or zero) is reached 
    and then adds 5 until the original number is reached again.

    This problem appeared in an interview from Microsoft.
    """

    if n <= 0:
        return [n]

    result = create_pattern(n-5)

    return [n] + result + [n]


def find_middle(head: LinkedListNode) -> LinkedListNode:
    """
    return the node in the middle of the linked list. Examples:

    The list 1->2->3->4->5 should return 3;
    The list 1->2->3->4->5->6 should return 4
    """
    # Don't change this function
    return find_middle_rec(head)[1]


def find_middle_rec(head: LinkedListNode, n: int = 0) -> tuple[int, LinkedListNode]:
    # Hint: n will be used to count nodes from left to right and
    # the number returned by the function will be used to count the nodes from right to left
    # TODO: Implement this function

    if head is None:
        return n, head

    dist_from_end, middle = find_middle_rec(head.next, n + 1)

    if n == dist_from_end // 2:
        middle = head

    return dist_from_end, middle
