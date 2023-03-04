class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ##########
        # First solution , not good one ####
        # str1 = ""
        # str2 = ""
        # cnt1 = 0
        # cnt2 = 0
        # if len(s) == len(t):
        #     for el in s:
        #         if el not in str1:
        #             str1 += el 
        #             cnt1 += 1
        #     for el in t :
        #         if el not in str2:
        #             str2 += el
        #             cnt2 += 1
        # else:
        #     return False
        # if cnt1 == cnt2:
        #     return True
        # else:
        #     return False  
        # 
        #######
        # Good one #### 
        mydict = {}

        for i , v in enumerate(s):
            if v not in mydict:
                if t[i] not in mydict.values():
                    mydict[v] = t[i]
                else:
                    return False
            else:
                if mydict[v] != t[i]:
                    return False
        return True


s = "bbbaaaba"
t = "aaabbbba"

g = Solution()
print(g.isIsomorphic(s,t))