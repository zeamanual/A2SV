import math
test_cases_count = int(input())
size_dic={
    'X':1,
    'S':100000,
    'M':200000,
    'L':300000
}

for i in range(test_cases_count):

    sizes = input().split(' ')
    final_result=[]
    for i in range(2):
        current=0
        for size_chr in sizes[i]:
            current+=size_dic[size_chr]
            if(size_chr=='S'):
                current=current-(2*current%100000)
        final_result.append(current)
    if(final_result[0]>final_result[1]):
        print('>')
    elif(final_result[0]<final_result[1]):
        print('<')
    else:
        print('=')
