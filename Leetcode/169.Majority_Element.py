def majorityElement(nums: list[int]) -> int:
    m: int = None
    c: int = 0

    for num in nums:
        if c == 0:
            m = num
            c = 1
        elif num == m:
            c += 1
        else:
            c -= 1
    return m

        
test1 = [3,2,3]
test2 = [3,3,4]
test3 = [2,2,1,1,1,2,2]

print(majorityElement(test1))
print(majorityElement(test2))