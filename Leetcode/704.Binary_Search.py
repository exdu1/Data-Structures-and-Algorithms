def search(nums: list[int], target: int) -> int:
  l, r = 0, len(nums) - 1
  while l < r:
    m = (l + r) // 2
    if nums[m] < target:
      l = m + 1
    elif target > nums[m]:
      r = m - 1
    else:
      return m
  return -1

result = search([-1, 0, 3, 5, 9, 9, 9, 9, 9, 9, 12], 9)
print(result)
