class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        flag =True
        i=0
        j=0
        while flag:
            j=i+1
            while (j < length):
                if nums[i] + nums[j] == target:
                    return([i,j])
                    flag = False
                j += 1
            i += 1
            if i == length:
                flag = False
                return []