class Solution:
    def interpret(self, command: str) -> str:
        current_ptr=0
        interpreated=''
        command_len = len(command)
        while(current_ptr<command_len):
            if(command[current_ptr]=='G'):
                interpreated+='G'
                current_ptr+=1
            elif(command[current_ptr]=='(' and command[current_ptr+1]==')'):
                interpreated+='o'
                current_ptr+=2
            else:
                interpreated+='al'
                current_ptr+=4
        return interpreated
