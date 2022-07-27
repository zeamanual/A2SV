#User function Template for python3

class Solution: 
    def select(self, arr, i):
        smallest = i
        size = len(arr)
        for index in range(i,size):
            if(arr[index] < arr[smallest]):
                smallest=index
        
        return smallest
    
    def selectionSort(self, arr,n):
        for index in range(n):
            selected_index = self.select(arr,index)
            arr[index],arr[selected_index] = arr[selected_index],arr[index]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
