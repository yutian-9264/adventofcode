with open('2024/2/1.txt') as f:
    
    
    result_list = []

    for line in f:
        list1 = []
        list2 = []
        result_temp = 0
        temp = line.split()
        list1.append(temp)
        print(list1[0])

        for i in range(len(list1)-1):
            # if list1[i+1] == list[i]:
            #     break

            list2.append(list1[i+1] - list1(i))    

        for i in list2:
            if all(i > 0 and i < 4):
                result_temp = 1
            if all(i > -4 and i < 0):
                result_temp = 1
        result_list.append(result_temp)

print(result_list.count(1))




