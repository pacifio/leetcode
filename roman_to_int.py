class Solution:
    def romanToInt(self, s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        t = 0
        for i in range(1, len(s)):
            if (s[i-1] == 'I' and s[i] == 'V') or (s[i-1] == 'I' and s[i] == 'X'):
                t -= m[s[i-1]]
            elif (s[i-1] == 'X' and s[i] == 'L') or (s[i-1] == 'X' and s[i] == 'C'):
                t -= m[s[i-1]]
            elif (s[i-1] == 'C' and s[i] == 'D') or (s[i-1] == 'C' and s[i] == 'M'):
                t -= m[s[i-1]]
            else:
                t += m[s[i-1]]
        t += m[s[::-1][0]]

        return t


s = Solution()
print(s.romanToInt("MMMCDXC"))
