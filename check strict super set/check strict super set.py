# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(input().split(' '))
n = int(input())
is_superset=True
for i in range(n):
    new_a = a.copy()
    child_set = set(input().split(' '))
    for ele in child_set:
        if(ele in new_a):
            new_a.discard(ele)
        else:
            is_superset=False
            break
        
    if(len(new_a)<1):
        is_superset=False
        break
    
if(is_superset):
    print('True')
else:
    print('False')
    
