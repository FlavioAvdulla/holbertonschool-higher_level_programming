#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Returns the length of a string and its first character.

    Args:
        sentence (str): The input string.

    Returns:
        tuple: A tuple containing the length of the string and its first character. If the string is empty, returns (0, None).

    Example:
        >>> multiple_returns("Hello")
        (5, 'H')
        >>> multiple_returns("")
        (0, None)
    """
    if sentence:
        return (len(sentence), sentence[0])
    else:
        return (0, None)
