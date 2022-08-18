# takes a positive integer parameter, n, and returns a list
# containing the Collatz sequence for n
def collatzSequence(n):
    if n == 1:
        return [1]
    elif n % 2 == 0:
        return [n] + collatzSequence(n//2)
    else:
        return [n] + collatzSequence(3*n + 1)


def maxLength(m):
    max_length = 0
    num = 0
    for i in range(1,m+1):
        if len(collatzSequence(i)) > max_length:
            max_length = len(collatzSequence(i))
            num = i
    return num, max_length

def maxValue(m):
    max_value = 0
    num = 0
    for i in range(1,m+1):
        if max(collatzSequence(i)) > max_value:
            max_value = max(collatzSequence(i))
            num = i
    return num, max_value

if __name__ == '__main__':
    n = int(input('Enter a positive integer: '))
    print(f'For number <= {n}')
    print(f'{maxLength(n)[0]} is the longest Collatz sequence. The length is {maxLength(n)[1]}.')
    print(f'{maxValue(n)[0]} has the largest number in the sequence. The number is {maxValue(n)[1]}.')