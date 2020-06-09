class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        for i in s:

            index = t.find(i)

            if index >= 0:
                t=t[index+1:]

            else:
                return False
        return True
