def removeElement(nums: list[int], val: int):
  k = 0
  for i in range(len(nums)):
    if nums[i] != val:
      nums[k] = nums[i]
      k += 1
  return k
  
  

nums1 = [3,2,2,3]
nums2 = [0,1,2,2,3,0,4,2]

print(removeElement(nums1, 3))
print(removeElement(nums2, 2))

