'''
题目：两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。

示例：
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''


# 解法一：暴力破解法(Python一般通不过)
class Solution1:
    def twoSum(self, nums, target):
        '''
        type nums: List[int]
        type target: int
        rtype: List[int]    
        
        '''
        result = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
        return result


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        # enumerate()函数：得到元素索引和元素组成的索引序列
        for i, m in enumerate(nums):
            j = i + 1
            while j < size:
                if target == (m + nums[j]):
                    return [i, j]
                else:
                    j += 1

