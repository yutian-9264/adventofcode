import numbers 

with open('2024/3/1.txt') as f:
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    all_txt = ''
    result = 0

    for line in f:
        all_txt = all_txt + line
        
    # print(all_txt)

    # print(all_txt.find('mul', 29))
    # print(all_txt.find('mul'))
    idx = 0
    # print(all_txt.find('mul', idx))
    while(all_txt.find('mul', idx+1)):
        

        # print(idx)
        # if(idx == all_txt.find('mul', idx+1)):
        #     break
        idx = all_txt.find('mul', idx+1)
        if idx == -1:
            break
        list1.append(idx)
        
    
    print(isinstance('343[<^mul(622', numbers.Number))
    print(len(list1))

    for i in range(len(list1)):
        tmp1 = all_txt.find(',', i)
        print(all_txt[list1[i]+4:tmp1])
        if(isinstance(all_txt[list1[i]+4:tmp1], numbers.Number)):
            list2.append(tmp1)
        else:
            list4.append(i)
            # del list1[i]
        # if(isinstance(all_txt[list2[i]+1:list3[i]], numbers.Number)):
        #     list3.append(all_txt.find(')', i))
        # else:
        #     del list1[i]
        #     del list2[i]
    
    # print(len(list1),len(list2),len(list3))
    # for i in range(len(list1)):
    #     print('test')
    #     print(all_txt[list1[i]+4:list2[i]])
    #     print(all_txt[list2[i]+1:list3[i]])
    #     result = result + int(all_txt[list1[i]+4:list2[i]]) * int(all_txt[list2[i]+1:list3[i]])

    # print(result)
    

    # print(all_txt[list1[0]+4:list2[0]])
    # print(all_txt[list2[0]+1:list3[0]])

        




    # # print('i')
        
        # next_idx = line.find('mul')
        # list1.append()