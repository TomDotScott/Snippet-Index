def bubble_sort(collection: list) -> list:
    """Pure implementation of the bubble sort algorithm
    :type collection: list
    :param collection: some mutable ordered collection with comparable
    items inside
    :return: the same collection ordered by ascending
    Examples:
    >>> bubble_sort([0, 5, 2, 3, 2])
    [0, 2, 2, 3, 5]
    >>> bubble_sort([])
    []
    >>> bubble_sort([-2, -45, -5])
    [-45, -5, -2]
    >>> bubble_sort([-23, 0, 6, -4, 34])
    [-23, -4, 0, 6, 34]
    >>> bubble_sort([-23, 0, 6, -4, 34]) == sorted([-23, 0, 6, -4, 34])
    True
    """
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection

