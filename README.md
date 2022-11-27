# check_balanced_brackets

A Python script to check balanced brackets

This is a simple Python script for checking if a series of brackets
are balanced.

Every opening bracket must have a corresponding closing bracket.
We can approximate this using strings. Given a string containing
just the characters '(', ')', '{', '}', '[' and ']', the script
determines if the input string is valid

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False

Usage:
python3 check_brackets.py "({[)]"
Returns: False

python3 check_brackets.py "[()]{}"
Returns: True

python3 check_brackets.py "[()]{}" "Something else"
Returns: Wrong input

python3 check_brackets.py
Returns: Wrong input
