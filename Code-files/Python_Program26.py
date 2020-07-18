def isPalRec(st, s, e) : 
    if len(st) == 0:
        return True
    if (s == e): 
        return True  
    if (st[s] != st[e]) : 
        return False  
    if (s < e + 1) : 
        return isPalRec(st, s + 1, e - 1); 
    return True  
strng1 = "rac"
strng2 = "racecar"
print(isPalRec(strng1, 0, len(strng1) -1))
print(isPalRec(strng2, 0, len(strng2) -1))