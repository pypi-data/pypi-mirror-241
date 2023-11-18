from .constant import *

import random
import types

int_1e9_pos = lambda: random.randint(1, INT_1E9)
int_1e9_not_neg = lambda: random.randint(0, INT_1E9)
int_1e9 = lambda: random.randint(-INT_1E9, INT_1E9)
int_1e18_pos = lambda: random.randint(1, INT_1E18)
int_1e18_not_neg = lambda: random.randint(0, INT_1E18)
int_1e18 = lambda: random.randint(-INT_1E18, INT_1E18)
int_1bit = lambda: random.randint(0, 1)
int_32bit = lambda: random.randint(0, INT32_MAX)
int_64bit = lambda: random.randint(0, INT64_MAX)

char_lower = lambda: random.choice(ALPHABET_LOWER)
char_upper = lambda: random.choice(ALPHABET_UPPER)


def gen_string(n: int, char_set):
    """
    Generate a random string of a specified length using characters from a given character set.

    Parameters:
        - `n` (int): Length of the generated string.
        - `char_set`: Set of characters to choose from.

    Returns:
        - str: The generated random string.

    Examples:
        >>> gen_string(5, "abcde")
        'cadbe'
    """
    return "".join(random.choices(char_set, k=n))


def identity_permutation(n):
    """
    Generate the identity permutation of a specified length.

    Parameters:
        - `n` (int): Length of the permutation.

    Returns:
        - list: The identity permutation.

    Examples:
        >>> identity_permutation(3)
        [1, 2, 3]
    """
    return list(range(1, n + 1))


def gen_permutation(n: int):
    """
    Generate a random permutation of a specified length.

    Parameters:
        - `n` (int): Length of the permutation.

    Returns:
        - list: The generated random permutation.

    Examples:
        >>> gen_permutation(3)
        [2, 1, 3]
    """
    a = identity_permutation(n)
    random.shuffle(a)
    return a


def evaluate(f):
    """
    Evaluate a function, integer, string, or a range defined by a list or tuple.

    Parameters:
        - `f`: The function, value, or range to evaluate.

    If `f` is a single value (integer, string, or float), it is returned unchanged.

    If `f` is a list or tuple:
        - If the length is 1, a random integer in the range [0, f[0]] is returned.
        - If the length is 2, a random integer in the range [f[0], f[1]] is returned.
        - Otherwise, a ValueError is raised for unexpected length.

    If `f` is a function (callable object of type types.FunctionType), it is called, and the result is returned.

    Raises:
        - TypeError: If `f` is of an unexpected type.

    Returns:
        - The evaluated result.

    Examples:
        >>> evaluate(5)
        5
        >>> evaluate((1, 10))
        8
        >>> evaluate(lambda: random.choice(['a', 'b', 'c']))
        'b'
    """
    if isinstance(f, (list, tuple)):
        if len(f) == 1:
            return random.randint(0, f[0])
        elif len(f) == 2:
            return random.randint(f[0], f[1])
        else:
            raise ValueError("Unexpected length of f: {}".format(len(f)))
    elif isinstance(f, types.FunctionType):
        return f()
    elif isinstance(f, (int, str, float)):
        return f
    else:
        raise TypeError("Unexpected type: {}".format(type(f)))


def evaluate_list(f_list) -> list:
    """
    Evaluate a list of functions, integers, strings, or ranges.

    Parameters:
        - `f_list`: List or tuple of functions or values.

    Returns:
        - list: The list of evaluated results.

    Examples:
        >>> evaluate_list([1, (2, 5), lambda: random.choice(['a', 'b', 'c'])])
        [1, 3, 'c']
    """
    if isinstance(f_list, (list, tuple)):
        return [evaluate(f) for f in f_list]
    else:
        return [evaluate(f_list)]