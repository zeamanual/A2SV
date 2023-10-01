n = int(input())
arr = list(map(int,input().split()))

odd_count=0
even_count = 0

for num in arr:
    if(num%2==0):
        even_count+=1
    else:
        odd_count+=1
        
if(odd_count==n or even_count==n):
    print(*arr)
    
else:
    arr.sort()
    print(*arr)
