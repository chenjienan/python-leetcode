#
# @lc app=leetcode id=591 lang=python3
#
# [591] Tag Validator
#
class Solution:
    def isValid(self, code: str) -> bool:

        stack = []
        n = len(code)
        is_first_tag = False

        i = 0

        # 边界条件
        while i < n:

            # deal with CDATA
            # 找头
            if i+8 < n and code[i:i+9] == '<![CDATA[':
                i += 9  #跳过前9
                j = i
                # 找尾 
                # i+2 条件成立, code[i:i+3]才有意义
                while i+2 < n and code[i: i+3] !=']]>': i += 1
                if i+2 == n: return False
                i += 3  # 跳过尾关键字符
                
            # found close tag
            elif i+1 < n and code[i:i+2] == '</':
                i += 2 # 跳过前2
                j = i
                while i < n and code[i] != '>': i += 1  
                
                # cannot find '>'
                if i == n: return False
                tag_name = code[j:i]
                                
                if not stack or stack[-1] != tag_name: return False
                # 出栈
                stack.pop()
                i += 1
                # rule 1: The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.
                # 后面不能再加东西
                if not stack and i != n: return False

            # found open tag
            elif code[i] == '<':
                i += 1
                j = i   # first char of the tag name
                while i < n and code[i] != '>': i += 1
                
                if i == n: return False
                tag_name = code[j:i]

                if not self.isValidTag(tag_name): return False
                # 第一个tag头, j(第一个字符)必须为1
                if not is_first_tag and j != 1: return False
                is_first_tag = True
                stack.append(tag_name)
                i += 1
            
            # tag content
            else:
                i += 1

        # 从来没有一个tag
        if not is_first_tag: return False
        # 没有close tag
        return False if stack else True
        
    def isValidTag(self, s):
        if len(s) < 1 or len(s) > 9: return False
        for ch in s:
             if ch < 'A' or ch > 'Z': return False
        return True                

s = Solution()
s.isValid("<A<></A<>")

# tag head => push
# tag tail => pop

