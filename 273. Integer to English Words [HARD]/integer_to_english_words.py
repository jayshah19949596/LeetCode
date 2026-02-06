"""
273. Integer to English Words [HARD]
https://leetcode.com/problems/integer-to-english-words

"""
class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        res = helper(num)
        return res


def helper(num):
    belowTen = {0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
                9: "Nine"}
    belowTwenty = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
                   17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}
    belowHundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    result = ""
    if (num < 10):
        result = belowTen[num]
    elif (num < 20):
        result = belowTwenty[num]
    elif (num < 100):
        result = belowHundred[num // 10] + " " + helper(num % 10)
    elif (num < 1_000):
        result = helper(num // 100) + " Hundred " + helper(num % 100)
    elif (num < 1_000_000):
        result = helper(num // 1_000) + " Thousand " + helper(num % 1000)
    elif (num < 1_000_000_000):
        result = helper(num // 1_000_000) + " Million " + helper(num % 1000000)
    else:
        result = helper(num // 1_000_000_000) + " Billion " + helper(num % 1000000000)
    return result.strip()



from collections import deque


class Solution1:
    def numberToWords(self, num: int) -> str:

        int_to_word = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
                       6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
                       11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
                       15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
                       19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
                       50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}

        digits_to_word = {3: 'Thousand', 6: 'Million', 9: 'Billion', 12: 'Trillion',
                          15: 'Quadrillion', 18: 'Quintillion', 21: 'Sextillion', 24: 'Septillion',
                          27: 'Octillion', 30: 'Nonillion'}

        english = deque()
        digits = 0
        if num == 0: return "Zero"

        while num:
            num, section = divmod(num, 1000)
            hundreds, tens = divmod(section, 100)  # 567

            if section and digits > 0:
                english.appendleft(digits_to_word[digits])

            digits += 3

            if tens >= 20:
                if tens % 10: english.appendleft(int_to_word[tens % 10])
                english.appendleft(int_to_word[10 * (tens // 10)])
            elif tens > 0:
                english.appendleft(int_to_word[tens])

            if hundreds > 0:
                english.appendleft("Hundred")
                english.appendleft(int_to_word[hundreds])

        return " ".join(english)
