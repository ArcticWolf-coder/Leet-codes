class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a={}
        n=len(nums)
        n/=2
        for i in nums:
            if i in a.keys():
                a[i]+=1
            else:
                a[i]=1
            if a[i]>n:
                return i