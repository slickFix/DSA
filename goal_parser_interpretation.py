# https://leetcode.com/problems/goal-parser-interpretation/


class Solution:
    def interpret(self, command: str) -> str:
        
        ret_str = ''
        le = len(command)
        
        for i in range(le):
            if command[i] == '(' and i+1<=le and command[i+1] == ')':
                ret_str+='o'
            elif command[i] == 'G':
                ret_str+='G'
            elif command[i] == '(' and i+3<=le and command[i+3] == ')':
                ret_str+='al'
                
        return ret_str
