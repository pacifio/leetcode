class Solution:
    def reverse(self, x: int) -> int:
        r = -int((str(x).split('-'))[1][::-1]
                 ) if '-' in str(x) else int(str(x)[::-1])
        return 0 if r > pow(2, 31) or r < -(pow(2, 31) - 1) else r
