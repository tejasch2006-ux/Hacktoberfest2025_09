from typing import List

def find_max_consecutive_ones(nums: List[int]) -> int:
    """
    Returns the maximum number of consecutive 1s in the given binary list.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count


if __name__ == "__main__":
    # Take input from user
    binary_input = input("Enter binary numbers separated by spaces (e.g., 1 1 0 1 1 1): ").split()
    nums = [int(x) for x in binary_input]
    result = find_max_consecutive_ones(nums)
    print("The maximum number of consecutive 1's is:", result)
