class Solution:
    def search(self, nums: List[int], target: int) -> int:
            
    ## The array has been rotated at an index k which has been taken as the pivot
    
        left,right=0,len(nums)-1
        ## completing the initializations

        while left <= right:
            mid = (left+right)//2

            if nums[mid]==target:
                return mid

            elif nums[mid]>=nums[left]:
                ## That means we are in left sorted part

                if target<=nums[mid] and target>=nums[left] :
                    right=mid-1
                else:
                    left=mid+1

            else:
                ## we are in right part of the list
                if target>nums[mid] and target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1

        return -1