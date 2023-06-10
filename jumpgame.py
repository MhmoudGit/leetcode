def can_jump(nums: list[int]) -> bool:
    max_reach = 0  # Maximum index that can be reached
    n = len(nums)
    
    for i in range(n):
        # If the current index is beyond the maximum reach, return False
        if i > max_reach:
            return False
        
        # Update the maximum reach if the current index + jump length is greater
        if i + nums[i] > max_reach:
            max_reach = i + nums[i]
        
        # If the maximum reach exceeds or equals the last index, return True
        if max_reach >= n - 1:
            return True
    
    return False  # Cannot reach the last index
    


print(can_jump(nums=[3, 2, 1, 1, 4]))
