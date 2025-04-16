"""Binary Search"""

def binary_search(nums: list[int], k: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == k:
            return mid
        elif nums[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
            
    return None

list_test = [1, 3, 6, 9, 10, 15, 18, 20, 22, 26, 30]
print(binary_search(list_test, 37))