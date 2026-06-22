class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # floyd
        # i -> index, nums[i] = res(next index) 
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: # find meeting point
                break;
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow
        return -1
            
