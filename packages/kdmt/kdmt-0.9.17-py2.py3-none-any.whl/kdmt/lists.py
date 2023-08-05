import functools
import operator
import collections
from six import string_types
import numpy as np




"""List-related functions"""


def unlist(list_thing, complain=True):
    """transforms [Something] -> Something. By default, raises a ValueError for
    any other list values."""
    if complain and len(list_thing) > 1:
        raise ValueError("More than one element in {}".format(list_thing))
    elif len(list_thing) == 1:
        return list_thing[0]

    if complain:
        raise ValueError("Nothing in {}".format(list_thing))
    return None


def flat_map(iterable, func):
    """func must take an item and return an interable that contains that
    item. this is flatmap in the classic mode"""
    results = []
    for element in iterable:
        result = func(element)
        if len(result) > 0:
            results.extend(result)
    return results


def get_shape(l):
    d = 0
    while isinstance(l, list):
        d += 1
        l = l[0]
    return d


def flatten(l):
    while get_shape(l) >= 2:
        l = functools.reduce(operator.iconcat, l, [])
    return l


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def get_dimensions(X):
    """ Return the dimensions from a numpy.array, numpy.ndarray or list.

    Parameters
    ----------
    X: numpy.array, numpy.ndarray, list, list of lists.

    Returns
    -------
    tuple
        A tuple representing the X structure's dimensions.
    """
    r, c = 1, 1
    if isinstance(X, type(np.array([0]))):
        if X.ndim > 1:
            r, c = X.shape
        else:
            r, c = 1, X.size

    elif isinstance(X, type([])):
        if isinstance(X[0], type([])):
            r, c = len(X), len(X[0])
        else:
            c = len(X)

    return r, c


def isiter(obj):
    try:
        iter(obj)
    except TypeError:
        return False
    else:
        return True


def can_iterate(obj):
    is_string = isinstance(obj, string_types)
    is_iterable = isinstance(obj, collections.Iterable)

    return is_iterable and not is_string

def is_column_vector(x):
    return len(x.shape) == 2 and x.shape[1] == 1


def is_row_vector(x):
    return len(x.shape) == 1
