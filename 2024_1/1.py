with open('2024_1/1.txt') as f:
    
    list3 = []
    list1 = []
    list2 = []

    for line in f:
        temp = line.split()
        list1.append(int(temp[0]))
        list2.append(int(temp[1]))

    for i in range(len(list1)):
        list3.append(abs(min(list1)-min(list2)))
        list1.remove(min(list1))
        list2.remove(min(list2))
    print(sum(list3))
        