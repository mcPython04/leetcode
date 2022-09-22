
# Three Sum (15)
# https://leetcode.com/problems/3sum/
def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        # add for loop to check for initial value
        for i, val in enumerate(nums):
            
            # checks for initial duplicates
            if i > 0 and nums[i-1] == val:
                continue
                
            l, r = i+1, len(nums) - 1
            
            # 2 Sum approach 2 pointers
            while l < r:
                
                three = val + nums[l] + nums[r]
                
                if three > 0:
                    r -= 1
                elif three < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    
                    # keep iterating through array by shifting left pointer
                    # might find another pair
                    # left pointer must surpass right pointer in order to break from loop
                    l += 1
                    
                    # checks for duplicates
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res
