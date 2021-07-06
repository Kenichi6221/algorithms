def superDigit(n, k):
    if len(n)==1:
        return n
    total = 0

    for element in n:
        total += int(element) % 9
    first_multiple = total % 9
    second_multiple = k % 9
    result = (first_multiple * second_multiple) % 9

    if result == 0:
        return 9

    return result