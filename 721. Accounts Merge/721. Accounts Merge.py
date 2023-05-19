class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        def get_rep(node):
            rep = stat[node]
            while(rep!=node):
                node = stat[rep]
                rep = stat[node]
            
            return rep

        def union(node1, node2):
            node1_rep = get_rep(node1)
            node2_rep = get_rep(node2)
            stat[node1_rep]=node2_rep
        
        email_to_name,email_to_id,id = {},{},0

        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                if email not in email_to_id:
                    email_to_name[email] = name
                    email_to_id[email] = id
                    id += 1
        
        stat = [i for i in range(id)]
        for account in accounts:
            emails = account[1:]
            for i in range(1, len(emails)):
                union(email_to_id[emails[i]], email_to_id[emails[i-1]])
        
        merged_accounts = {}
        for email in email_to_name:
            root = get_rep(email_to_id[email])
            if root in merged_accounts:
                merged_accounts[root].append(email)
            else:
                merged_accounts[root] = [email]
        
        result = []
        for root, emails in merged_accounts.items():
            result.append([email_to_name[emails[0]]] + sorted(emails))
        
        return result
