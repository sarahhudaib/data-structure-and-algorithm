def validate_brackets(string):
    """ validate brackets representing whether or not the brackets in the string are balanced"""
    stack = []
    # mapping closing bracket to opening bracket
    closeToOpen = {'{': '}',
                   '[': ']',
                   '(': ')'}

    closing_vals = closeToOpen.values()
    # to check if this character is a closing bracket
    for x in string:
        # if we have an open brackets append it to the stack and continue
        if x in closeToOpen:
            stack.append(x)
        # if we have a closing bracket check if it matches the last open bracket
        if x in closing_vals:
            # if the last open bracket is not the same as the closing bracket
            if not stack or x != closeToOpen[stack.pop()]:
                return False
# return True if the stack is empty and we have checked
# all the characters in the string and there are no unmatched brackets
    return True if len(stack) == 0 else False


if __name__ == '__main__':
    print(validate_brackets("()[[Extra Characters]]"))
    print(validate_brackets("(){}[[]]"))
    print(validate_brackets("{}{Code}[Fellows](())"))
    print(validate_brackets("[({}]"))
    print(validate_brackets("(]("))
    print(validate_brackets("{(})"))
    print(validate_brackets(")("))
    print(validate_brackets("([)]"))
