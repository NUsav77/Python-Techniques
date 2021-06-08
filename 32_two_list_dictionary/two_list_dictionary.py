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
    # Stores the number of keys
    dict_size = len(keys)

    # Blank dict for later
    dict_create = {}

    # Checks the number of keys vs number of values. If there are more keys than values, you add 'None" to the 'values'
    if len(keys) > len(values):
        while len(values) < len(keys):
            values.append(None)

    # For loop adds keys/values to the blank dict we created above
    for x in range(dict_size):
        dict_create[keys[x]] = values[x]
    return dict_create
