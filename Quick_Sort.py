def quickSort(list):
    if len(list) <= 1:
        return l

    pivot = randint(0, len(list))
    pivot = list[pivot]
    print("Pivot", pivot)
    key = [i for i in list if i == pivot]
    print(key)
    left = [i for i in list if i < pivot]
    print(left)
    right = [i for i in list if i > pivot]
    print(right)

    return left + key + right