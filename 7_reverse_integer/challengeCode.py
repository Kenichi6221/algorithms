
import math
import sys

import os
current_folder = os.path.dirname(os.path.realpath(__file__))
# redirect input from input.txt file
sys.stdin = open("{}\\input.txt".format(current_folder), "r")

# redirect output tou output.txt file
sys.stdout = open('{}\\output.txt'.format(current_folder), 'w')


def reverse(x: int) -> int:
    min_value = 2147483648
    max_value = 2147483647

    if x < 10 and x>-10:
        return x

    factor = -1 if x<0 else 1
    x *= factor
    total_digits = math.floor(math.log10(x))
    result = 0

    if total_digits>10:
        return 0

    if 1**total_digits == x:
        return 1*factor

    while total_digits>=0:
        nextDigit = (x%10)
        if (factor<0 and min_value-result<nextDigit) or (factor>0 and max_value-result<nextDigit):
            return 0

        result += nextDigit*(10**total_digits)
        x //= 10
        total_digits-=1

    return result*factor

if __name__ == '__main__':
  for line in sys.stdin:
    value = int(line)
    print(reverse(value))
