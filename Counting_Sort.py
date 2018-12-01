def countingSort(list):
    res = [0] * len(list)
    low = min(list)
    high = max(list)+1
    aux= [0 for i in range(low, high)]

    for i in list:
        aux[i-low]+=1

    for i in range(len(aux)-1):
        aux[i+1]+=aux[i]

    for i in reversed(list):
        res[aux[i - low] - 1] = i
        aux[i - low] -= 1
    return res