"""
Questions Marks

Have the function QuestionsMarks(str) take the `str` string parameter,
which will contain single digit numbers, letters, and question marks,
and check if there are exactly 3 question marks between every pair of
two numbers that add up to 10. If so, then your program should return
the string 'true', otherwise it should return the string 'false'.
If there aren't any two numbers that add up to 10 in the string, then
your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should
return true because there are exactly 3 question marks between 6 and 4,
and 3 question marks between 5 and 5 at the end of the string.

Examples:

Input: "aa6?9"
Output: false

Input: "acc?7??sss?3rr1??????5"
Output: true
"""


def isDigit(d):
    try:
        int(d)
        return True
    except ValueError:
        return False


def QuestionsMarks(strParam):
    question_marks = 0
    current_int = None
    exists = False

    for i in range(len(strParam)):
        if isDigit(strParam[i]):
            if current_int is not None and int(strParam[i]) + current_int == 10:
                exists = True
                if question_marks != 3:
                    return "false"
                question_marks = 0  # Reset for next pair
            current_int = int(strParam[i])
        elif strParam[i] == "?" and current_int is not None:
            question_marks += 1

    return "true" if exists else "false"


# keep this function call here
print(QuestionsMarks(input()))
