class Solution:
    """
    @param target: the target
    @param array: an array
    @return: the closest value
    """
    def closestTargetValue(self, target, array):
        array.sort()
        diff = float('inf')
        left, right = 0, len(array) - 1
        
        while left < right:
            cur_diff = target - array[left] - array[right]
            
            if cur_diff < 0:
                right -= 1
            else:
                diff = min(diff, cur_diff)
                left += 1

        return -1 if diff == float('inf') else target - diff