"""
============================================
Approach-1: Sorting with Sliding Window 
============================================
We first parse and sort transactions by time in O(n log n).
Then we process them using a sliding 60-minute window maintained by a deque.
Each transaction is compared with other transactions in the current window to check the city rule.
In the worst case, the window can contain O(n) transactions, leading to O(n²) total comparisons.
"""
from collections import deque
from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        parsed_transactions = []

        for index, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            parsed_transactions.append((name, int(time), int(amount), city, index))

        parsed_transactions.sort(key=lambda transaction: transaction[1])

        invalid_indices = set()
        sixty_minute_window = deque()

        for cur_trans in parsed_transactions:
            cur_name, cur_time, cur_amnt, cur_city, cur_idx = cur_trans

            while sixty_minute_window and sixty_minute_window[0][1] < cur_time - 60:
                sixty_minute_window.popleft()

            if cur_amnt > 1000:
                invalid_indices.add(cur_idx)

            for prv_trans in sixty_minute_window:
                prv_name, prv_time, prv_amnt, prv_city, prv_idx = prv_trans

                if prv_name == cur_name and prv_city != cur_city:
                    invalid_indices.add(prv_idx)
                    invalid_indices.add(cur_idx)

            sixty_minute_window.append(cur_trans)

        return [transactions[index] for index in invalid_indices]


"""
============================================
Approach-2: Grouping by name
============================================
I first parse each transaction into structured fields: name, time, amount, and city, 
and I also keep the original index so I can return duplicates correctly and preserve input order.
Then I group transactions by name, because the invalid-city rule only applies between transactions from the same person.
"""

from collections import defaultdict
from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        transactions_by_name = defaultdict(list)
        invalid_indices = set()

        # Parse transactions and group by name
        for index, transaction in enumerate(transactions):
            name, time, amount, city = transaction.split(",")
            time = int(time)
            amount = int(amount)

            transactions_by_name[name].append((time, amount, city, index))

            if amount > 1000:
                invalid_indices.add(index)

        # Check conflicting transactions for each person
        for name in transactions_by_name:
            person_transactions = transactions_by_name[name]
            person_transactions.sort(key=lambda transaction: transaction[0])

            n = len(person_transactions)

            for i in range(n):
                time_i, amount_i, city_i, index_i = person_transactions[i]

                for j in range(i + 1, n):
                    time_j, amount_j, city_j, index_j = person_transactions[j]

                    if time_j - time_i > 60:
                        break

                    if city_i != city_j:
                        invalid_indices.add(index_i)
                        invalid_indices.add(index_j)

        # Return invalid transactions in original input order
        result = []
        for index, transaction in enumerate(transactions):
            if index in invalid_indices:
                result.append(transaction)

        return result
