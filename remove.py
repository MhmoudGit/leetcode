def remove_element(nums: list[int], val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)


print(remove_element(nums=[0, 1, 2, 2, 3, 0, 4, 2, 2], val=2))
