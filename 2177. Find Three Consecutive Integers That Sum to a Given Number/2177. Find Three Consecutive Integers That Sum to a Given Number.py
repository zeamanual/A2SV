class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        required_value=num/3
        if((required_value-math.floor(required_value))==0):
            required_value=int(required_value)
            return [required_value-1,required_value,required_value+1]
        else:
            return []
