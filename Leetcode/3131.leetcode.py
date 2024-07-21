def sortSequence(nums: list[int]) -> list[int]:
        for num in range(0, len(nums) - 1):
            current: int = nums[num]
            next: int = nums[num + 1]
            temp: int = 0

            if current < next:
                temp = current
                current = next
                next = temp

                nums[num] = current
                nums[num + 1] = next
        return nums

def addedIntegerCustom(nums1: list[int], nums2: list[int]) -> int:
        #sort nums1 and nums2
        sortSequence(nums1)
        sortSequence(nums2)
        
        #find the common difference for nums1 and nums2
        return nums2[0] - nums1[0] 

def addedInteger(nums1: list[int], nums2: list[int]) -> int:
      nums1.sort()
      nums2.sort()

      return nums2[0] - nums1[0]
        

nums1 = [2, 6, 4]
nums2 = [9, 7, 5]
print(addedIntegerCustom(nums1, nums2))