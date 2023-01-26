n,k = list(map(int,input().split()))

arr = list(map(int,input().split()))
arr.sort()

if(k==0):
    print(f'{ arr[0]-1 if(arr[0]-1>0) else -1}')
elif(k==len(arr)):
    print(arr[len(arr)-1])
elif( k>=len(arr) or arr[k]==arr[k-1]):
    print('-1')
else:
    print(arr[k-1])
