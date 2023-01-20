size = int(input())
 
nums=list(map(int,input().split()))
zero=[]
less=[]
greater=[]
 
for num in nums:
    if(num<0):
        less.append(str(num))
    elif(num==0):
        zero.append(str(num))
    else:
        greater.append(str(num))
# print(less,zero,greater)
 
if len(less) % 2 == 0:
    zero.append(less.pop())
 
if len(less) > 2:
    greater.append(less.pop())
    greater.append(less.pop())
 
 
 
print(len(less),' '.join(less))
 
print(len(greater),' '.join(greater))
 
print(len(zero),' '.join(zero))
