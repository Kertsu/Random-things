def tiny(list_1, list_2, limit):
    global bools
    storage = []
    bools = []
    length = len(list_1)
    
    for i in range(length):
        storage.append(str(list_1[i]) + str(list_2[(length-1)-i]))
    
    for i in range(length):
        if limit < int(storage[i]):
            bools.append(False)
        else:
            bools.append(True)
    return bools
    
if tiny([1,2,3,4,5], [6,7,8,9,10], 100) != None:
    print(bools)