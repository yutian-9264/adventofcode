with open('2024/1/1.txt') as f:
    
    list3 = []
    list1 = []
    list2 = []

    for line in f:
        temp = line.split()
        list1.append(int(temp[0]))
        list2.append(int(temp[1]))

    for i in range(len(list1)):
        list3.append(list1[i]*list2.count(list1[i]))
        # list1.remove(min(list1))
        # list2.remove(min(list2))
    print(sum(list3))
        