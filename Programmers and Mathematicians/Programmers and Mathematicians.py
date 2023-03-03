import math
test_cases = int(input())

for count in range(test_cases):
    prg, mat = list(map(int,input().split()))
    max_possible = math.floor((prg+mat)/4)

    min_possible = 1
    max_combination = min(prg,mat)
    answer = 0
    while(max_possible>=min_possible):
        mid = min_possible+(max_possible-min_possible)//2
        if(mid<=max_combination):
            answer = max(answer,mid)
            min_possible=mid+1
        else:
            max_possible=mid-1

    print(answer)
