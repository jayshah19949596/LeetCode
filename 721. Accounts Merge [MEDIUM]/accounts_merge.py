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

Create mapping from email to list of accounts with that
email. For each account dfs to visit the accounts of its
emails recursively.
Time - O(n log n) where n is total number of emails.
Each email visited once, then list sorted.
Space - O(n)
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
