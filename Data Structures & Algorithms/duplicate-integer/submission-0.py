class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # for slow in range(len(nums)):
        #     for fast in range(slow + 1, len(nums)):
        #         if nums[slow] == nums[fast]:
        #             return True
        # return False
        hashmap1 = set()

        for num in nums:
            if num in hashmap1:
                return True
            hashmap1.add(num)
        
        return False