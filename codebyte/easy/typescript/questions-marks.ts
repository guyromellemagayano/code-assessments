/**
 * Questions Marks
 *
 * Have the function QuestionsMarks(str) take the `str` string parameter,
 * which will contain single digit numbers, letters, and question marks,
 * and check if there are exactly 3 question marks between every pair of
 * two numbers that add up to 10. If so, then your program should return
 * the string 'true', otherwise it should return the string 'false'.
 * If there aren't any two numbers that add up to 10 in the string, then
 * your program should return false as well.
 *
 * For example: if str is "arrb6???4xxbl5???eee5" then your program should
 * return true because there are exactly 3 question marks between 6 and 4,
 * and 3 question marks between 5 and 5 at the end of the string.
 *
 * Examples:
 *
 * Input: "aa6?9"
 * Output: false
 *
 * Input: "acc?7??sss?3rr1??????5"
 * Output: true
 */
function QuestionsMarks(str: string): boolean {
  let new_str = str.replace(/[a-zA-Z]/g, "");
  let number_of_question_marks = 0;
  let sum = 0;
  let numbers_processed = 0;

  if (!/\d/.test(new_str)) return false;

  for (let i = 0; i < new_str.length; i++) {
    if (parseInt(new_str[i])) {
      sum += parseInt(new_str[i]);
      numbers_processed++;
    } else if (new_str[i] == "?" && numbers_processed > 0)
      number_of_question_marks++;

    if (numbers_processed === 2) {
      if (sum >= 10 && !(number_of_question_marks == 3)) return false;

      numbers_processed = 1;
      sum = parseInt(new_str[i + 1]) ? 0 : parseInt(new_str[i]);
      number_of_question_marks = 0;
    }
  }

  return true;
}

// keep this function call here
// @ts-ignore
console.log(QuestionsMarks(readline()));
