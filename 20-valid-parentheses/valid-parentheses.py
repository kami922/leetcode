class Solution:
    def isValid(self, s: str) -> bool:
        open_stack = []
        close_stack = []
        count = 0
        for bracket in s:
            if bracket == "(" or bracket == "{" or bracket == "[":
                open_stack.append(bracket)

            else:
                if len(open_stack) == 0:
                    return False
                elif bracket == ")" and open_stack.pop() != "(":
                    return False
                elif bracket == "]" and open_stack.pop() != "[":
                    return False
                elif bracket == "}" and open_stack.pop() != "{":
                    return False

        return len(open_stack) == 0
        