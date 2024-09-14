def FindIndex(nums: list, target: int) -> int:
  l, r = 0, len(nums) - 1

  while l <= r:
    m = (l + r) // 2
    
    if nums[m] == target:
      return m
    elif nums[m] > target:
      r = m - 1
    else:
      l = m + 1
  
  return l


target = 5
nums = [1, 3, 5, 6] # return 2


print(FindIndex(nums, target))

