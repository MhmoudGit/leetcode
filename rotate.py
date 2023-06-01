def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if len(nums) % 2 == 0:
        x = nums[k:]
        nums[k:] = nums[:k]
        nums[:k] = x
    elif k < len(nums):
        x = nums[k + 1 :]
        nums[k:] = nums[: k + 1]
        nums[:k] = x
    print(nums)


print(rotate(nums=[-1, -100, 3, 99], k=2))
