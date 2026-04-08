class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {"]":"[", "}":"{", ")":"("}
        stack = [] 
        for b in s:
            if b in "[{(":
                stack.append(b)
            else:
                if stack:
                    tmp_open = stack.pop()
                    if bracket_dict[b] == tmp_open:
                        continue 
                    else:
                        return False
                else:
                    return False
        return not stack