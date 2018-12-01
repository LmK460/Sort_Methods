def selectionSort(list):
    #print("Ordenando")
    for i in range(len(list)):
        menor = i
        for j in range(i+1,len(list)):
            if((list[j] < list[menor])):
                menor = j
        list[i], list[menor] = list[menor],list[i]
    return list
