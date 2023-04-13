class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.answer = []
        self.backtracking(s,0,[])
        print(self.answer)
        return self.answer

    def backtracking(self,s,index,curr):
        
        if(len(curr)==4 and index == len(s)):
            if(self.is_valid(curr)):
                self.answer.append('.'.join(curr))
            return
        elif(len(curr)==4):
            return

        for i in range(index,len(s)):
            curr.append(s[index:i+1])
            self.backtracking(s,i+1,curr)
            curr.pop()
            
    def is_valid(self,nums):
        for num in nums:
            if(len(num)>1 and num[0]=='0'):
                return False
            if(int(num) < 0 or int(num) > 255):
                return False
        return True
