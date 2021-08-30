class Solution:
    def longestCommonPrefix(self, strs) -> str:
        x = [set(i) for i in strs]
        r = ''.join([x[i-1].intersection(x[i])
                     for i in range(1, len(x))][-1])[::-1]
        c = False
        if len(r) > 0:
            for i in strs:
                if i.startswith(r):
                    c = True
                else:
                    c = False
            if c:
                return r
            else:
                return r[::-1]
        else:
            return ''


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
