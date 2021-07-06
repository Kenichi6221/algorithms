def superDigit(n, k):
    # Write your code here
    if len(n)==1:
        return n

    total = 0
    for element in n:
        total += int(element)

    total = total*k

    return superDigit(str(total),1)