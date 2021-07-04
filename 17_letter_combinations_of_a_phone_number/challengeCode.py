from typing import List

class Solution:
    dial_dictionary = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }

    def is_a_solution(self,letters,current_digit,current_letter):
        return current_digit == len(letters)

    def process_solution(self,subset,final_result, k):
        if len(subset) == k:
            final_result.append("".join(subset))
        else:
            print(f"subset: {subset}_________________________")


    def backtrack(self,letters,subset,final_result,total_digits,current_digit,current_letter):
        if self.is_a_solution(letters,current_digit,current_letter):
            self.process_solution(subset,final_result, len(letters))
            #print(f"letters:{letters},current_digit:{current_digit},current_letter:{current_letter}")
        else:
            total_letters = len(letters[current_digit])
            for letter in range(total_letters):
                subset.append(letters[current_digit][letter])
                self.backtrack(letters,subset,final_result,total_digits,current_digit+1,letter)
                subset.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        total_digits = len(digits)

        if total_digits == 0:
            return []

        letters = []
        for digit in digits:
            letters.append(self.dial_dictionary[digit])

        final_result = []

        current_digit = 0
        current_letter = 0

        self.backtrack(letters,[],final_result,total_digits,current_digit,current_letter)
        return final_result

if __name__ == '__main__':
  s = Solution()
  digits = ["5","6","7","8"]
  print(s.letterCombinations(digits))
