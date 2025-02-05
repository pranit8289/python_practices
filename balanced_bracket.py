"""
Write a function that takes in a string made up of brackets ([,(,[,{  ]) and other optional characters. The function should return a
  boolean representing whether the string is balanced with regards to brackets.

A string is said to be balanced if it has as many opening brackets of a
certain type as it has closing brackets of that type and if no bracket is
unmatched. Note that an opening bracket can't match a corresponding closing
bracket that comes before it, and similarly, a closing bracket can't match a
corresponding opening bracket that comes after it. Also, brackets can't
overlap each other as in [(])

Samplt Input 
([])(){}(())()() - True
"""

input_string = "([]"



def balanced_bracket(input_string):
    stack = []
    opening_brackets = "({["
    closing_brackets = ")}]"
    brancket_pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for string in input_string:
        if string in opening_brackets:
            stack.append(string)
        elif string in closing_brackets:
            if len(stack) == 0:
                return False
            if brancket_pairs[string] == stack[-1]:
                stack.pop()
        
    return len(stack) == 0

print(balanced_bracket(input_string))

