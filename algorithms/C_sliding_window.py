"""Sliding Window"""

def max_sum_subarray(nums: list[int], k: int) -> int:
    max_sum = 0
    running_sum = 0
    for index, value in enumerate(nums):
        running_sum += value
        if index == k - 1:
            max_sum = max(max_sum, running_sum)
        elif index > (k - 1):
            running_sum -= nums[index - (k)]
            print(f'{index = }')
            print(f'{nums[index - k] = }')
            max_sum = max(max_sum, running_sum)
            print(f'{max_sum = }')
            print(f'{running_sum = }\n')
    return max_sum

kamote = [7, 2, 9, 4, 1, 6, 5, 9]
print(max_sum_subarray(kamote, 3))