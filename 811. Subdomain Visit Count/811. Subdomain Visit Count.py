
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_dic = {}

        for cpdomain in cpdomains:

            current_inputs=cpdomain.split(' ')
            current_count = int(current_inputs[0])
            sub_doman_list=current_inputs[1].split('.')
            num_of_sub_doman=len(sub_doman_list)

            for i in range(num_of_sub_doman):
                domain_dic['.'.join(sub_doman_list[i:])]= domain_dic.get('.'.join(sub_doman_list[i:]),0)+current_count
            
        answer = []

        for domain in domain_dic.keys():
            answer.append(f'{domain_dic[domain]} {domain}')        
        return answer
