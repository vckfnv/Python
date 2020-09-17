def mergeSort(a):
    if len(a) <=1:
        return a

    #반틈씩 계속 나누기
    part1 = mergeSort(a[:len(a)//2])
    part2 = mergeSort(a[len(a)//2:])
    
    i=0
    j=0
    k=0

    while i<len(part1) and j<len(part2):
        if part1[i] < part2[j]:
            a[k] = part1[i]
            i+=1
        else:
            a[k]=part2[j]
            j+=1
        k+=1

    if i==len(part1):
        while j<len(part2):
            a[k]=part2[j]
            j+=1
            k+=1
    elif j==len(part2):
        while i<len(part1):
            a[k]=part1[i]
            i+=1
            k+=1
    return a


toMergeList=[69, 10, 30, 2, 16, 8, 31]
print(mergeSort(toMergeList))
