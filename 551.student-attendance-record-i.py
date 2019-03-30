#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#
# https://leetcode.com/problems/student-attendance-record-i/description/
#
# algorithms
# Easy (45.16%)
# Total Accepted:    48.6K
# Total Submissions: 107.5K
# Testcase Example:  '"PPALLP"'
#
# You are given a string representing an attendance record for a student. The
# record only contains the following three characters:
# 
# 
# 
# 'A' : Absent. 
# 'L' : Late.
# ⁠'P' : Present. 
# 
# 
# 
# 
# A student could be rewarded if his attendance record doesn't contain more
# than one 'A' (absent) or more than two continuous 'L' (late).    
# 
# You need to return whether the student could be rewarded according to his
# attendance record.
# 
# Example 1:
# 
# Input: "PPALLP"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "PPALLL"
# Output: False
# 
# 
# 
# 
# 
#
class Solution:
    def checkRecord(self, s: str) -> bool:
        if not s: return False
        
        A, L= 0, 0
        last = None
        
        for c in s:
            if c == 'A':
                A += 1
            elif c == 'L':
                L += 1
            
            if A > 1 or L > 2: return False        
            if c != 'L': L = 0
            last = c
        
        return True

