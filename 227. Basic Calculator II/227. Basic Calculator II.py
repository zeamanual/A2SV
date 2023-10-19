class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        opps = ['+','-','/','*']
        advanced = ['*','/']
        index = 0
        while(index<len(s)):
            if(s[index].isdigit()):

                curr_num = ''
                while(index<len(s) and s[index].isdigit()):
                    curr_num+=s[index]
                    index+=1
                stack.append(int(curr_num))
                if(len(stack)>2 and stack[-2] in advanced):
                    one,op,two= stack.pop(),stack.pop(),stack.pop()
                    if(op=='*'):
                        stack.append(one*two)
                    else:
                        stack.append(two//one)

            elif(s[index] in opps):
                stack.append(s[index])
                index+=1

            else:
                index+=1

        return self.evaluate(stack)
        
    def evaluate(self,s):
        stack =[]
        index=0
        while(index<len(s)):
            if(isinstance(s[index],int)):
                stack.append(s[index])
                index+=1
            else:
                one = stack.pop()
                two = s[index+1]
                if(s[index]=='+'):
                    stack.append(one+two)
                else:
                    stack.append(one-two)
                index+=2

        return stack[0]
