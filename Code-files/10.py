def binary_search(list1, low, high, x): 
    high = len(list1)-1
    if high >= low: 
        mid = (high + low) // 2
        if list1[mid] == x: 
            return mid 
        elif list1[mid] > x: 
            return binary_search(list1, low, mid - 1, x) 
        else: 
            return binary_search(list1, mid + 1, high, x) 
    else: 
        return -1
print(binary_search([0, 2, 4, 5, 2, 4], 0, 0, 4))