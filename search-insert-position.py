
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1

        if nums[i]==target:
            return 0

        if nums[j]==target:
            return j

        if nums[i]>target:
            return 0

        if nums[j]<target:
            return j+1


        while j-i>1:
            mid = (i+j)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                j = mid
            elif nums[i]<target:
                i = mid

        return i+1
