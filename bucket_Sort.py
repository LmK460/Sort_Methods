def bucketSort(list):
    tam = len(list)
    b = [[] for i in range(tam)]
       
    for i in range(tam):
        b[int(tam*list[i])].append(list[i])   
    for i in b:
        mergeSort(i)
    
    res=[]   
    for i in range(len(b)):
        while len(b[i]) > 0:
            res.append(b[i].pop(0))

    return res

def mergeSort(list):
    if len(list)<=1:
        return list
    else:
        m=int(len(list)/2)
        left=list[:m]
        right = list[m:]
        return  merge(mergeSort(left),mergeSort(right))

def merge(left,right):
    final=[]

    while left or right:
        if len(left) and len(right):
            if(right[0]>left[0]):
                final.append(left.pop(0))
            else:
                final.append(right.pop(0))
        if len(left)<=0:
            if len(right):
                final.append(right.pop(0))
        if len(right)<=0:
            if len(left):
                final.append(left.pop(0))
    return final