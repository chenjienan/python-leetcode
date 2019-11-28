/*
 * @lc app=leetcode id=154 lang=java
 *
 * [154] Find Minimum in Rotated Sorted Array II
 */

// @lc code=start
class Solution {
    public int findMin(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] > nums[right]){
                left = mid;
            }else if (nums[mid] < nums[right]) {
                right = mid;
            }else { // when nums[mid] == nums[right]
                right--; 
            }            
        }        
        return nums[left] < nums[right] ? nums[left] : nums[right];
    }
}
// @lc code=end
