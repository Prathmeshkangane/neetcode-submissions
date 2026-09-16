class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        max_ans = 0
        l,r = 0,len(height)-1
        while l < r:
            width = r - l
            ht = min(height[l],height[r])
            answer = width * ht
            max_ans = max(max_ans,answer)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_ans       