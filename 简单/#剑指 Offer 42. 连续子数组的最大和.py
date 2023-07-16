from typing import List


def maxSubArray(nums: List[int]) -> int:
    """动态规划"""
    table = [int(-float('inf'))] * (len(nums))
    table[0] = nums[0]
    for i in range(1, len(nums)):
        table[i] = max(table[i-1] + nums[i], nums[i])
    return max(table)


def maxSubArray2(nums: List[int]) -> int:
    max_sum, sum = nums[0], 0
    for num in nums:
        sum = max(sum + num, num)
        max_sum = max(sum, max_sum)
        # print(max_sum)
    return max_sum


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [-1]
    print(maxSubArray2(nums))