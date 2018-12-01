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