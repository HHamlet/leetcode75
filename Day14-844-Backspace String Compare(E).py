class Solution:
    def backspaceCompare(self, s: str, t: str):
        s1 = "" 
        t1 = ""
        for i in range(len(s)):
            if s[i] != "#":
                s1 += s[i]
            else:
                s1 = s1[:-1]
        for i in range(len(t)):
            if t[i] != "#":
                t1 += t[i]
            else:
                t1 = t1[:-1]
        print("s ",s1)
        print("t ",t1)
        return True if s1 == t1 else False

s ="a#c"
t ="b"

q=Solution()
print(q.backspaceCompare(s,t))



