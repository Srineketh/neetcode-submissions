class Solution:

    def alphanum(self,s):
        return (ord('A') <= ord(s) <= ord('Z') or
                ord('a') <= ord(s) <= ord('z') or
                ord('0') <= ord(s) <= ord('9'))

    def isPalindrome(self, s: str) -> bool:
        processed = ""
        for i in s:
            if self.alphanum(i):
                processed += i
        processed = processed.lower()
        i = 0
        j = len(processed) // 2 if len(processed) % 2 == 0 else (len(processed) // 2 ) + 1

        print(len(processed))
        for i in range(j):
            if processed[i] != processed[-(i+1)]:
                return False
        return True