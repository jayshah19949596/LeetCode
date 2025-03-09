"""
https://leetcode.com/problems/accounts-merge/
Given a list accounts, each element accounts[i] is a list
of strings, where the first element accounts[i][0] is a
name, and the rest of the elements are emails
representing emails of the account.
Now, we would like to merge these accounts. Two accounts definitely
belong to the same person if there is some email
that is common to both accounts. Note that even if two accounts
have the same name, they may belong to different
people as people could have the same name. A person can
have any number of accounts initially, but all of their
accounts definitely have the same name.
After merging the accounts, return the accounts in the following
format: the first element of each account is the
name, and the rest of the elements are emails in sorted order.
The accounts themselves can be returned in any order.
"""

"""
=====================================
Approach-1: Graph based DFS solution 
=====================================
Create mapping from email to list of accounts with that
email. For each account dfs to visit the accounts of its
emails recursively.

--------------------------------------
### Complexity Analysis:
--------------------------------------
Time complexity: O(NKlogNK)
Space complexity: O(NK)
Here N is the number of accounts and K is the maximum length of an account.
"""

from collections import defaultdict

class Solution(object):
    def accountsMerge(self, accounts):
        email_accountid_graph = defaultdict(list)        # email to list of account indices containing that email

        for account_id in range(len(accounts)):
            account = accounts[account_id]
            for j in range(1, len(account)):
                email = account[j]
                email_accountid_graph[email].append(account_id)

        result, visited = [], set([])

        def dfs(cur_account_id):
            emails = set()
            if cur_account_id in visited: return emails
            visited.add(cur_account_id)
            cur_account = accounts[cur_account_id]
            for k in range(1, len(cur_account)):
                email = cur_account[k]
                emails.add(email)
                for neighbor_account_id in email_accountid_graph[email]:
                    emails |= dfs(neighbor_account_id)          # union existing and new emails
            return emails

        for account_id in range(len(accounts)):
            all_emails = dfs(account_id)
            if all_emails:
                account = accounts[account_id]
                result.append([account[0]] + sorted(list(all_emails)))

        return result


"""
=====================================
Approach-2: Union Find
=====================================

--------------------------------------
### Complexity Analysis:
--------------------------------------
Time complexity: O(NKlogNK)
Space complexity: O(NK)
Here N is the number of accounts and K is the maximum length of an account.

"""
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n # this is to identify how many children does each indexed parent has

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, n1, n2):
        parent1, parent2 = self.find(n1), self.find(n2)

        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # utilize multiple techniques here
        # lets say that we have something looks like this as originals:
        # accounts = [
        #     ["John","johnsmith@mail.com","john_newyork@mail.com"],
        #     ["John","johnsmith@mail.com","john00@mail.com"],
        #     ["Mary","mary@mail.com"],
        #     ["John","johnnybravo@mail.com"]
        # ]

        # for every account records, we need to check whether if the groups of emails have overlapping or not.
        # if they have overlapping, we need to combine them. if not, they are "two different" person with a same name
        # in this case, I am going to utilize a one data structure called unionFind, technique used for the graph
        # data structures
        uf = UnionFind(len(accounts))
        email_to_acc_idx = {}

        for idx, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_acc_idx:
                    uf.union(idx, email_to_acc_idx[email])
                else:
                    email_to_acc_idx[email] = idx
        
        # then we will have something like:
        # email_to_acc_idx = {
        #     'email1': '0',
        #     'email3': '2',
        #     'email4': '3',
        #     'email5': '4'
        # Lets say that there is an email 6 with account index 5, but this email has overlapping with account 0. this will get unionized in uf object
        # }

        email_to_group = collections.defaultdict(list)

        for email, account_idx in email_to_acc_idx.items():
            parent_account = uf.find(account_idx)
            email_to_group[parent_account].append(email)

        # then things get easier from here. we just need to assign names for each account grouped

        res = []

        for account_idx, emails in email_to_group.items():
            person_name = accounts[account_idx][0]
            res.append( [person_name] + sorted(emails) )
        
        return res
