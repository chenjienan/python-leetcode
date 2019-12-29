/*
 * @lc app=leetcode id=838 lang=java
 *
 * [838] Push Dominoes
 */

// @lc code=start
class Solution {
    public String pushDominoes(String dominoes) {
        char[] arr = dominoes.toCharArray();
        int n = dominoes.length();
        int[] force = new int[n];
        
        int f = 0;
        
        for (int i = 0; i < n; i++){
            if (arr[i] == 'R'){
                f = n;
            }else if (arr[i] == 'L'){
                f = 0;
            }else{
                f = Math.max(f-1, 0);
            }
            force[i] += f;
        }
        
        for (int i = n-1; i > -1; i--){
            if (arr[i] == 'R'){
                f = 0;
            }else if (arr[i] == 'L'){
                f = n;
            }else{
                f = Math.max(f-1, 0);
            }
            force[i] -= f;
        }
        
        for (int i = 0; i < n; i++){
            if (force[i] > 0){
                arr[i] = 'R';
            }else if (force[i] < 0){
                arr[i] = 'L';
            }else{
                arr[i] = '.';
            }
        }
        
        return new String(arr);
    }
}
// @lc code=end

