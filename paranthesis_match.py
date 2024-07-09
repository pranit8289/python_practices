"""
Problem statement - please find given set of Parentheses are Valid Parentheses or not

input1 = [{()}] - True
input2 = [()}] - False
input3 = {()}] - False
"""

"""
Algorithm
check if we are getting opening bracket, then add to stack
when we get closing bracket, check latest pushed element in the stack
if that parentheses is matching with closing parentheses then pop it and move to next one
if your array is finished and if your stack has no elements in it, then True, otherwise false
"""


def balancedBrackets(parentheses_series):
    # Write your code here.
    opening_parenteses = "([{"
    closing_parantheses = ")]}"
    mapping = {
        ")":"(", "}": "{", "]": "["
    }
    stack = []
    for count, parentheses in enumerate(parentheses_series):
        if parentheses in opening_parenteses:
            stack.append(parentheses)
        elif parentheses in closing_parantheses:
            if len(stack) == 0:
                return False
            if mapping[parentheses] == stack[-1]:
                stack.pop()
            else:
                return False
    return len(stack) == 0






if __name__ == "__main__":
    parentheses_series = r"""{[()]}"""
    parentheses_series = r"""()[]{}{"""
    print(balancedBrackets(parentheses_series=parentheses_series))
