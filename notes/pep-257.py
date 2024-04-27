"""
PEP for docstrings

1. Use triple double quotes
2. Brief summary of function
3. Parameters
4. Return type
5. Examples
6. Raises

Even better if you use Sphinx-style markup
(tool for generating docs with docstrings)
"""


# With Sphinx style
def calculate_area(radius):
    """
    Calculate the area of a circle.

    :param radius: The radius of the circle.
    :type radius: float

    :return: The area of the circle.
    :rtype: float

    :raises ValueError: If the radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    else:
        return 3.14159 * radius ** 2


# Without Sphinx style
def calculate_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle

    Returns:
        float: The area of the circle

    Examples:
        >>> calculate_area(5)
            78.53975
        >>> calculate_area(4.2)
            55.4176476

    Raises:
        ValueError: If the radius is negative
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    else:
        return 3.14159 * radius ** 2


print(calculate_area(5))
print(calculate_area(4.2))
