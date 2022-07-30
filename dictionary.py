def no(n):
    while(n > 9):
        sum = 0
        for i in str(n):
            sum = sum + int(i)
        n = sum
    return n


def test(n):
    while n > 9:
        sum = 0
        while n != 0:
            sum += n % 10
            n //= 10
        n = sum
    return sum


n = 99999
print(test(n))
