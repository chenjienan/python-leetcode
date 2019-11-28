/*
 * @lc app=leetcode id=153 lang=java
 *
 * [153] Find Minimum in Rotated Sorted Array
 */

// @lc code=start
class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]){
                left = mid;
            }else {
                right = mid;
            }
        }        
        return nums[left] < nums[right] ? nums[left] : nums[right];
    }
}
// @lc code=end

