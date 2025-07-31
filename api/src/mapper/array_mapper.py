from numpy import ndarray


def ndarray_to_pgarray(_list: ndarray):
    return ('{' +
            ', '.join(list(map( str, list(_list) )))
            + '}')
