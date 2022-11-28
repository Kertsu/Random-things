def tiny(list_1, list_2, limit):
    length = len(list_1)
    answer = []
    for i in range(length):
         concatenations = str(list_1[i]) + str(list_2[(length-1)-i])
         
         if limit < int(concatenations):
             answer.append(False)
         else:
             answer.append(True)
    return answer
