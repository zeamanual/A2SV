class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        change = {5:0, 10:0}
        for i in range(len(bills)):
            cur = bills[i]
            if cur == 5: 
                change[5] += 1
            elif cur == 10:
                if change[5]:
                    change[5] -= 1
                    change[10] += 1
                else: return False
            else:
                if change[10]  and change[5]:
                    change[10] -= 1
                    change[5]-=1
                elif change[5]>=3: 
                    change[5] -= 3
                else: return False

        return True
