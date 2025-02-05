# Logarithmic Time complexity

def binary_search(arr, target):
    left, right = 0, len(arr) - 1                   # first we Initialize Pointers
    while left <= right:                            # Loop Until left ≤ right
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1                                       # if target not found

print(binary_search([1, 3, 5, 7, 9], 5))  # Output: 2


# TC = O(log n)     -->     it divides the search space in half
# SC = O(1)         -->     no extra space