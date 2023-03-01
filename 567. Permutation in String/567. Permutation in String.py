class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s2)<len(s1)):
            return False

        window_size = len(s1)
        original={}
        curr_window={}
        for index in range(len(s1)):
            original[s1[index]]=original.get(s1[index],0)+1
            curr_window[s2[index]]=curr_window.get(s2[index],0)+1
    
        left_ptr=0
        right_ptr=window_size-1
        while(right_ptr<len(s2)):
            if(self.compare(original,curr_window)):
                return True

            curr_window[s2[left_ptr]]-=1
            left_ptr+=1
            right_ptr+=1
            if(right_ptr<len(s2)):
                curr_window[s2[right_ptr]]=curr_window.get(s2[right_ptr],0)+1

        return False

    def compare(self,dic1,dic2):

        for key in  dic1.keys():
            if( key not in dic2 or dic1[key]!=dic2[key]):
                return False

        return True
