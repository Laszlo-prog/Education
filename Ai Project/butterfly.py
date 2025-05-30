def print_butterfly(n):
    #print upper half of the butterfly

    for i in range(n):
        print('*' * (i + 1) + ' ' * (n - i - 1) + ' ' * (n - i - 1) + '*' * (i + 1))

    for i in range(n -2, - 1, - 1):
        print(
            '*' * (i + 1) + ' ' * (n - i - 1) +
            ' ' * (n - i - 1) + '*' * (i + 1)
        )
if __name__ == "__main__":
        print_butterfly(1)