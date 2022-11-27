# Python3 program to check for balanced brackets.
import sys

# function check_brackets(bracket_string), to check if brackets are balanced


def check_brackets(bracket_string):
    bracket_stack = []

    # Traversing the bracket_string
    for char in bracket_string:
        if char in ["(", "{", "["]:

            # Push the element in the bracket_stack
            bracket_stack.append(char)
        else:

            # If current character is not opening bracket, then it must be closing.
            # So bracket_stack cannot be empty at this point.
            if not bracket_stack:
                return False
            current_char = bracket_stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    # Check for empty bracket_stack
    if bracket_stack:
        return False
    return True


# Main code
if __name__ == "__main__":
    if len(sys.argv) == 2:
        bracket_string = sys.argv[1]
    else:
        print("Wrong input")
        quit()

    # Check the brackets to see if they are balanced
    if check_brackets(bracket_string):
        print("True")
    else:
        print("False")
