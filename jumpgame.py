def can_jump(nums: list[int]) -> bool:
    target = nums[-1]
    current = nums[0]
    new = nums[current:]
    while len(new) != 0:
        current = new[0]
        if current == target:
            return True
        else:
            new[current:]
            return False


print(can_jump(nums=[3, 2, 1, 1, 4]))
