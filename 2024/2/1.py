with open('2024/2/1.txt') as f:
    result_list = []

    for line in f:
        list1 = []
        list2 = []
        result_temp = 0
        list1 = line.split()

        for i in range(len(list1)-1):
            list2.append(int(list1[i+1]) - int(list1[i]))  

        if all(i > 0 and i < 4 for i in list2):
            result_temp = 1
        if all(i > -4 and i < 0 for i in list2):
            result_temp = 1
         
        result_list.append(result_temp)

print(result_list.count(1)) 




