class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a=[]
        for i in nums:
            if i in a:
                a.remove(i)
            else :
                a.append(i)
        return a[0]