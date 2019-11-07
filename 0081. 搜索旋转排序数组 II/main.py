class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
                
            if nums[left] == nums[mid]:
                left+=1
                continue
            
            # 如果左边是有序的
            elif nums[left] <= nums[mid]:
                if (nums[mid] > target and nums[left] <= target):
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if (nums[mid] > target or target >= nums[left]):
                    right = mid - 1
                else:
                    left = mid + 1

        return False


s = Solution()
print(s.search([2,5,6,0,0,1,2], 0))
