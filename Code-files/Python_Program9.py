def bubbleSort(list1): 
    n = len(list1) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if list1[j] > list1[j+1] : 
                list1[j], list1[j+1] = list1[j+1], list1[j] 
    return list1
print(bubbleSort([2, 6, 2, 4, 6, 1, 7, 7, 2, 3, 9]))