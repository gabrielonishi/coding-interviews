def generate_parens(n: int) -> list[str]:
    """
    Returns list of all valid parentheses combinations

    Args:
        n(int): number of pairs of parentheses

    Returns:
        list[str]: list with all combinations

    Examples:
        >>> generate_parens(3):
        ["((()))", "(()())", "(())()", "()(())", "()()()"]
    """

    permutations = {i: set() for i in range(n)}

    permutations[0] = {"()"}

    for i in range(1, n):
        for possibility in permutations[i-1]:
            permutations[i].add("()" + possibility)
            permutations[i].add("(" + possibility + ")")
            permutations[i].add(possibility + "()")

    return list(permutations[n-1])
