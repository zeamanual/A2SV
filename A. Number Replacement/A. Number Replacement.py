test_cases_count=int(input())

for i in range(test_cases_count):
    test_case_size=int(input())
    array=input().split(' ')
    converted=input()

    char_dic = {}
    is_valid=True
    for index in range(test_case_size):
        if(array[index] in char_dic):
            if(char_dic[array[index]]!=converted[index]):
                is_valid=False
                break
        else:
            char_dic[array[index]]=converted[index]
        
    if(is_valid):
        print("YES")
    else:
        print('NO')
    

