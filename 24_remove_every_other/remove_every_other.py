def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """

    other_items = []

    for count, items in enumerate(lst):
        if (count + 1) % 2 == 0:
            continue
        else:
            other_items.append(items)
    return other_items