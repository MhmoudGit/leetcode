def remove_duplicates(nums: list[int]) -> int:
    for num in nums:
            while nums.count(num) > 2:
                nums.remove(num)
    return len(nums)


print(remove_duplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))
