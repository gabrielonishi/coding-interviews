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
