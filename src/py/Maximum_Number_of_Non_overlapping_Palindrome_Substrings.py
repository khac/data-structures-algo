# 2472. Maximum Number of Non-overlapping Palindrome Substrings
# https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        if k==1: return len(s)
        palindromes = []
        def checkPalindromeLength(l,r):
            while l>=0 and r<len(s) and s[l] == s[r] and r-l+1<=k+1:
                l -= 1
                r += 1
            return (l+1,r-1)
        for i in range(k//2-1,len(s)):
            o = checkPalindromeLength(i,i)
            e = checkPalindromeLength(i,i+1)
            if o[1]-o[0]+1 >= k:
                palindromes.append((o[0], o[1]))
            if e[1]-e[0]+1 >= k:
                palindromes.append((e[0], e[1]))
        palindromes.sort(key=lambda x:(x[0], x[1]))
        n = len(palindromes)
        # print(n,palindromes)


        # return n
        def minIntervalToRmNonOverlappingIntervals(palindromes):
            interval = []
            count = 0
            for i in palindromes:
                if not interval or interval[1] < i[0]:
                    interval = list(i)
                else:
                    count += 1
                    interval[1] = min(interval[1],i[1])
                # print(interval)
            return count

        minPalindromeToRemove = minIntervalToRmNonOverlappingIntervals(palindromes)

        return n - minPalindromeToRemove
