n,m = list(map(int,input().split()))
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
 
 
ptr1=0
ptr2=0
 
sorted_arr=[]
while(ptr1<n and ptr2 <m):
    if(nums1[ptr1]>nums2[ptr2]):
        sorted_arr.append(nums2[ptr2])
        ptr2+=1
    else:
        sorted_arr.append(nums1[ptr1])
        ptr1+=1
 
while(ptr1<n):
    sorted_arr.append(nums1[ptr1])
    ptr1+=1
 
while(ptr2<m):
    sorted_arr.append(nums2[ptr2])
    ptr2+=1
 
print(*sorted_arr)
