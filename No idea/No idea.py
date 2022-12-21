# Enter your code here. Read input from STDIN. Print output to STDOUT
first_line= input()
list_n = input().split(' ')
set_a = set(input().split(' '))
set_b = set(input().split(' '))
happiness = 0

for num in list_n:
    if(num in set_a):
        happiness+=1
    elif(num in set_b):
        happiness-=1
print(happiness)
