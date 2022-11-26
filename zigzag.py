
storage = []
bools = []

def zigzag(list):
    end = list[-1]
    
    
    for i in range(len(list)):
        temp_list = []

        for j in range(i, i+3):
            temp_list.append(list[j])
            
        storage.append(temp_list)
        
        if end == storage[-1][-1]:
            for i in range(len(storage)):
                if storage[i][0]>storage[i][1]<storage[i][2]:
                    bools.append(True)
                else:
                    bools.append(False)
        
            return bools

if zigzag([1,2,3,4,5]) != None:
    print(bools)