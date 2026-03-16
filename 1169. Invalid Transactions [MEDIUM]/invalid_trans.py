"""
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
