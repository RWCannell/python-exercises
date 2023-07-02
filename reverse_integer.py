# we divide by 10 to get the last digit in the number
def reverse_digits(integer):
    reversed_integer = 0
    remainder = 0

    while integer > 10:
        remainder = integer % 10
        integer = integer // 10
        reversed_integer = reversed_integer*10 + remainder
    return reversed_integer

if __name__ == "__main__":
    integer = 123456789
    solution = reverse_digits(integer)
    print(solution)