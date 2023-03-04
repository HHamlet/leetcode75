class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 1
        nstr = ""
        if s == "":
            return True
        print("Lenght s ",len(s))
        if len(s) < len(t):
            for el in t:
                if len(s) >= i:
                    print("el ",el)
                    print("i ",i)
                    if s[i-1] == el:
                        nstr +=el
                        i +=1
            if s == nstr :
                return True
            else:
                return False
        return False

s = "b"
t = "abc"
g =Solution()
print(g.isSubsequence(s,t))
