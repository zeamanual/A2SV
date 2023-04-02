class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        my_set = set()
        for num in nums:
            self.get_prime_factors(num,my_set)

        return len(my_set)

    

    def get_prime_factors(self,num,my_set):

        start = 2

        while(start * start <= num):
            while(num%start==0):
                my_set.add(start)
                num=num/start
            start+=1

        if(num>1):
            my_set.add(num)
