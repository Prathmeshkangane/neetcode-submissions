import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        list1 = "".join(re.findall(r"[a-zA-Z0-9]", s))
        list2 = "".join(list(reversed(list1)))

        return list1.lower() == list2.lower()
        