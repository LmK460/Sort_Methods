def countingSort(list,base):
    tam = len(list)
    res = [0] * (tam)

    # initialize count array as 0
    aux = [0] * (10)

    for i in range(0, tam):
        aux[int((list[i] // base) % 10)] += 1

    for i in range(1, 9):
        aux[i+1] += aux[i]

    for i in reversed(list):
        res[aux[int((i // base) % 10)] - 1] = i
        aux[int((i // base) % 10)] -= 1


    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    for i in range(len(list)):
        list[i] = res[i]


def radixSort(list):
    n=max(list)
    base=1
    while(n/base)>0:
        countingSort(list,base)
        base*=10