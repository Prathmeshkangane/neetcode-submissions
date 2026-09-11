class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = {}
        dict_2 = {}

        for l1 in list(s):
            if l1 not in dict_1:
                dict_1[l1] = 1
            else:
                dict_1[l1] += 1
        
        for l2 in list(t):
            if l2 not in dict_2:
                dict_2[l2] = 1
            else:
                dict_2[l2] += 1
        
        return dict_1 == dict_2
        