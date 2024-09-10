#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples element-wise.

    Args:
        tuple_a (tuple): The first tuple, default is an empty tuple.
        tuple_b (tuple): The second tuple, default is an empty tuple.

    Returns:
        tuple: A tuple containing the element-wise sum of the input tuples. If a tuple has fewer than two elements, 0 is used as the default value for missing elements.

    Example:
        >>> add_tuple((1, 2), (3, 4))
        (4, 6)
        >>> add_tuple((1,), (3, 4))
        (4, 4)
        >>> add_tuple((1, 2), ())
        (1, 2)
    """
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
