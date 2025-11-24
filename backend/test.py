def remove_positive_rec(nums, index=0):
    """Recursively remove positive numbers from a list."""
    if index >= len(nums):
        return []
    current = nums[index]
    rest = remove_positive_rec(nums, index + 1)
    if current <= 0:
        return [current] + rest
    else:
        return rest

def power_four_sum_rec(nums, index=0):
    """Recursively calculate sum of fourth powers of numbers in a list."""
    if index >= len(nums):
        return 0
    return nums[index] ** 4 + power_four_sum_rec(nums, index + 1)

def negative_sum(nums):
    """Compute sum of fourth powers for non-positive numbers."""
    filtered = remove_positive_rec(nums)
    return power_four_sum_rec(filtered)

def main():
    # Example test cases
    test_cases = [
        [-2, 3, 0, -1],  # expected output: 17
        [5, -1, -1],     # expected output: 2
        [0, 2, -2, -3]   # expected output: 97
    ]
    
    # Process each test case
    if len(test_cases) > 0:
        print(negative_sum(test_cases[0]))
    if len(test_cases) > 1:
        print(negative_sum(test_cases[1]))
    if len(test_cases) > 2:
        print(negative_sum(test_cases[2]))

# Entry point
if __name__ == "__main__":
    main()
