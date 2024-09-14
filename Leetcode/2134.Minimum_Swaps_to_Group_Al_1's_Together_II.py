def minSwaps(nums) -> int:
  N = len(nums)
  total_ones = nums.count(1)

  #sliding window technique
  l = 0
  r = N - 1

  
  
  

nums = [ 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0 ]
swaps = minSwaps(nums)
print(swaps)