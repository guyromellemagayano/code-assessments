import re

"""
Codeland Username Validation

Have the function CodelandUsernameValidation(str) take the `str` parameter 
being passed and determine if the string is a valid username 
according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, 
otherwise return the string false.

Examples:

Input: "aa_"
Output: false

Input: "u__hello_world123"
Output: true
"""


def CodelandUsernameValidation(strParam):
    pattern = re.compile(r"^[a-zA-Z][\w_]{2,23}[^_]$")
    res = pattern.match(strParam)
    strParam = "true" if res else "false"
    return strParam


# keep this function call here
print(CodelandUsernameValidation(input()))
