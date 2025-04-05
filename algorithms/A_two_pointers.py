"""Check If Palindrome"""

def check_if_palindrome(iterable) -> bool:
    left = 0
    right = len(iterable) - 1
    while left < right:
        if iterable[left] != iterable[right]:
            return False
        else: 
            left += 1
            right -= 1
    return True

test_str = "racecar"
print(check_if_palindrome(test_str))

"""Twosum II"""

def check_sum_exists(nums, target) -> list[int]:
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        if sum < target:
            left += 1
        elif sum > target:
            right -= 1
    return []

test_nums = [1, 1]
print(check_sum_exists(test_nums, 3))

"""Middle Point"""

def middle_point(nums) -> int:
    slow, fast = 0, 0
    while fast < len(nums) - 1:
        slow += 1
        fast += 2
    return nums[slow]

test_midpoint = [1, 2, 3, 4, 5, 6, 7, 8]
print(middle_point(test_midpoint))

"""Happy Number"""

def check_happy(num: int) -> int:
    def get_next(input) -> int:
        sum = 0
        while input > 0:
            digit = input % 10
            sum += digit * digit
            input = input // 10
        return sum
    
    slow = num
    fast = get_next(num)

    while fast != 1 and slow != fast:
        slow = get_next(slow)
        fast = get_next(get_next(fast))

    return fast == 1

happy_test = 4
print(check_happy(happy_test))
