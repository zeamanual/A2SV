class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        if(self.is_valid_ipv4(queryIP)):
            return 'IPv4'
        elif(self.is_valid_ipv6(queryIP)):
            return 'IPv6'
        else:
            return 'Neither'

    def is_valid_ipv4(self,queryIP):
        def ipv4_element(string):
            leading_zeros =0
            index=0

            # counting leading zeros
            while(index<len(string) and string[index]=="0" ):
                leading_zeros+=1
                index+=1
            return (leading_zeros<1 or len(string)==1) and string.isdigit() and 0<= int(string)<=255

        ipv4_parts = queryIP.split('.')

        for index in range(len(ipv4_parts)):
            if(not ipv4_element(ipv4_parts[index])):
                return False

        return len(ipv4_parts)==4


    def is_valid_ipv6(self,queryIP):

        def ipv6_element(string):

            # checking letters 
            for char in string:
                if(char.isalpha() and not (65 <= ord(char)<=70 or 97<=ord(char)<=102)):
                    return False

            return string.isalnum() and len(string)<=4

        ipv6_parts = queryIP.split(':')

        for index in range(len(ipv6_parts)):

            if(  not ipv6_element(ipv6_parts[index])):
                return False

        return len(ipv6_parts)==8
