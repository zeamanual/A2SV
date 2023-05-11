from typing import List
import sys
sys.setrecursionlimit(1<<27)
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		cycle_detected = False
		def dfs(node,prev):
		    nonlocal clrs
		    nonlocal cycle_detected
		    clrs[node]=1
		    
		    
		    for nbr in adj[node]:
		        if(nbr!=prev and clrs[nbr]!=0):
		            cycle_detected=True
		            break
		        elif(clrs[nbr]==0):
                    dfs(nbr,node)
		clrs = [0 for i in range(len(adj))]
		for curr in range(len(adj)):
		    if(clrs[curr]==0):
		        dfs(curr,-1)
		        
		return 1 if cycle_detected else 0


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
