class Solution:
    def longestPalindrome(self, s: str) -> int:
        htable = {}
        countlist = []
        odd = 0
        for el in s:
            if el not in htable:
                htable[el] =1
            else:
                htable[el] +=1
        for val in htable.values():
            countlist.append(val)
            if val % 2 !=0:
                odd +=1
        if odd !=0:
            return sum(countlist) - odd + 1
        else:
            return sum(countlist) - odd

s = "abccccdd"
g =Solution()
print(g.longestPalindrome(s))
