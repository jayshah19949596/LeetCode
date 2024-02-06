class Solution:

    def countPalindromes(self, s: str) -> int:
        total_subseq = set([])

        def recurse(inter, l, r):
            nonlocal s
            if len(inter) >= 5:
                total_subseq.add(tuple(inter))
                return
            if l < 0 or r >= len(s): return

            if s[l] == s[r]:
                recurse([l] + inter + [r], l - 1, r + 1)
            recurse(inter[:], l - 1, r)
            recurse(inter[:], l, r + 1)

        for i in range(2, len(s) - 2):
            recurse([i], i - 1, i + 1)

        return len(total_subseq)