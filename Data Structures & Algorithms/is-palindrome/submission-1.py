class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = list("".join(char for char in s.lower() if char.isalnum()))
        rev_s = list(reversed(new_s))

        answer = True
        i = 0
        for j in range(len(new_s)):
            if rev_s[j] != new_s[i]:
                answer = False
                break
            else:
                i += 1
        return answer

        
        