def array_split_gen(sequence, seperators=[0]):
    """ A generator that yields an array into sub-arrays.
        E.g. for _ in array_split_gen([2,3,4,5,0,6,7,0,8,9,10,0,11,12], [0]):
                print(_)

                [2, 3, 4, 5]
                [6, 7]    
                [8, 9, 10]
                [11, 12]

    Args:
        sequence:
            The array to be split up.
        seperators:
            An array of seperators to split on.

    Returns:
        A generator.
    """
    chunk = []

    for val in sequence:
        if val in seperators:
            yield chunk
            chunk = []
        else:
            chunk.append(val)

    yield chunk



for _ in array_split_gen(['h', 'e', 'l', 'l', 'o', '_', 'C', 'r', 'a', 'i', 'g'], ['_']):
    print(_)