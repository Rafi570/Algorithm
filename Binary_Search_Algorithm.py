class Solution:
    def search(self, nums, target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1
ob=Solution()
arrayy=[10,20,3,0,5,0,9,20]
arrayy.sort()
print(arrayy)
print(ob.search(arrayy,5))
