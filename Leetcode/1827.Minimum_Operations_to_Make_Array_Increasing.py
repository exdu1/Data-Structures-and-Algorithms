nums = [1, 5, 2, 4, 1]

def MinimumOperations(nums: list):
    operations: int = 0

    for i in range(0, len(nums) - 1):
        if nums[i] >= nums[i + 1]:
            difference: int = nums[i] - nums[i + 1] + 1
            nums[i+1] += difference
            operations += difference
    return operations

print(MinimumOperations(nums))
    