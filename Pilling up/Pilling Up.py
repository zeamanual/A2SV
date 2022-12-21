# Enter your code here. Read input from STDIN. Print output to STDOUT
tests = int(input())
for i in range(tests):
    cubes_len = int(input())
    cubes = list(map(int,input().split()))
    leftPtr =0
    rightPtr = cubes_len-1
    last_base=None
    pilled=True
    while(leftPtr<=rightPtr):
        largest = None
        if(cubes[leftPtr]>=cubes[rightPtr]):
            largest=cubes[leftPtr]
            leftPtr+=1
        else:
            largest=cubes[rightPtr]
            rightPtr-=1   
        if(last_base==None or last_base>=largest):
            last_base=largest
        else:
            pilled=False 
            break
    if(pilled):
        print('Yes')
    else:
        print('No')
          
    
