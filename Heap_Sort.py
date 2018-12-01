def newno(list, size, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < size and list[left] > list[largest]:
        largest = left
    if right < size and list[right] > list[largest]:
        largest = right
    if largest != i:
        list[i], list[largest] = list[largest], list[i]
        newno(list, size, largest)


def newheap(list,size):
    for i in range(int(size / 2), -1, -1):
        newno(list, size, i)


def heapsort(list):
    size = len(list)
    newheap(list,size)
    # print A #uncomment this print to see the heap it builds
    for i in range(size - 1, 0, -1):
        list[0], list[i] = list[i], list[0]
        size -= 1
        newno(list, size, 0)

    return list