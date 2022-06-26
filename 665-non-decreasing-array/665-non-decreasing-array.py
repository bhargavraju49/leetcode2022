class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        slow = -1*sys.maxsize
        flag = 0
        for j,i in enumerate(nums):
            print(i,j,slow)
            if i<slow and flag==0:
                if j-2 >=0 and nums[j-2]<nums[j]:
                    slow = nums[j]
                elif j-2 >=0 and nums[j-2]>nums[j]:
                    print('ok')
                    slow = nums[j-1]
                elif j-2 >=0 and j+1<len(nums) and nums[j-2]==nums[j]:
                    if nums[j-1]>nums[j+1]:
                        slow = nums[j]
                elif j-2 < 0 and j+1 < len(nums) and slow>nums[j+1]:
                    slow = nums[j]
                    print('ok')
                flag = 1
            elif i<slow and flag == 1:
                print(i,slow)
                return False
            else:
                slow = i
        return True