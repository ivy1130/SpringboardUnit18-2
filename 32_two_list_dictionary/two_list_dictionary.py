def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """

    if len(keys) == len(values):
        return {keys[i]: values[i] for i in range(len(keys))}
    elif len(keys) > len(values):
        res = dict()
        for i in range(len(values)):
            res[keys[i]] = values[i]
        for i in (range(len(keys) - len(values))):
            res[keys[i + len(values)]] = None
        return res
    else:
        return {keys[i]: values[i] for i in range(len(keys))}


    # Solution below, but doesn't work for the use case of fewer keys, because it will add an additional key of None
    # from itertools import zip_longest
    # return dict(zip_longest(keys, values))
