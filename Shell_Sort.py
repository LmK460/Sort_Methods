def shellSort(v):
    key = int(len(v)/2)
    while( key> 0):
        for i in range(key,len(v)):
            aux= v[i]
            j=i
            while(j>=key and v[j-key]>aux):
                v[j] = v[j-key]
                j-=key
            v[j]=aux
        key = int(key/2)
    return v