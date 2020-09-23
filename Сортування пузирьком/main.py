nums = [2, 5, 6, 6, 2, 1, 6, 6, 9, 7]

print(nums)

swaps = True
while swaps:
    swaps = False

    for j in range(len(nums) - 1):
        if nums[j] > nums[j + 1]:
            swaps = True
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

            print(nums)

print("test valik 1")
print()
