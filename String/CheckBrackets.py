def CheckCompleteBrackets(str):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    bracket_map = {")": "(", "}": "{", "]": "["}
    
    for char in str:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    
    return len(stack) == 0
# Test cases
test_str1 = "{[()]}"
test_str2 = "{[(])}"
test_str3 = "{[}"
CheckCompleteBrackets(test_str1) # True
CheckCompleteBrackets(test_str2) # False
CheckCompleteBrackets(test_str3) # False
