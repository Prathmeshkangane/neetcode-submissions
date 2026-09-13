class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = list("".join(char for char in s.lower() if char.isalnum()))
        i,j = 0,len(new_s)-1

        answer = True
        while i < j:
            if new_s[i] == new_s[j]:
                i += 1
                j -= 1
            else:
                answer = False
                break
        return answer
        
        