"""Next Largest Element"""

def next_largest_element(nums: list[int]) -> int:
    ms = []
    ans = []

    for index, value in enumerate(nums):
        ans.append(-1)
        while ms and nums[ms[-1]] <= value: 
            ans[ms.pop()] = value
        ms.append(index)

    return ans

next_largest_test = [1, 3, 7, 3, 2, 5, 6, 2, 3]
print(next_largest_element(next_largest_test))