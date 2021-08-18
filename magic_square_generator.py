import time

if __name__ == "__main__":
    constant = int(input("Enter any random number between 22 and 99:\n"))
    A = constant-20
    B = A+1
    C = B+1
    D = A-1
    magicSquare = [
        [A, 1, 12, 7],
        [11, 8, D, 2],
        [5, 10, 3, C],
        [4, B, 6, 9]
    ]
    for row in magicSquare:
        print(row)
        time.sleep(0.5)
