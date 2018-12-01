def insertionSort(list):
    for i in range(1,len(list),1):
        menor = list[i]
        j=i-1
        while(j>=0 and list[j] > menor):
            list[j+1] = list[j]
            j-=1

        list[j+1]=menor
    return list