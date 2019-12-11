/*
 * @lc app=leetcode id=34 lang=java
 *
 * [34] Find First and Last Position of Element in Sorted Array
 */

// @lc code=start
class Solution {
    public int[] searchRange(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return new int[]{-1, -1};
        }
        
        int left = searchFirst(nums, target);
        int right = searchLast(nums, target);
        
        return new int[]{left, right};
    }
    
    private int searchFirst(int[] A, int x) {
        int start = 0;
        int end = A.length - 1;
        
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            
            if (A[mid] >= x) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (A[start] == x) {
            return start;
        }
        if (A[end] == x) {
            return end;
        }
        return -1;
    }
    
    private int searchLast(int[] A, int x) {
        int start = 0;
        int end = A.length - 1;
        
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            
            if (A[mid] > x) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (A[end] == x) {
            return end;
        }
        
        if (A[start] == x) {
            return start;
        }
        return -1;
    }
}
// @lc code=end

