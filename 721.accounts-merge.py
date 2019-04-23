#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#
# https://leetcode.com/problems/accounts-merge/description/
#
# algorithms
# Medium (39.58%)
# Total Accepted:    30.5K
# Total Submissions: 76.8K
# Testcase Example:  '[["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]'
#
# Given a list accounts, each element accounts[i] is a list of strings, where
# the first element accounts[i][0] is a name, and the rest of the elements are
# emails representing emails of the account.
# 
# Now, we would like to merge these accounts.  Two accounts definitely belong
# to the same person if there is some email that is common to both accounts.
# Note that even if two accounts have the same name, they may belong to
# different people as people could have the same name.  A person can have any
# number of accounts initially, but all of their accounts definitely have the
# same name.
# 
# After merging the accounts, return the accounts in the following format: the
# first element of each account is the name, and the rest of the elements are
# emails in sorted order.  The accounts themselves can be returned in any
# order.
# 
# Example 1:
# 
# Input: 
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John",
"johnnybravo@mail.com"], ["John", "johnsmith@mail.com",
"john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com',
# 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary",
# "mary@mail.com"]]
# Explanation: 
# The first and third John's are the same person as they have the common email
# "johnsmith@mail.com".
# The second John and Mary are different people as none of their email
# addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary',
# 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']]
# would still be accepted.
# 
# 
# 
# Note:
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].
# 
#
class Solution:
    def accountsMerge(self, accounts):
        uf = UnionFindSet(len(accounts))

        # map ids to email
        email_dict = {}     # {email: id list}
        for id, emails in enumerate(accounts):
            for email in emails[1:]:    # skip the first one (name)
                if email not in email_dict: email_dict[email] = []
                email_dict[email].append(id)
        
        for id_list in email_dict.values():
            root_id = id_list[0]
            child_id_list = id_list[1:]
            for id in child_id_list:
                uf.union(id, root_id)

        # map emails to id
        id_dict = {}
        for id, emails in enumerate(accounts):
            root = uf.find(id)
            if root not in id_dict: id_dict[root] = set()
            
            for email in emails[1:]:
                id_dict[root].add(email)

        # add to result list:
        res = []
        for id, emails in id_dict.items():
            name = accounts[id][0]
            email_ls = sorted(emails)
            res.append([name] + email_ls)
        return res

class UnionFindSet:
    def __init__(self, n):
        self.father = {i: i for i in range(n)}

    def find(self, node):
        path = []
        while self.father[node] != node:
            path.append(node)
            node = self.father[node]

        for p in path:
            self.father[p] = node

        return node
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        self.father[root_a] = root_b

# s = Solution()
# s.accountsMerge(accounts)