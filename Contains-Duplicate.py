def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    myset = {n for n in nums}
    compare = [n for n in myset]
    compare.sort()
    if compare == nums:
        return False
    else:
        return True


print(containsDuplicate([1,5,-2,-4,0]))
