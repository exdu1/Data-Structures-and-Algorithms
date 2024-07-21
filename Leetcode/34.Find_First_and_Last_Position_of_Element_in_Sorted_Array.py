def searchRange(nums: list[int], target: int):
  pass

def binSearch(nums: list[int], target: int, leftBias: bool) -> int:
  l, r = 0, len(nums) - 1
  i = -1
 
  while l <= r:
   m = (l + r) // 2

   if target > nums[m]:
    l = m + 1
   elif target < nums[m]:
    r = m - 1
   else:
    i = m
    if leftBias:
     r = m - 1
    else:
     l = m + 1
     
  return i
   
nums = [5, 7, 8, 8, 8, 8, 8, 10]
left = binSearch(nums, 8, True)
right = binSearch(nums, 8, False)
print([left, right])
   