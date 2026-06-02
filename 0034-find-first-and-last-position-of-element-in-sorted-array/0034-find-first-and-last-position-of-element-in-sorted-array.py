class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def target_search(is_left_index, l,r):
            target_index = -1
            while l<=r:
                mid = l + (r - l) // 2

                if nums[mid] == target:
                    target_index = mid
                    if is_left_index:
                        r = mid-1
                    else:
                        l = mid+1
                elif nums[mid] > target:
                    r = mid-1
                else:
                    l = mid+1
            
            return target_index

        l,r = 0,len(nums)-1

        left_index = target_search(True, l,r)
        if left_index == -1:
            return [-1,-1]
        
        right_index = target_search(False, left_index,r)
        
        return [left_index, right_index]