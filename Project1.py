def square_pattern(n):                                                         # Square pattern
    for i in range(n):
        print("* " * n)


def alphabet_square(n):
    for i in range(n):
        for j in range(n):
            print(chr(65 + j), end=" ")
        print()


def alphabet_row_square(n):
    for i in range(n):
        for j in range(n):
            print(chr(65 + i), end=" ")
        print()

# 3. Increasing Alphabet Square (A, B, C... continuously)
def alphabet_increasing_square(n):
    ch = 65  # ASCII of 'A'
    for i in range(n):
        for j in range(n):
            print(chr(ch), end=" ")
            ch += 1
            if ch > 90:  # reset to 'A' if beyond 'Z'
                ch = 65
        print()

# 4. Hollow Alphabet Square
def hollow_alphabet_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print(chr(65 + j), end=" ")
            else:
                print(" ", end=" ")
        print()

# 5. Reverse Alphabet Square (E D C B A)
def reverse_alphabet_square(n):
    for i in range(n):
        for j in range(n - 1, -1, -1):
            print(chr(65 + j), end=" ")
        print()


def alphabet_reverse_triangle(n):                                       #Reverse Right Triangle
    for i in range(n, 0, -1):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()


def inverted_right_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)


def right_triangle(n):
    for i in range(1, n + 1):
        print("* " * i)

def inverted_repeated_triangle(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(chr(65 + (n - i)), end=" ")
        print()


def alphabet_right_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(65 + j), end=" ")
        print()


def alphabet_repeated_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(65 + i), end=" ")
        print()


def inverted_number_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()



      

def diamond_pattern(n):
    # upper part
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * (2 * i - 1))                                 # Diamond pattern
    # lower part
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * (2 * i - 1))

def inverted_right_triangle(n):
    for i in range(n, 0, -1):                                                    # Inverted right triangle pattern
        print("* " * i)

def plus_symbol(n):
     for i in range(n):
         for j in range(n):
             if i == n // 2 or j == n // 2:
                 print("*", end=" ")
             else:
                 print(" ", end=" ")
         print()

# Main function
def main():
    n = 5 
    



    print("\nSquare Pattern:")
    square_pattern(n)



    print("\n1. Normal Alphabet Square:")
    alphabet_square(n)

    print("\n2. Same Row Alphabet Square:")
    alphabet_row_square(n)

    print("\n3. Increasing Alphabet Square:")
    alphabet_increasing_square(n)

    print("\n4. Hollow Alphabet Square:")
    hollow_alphabet_square(n)

    print("\n5. Reverse Alphabet Square:")
    reverse_alphabet_square(n)


    print("\nInverted Right Triangle:")
    inverted_right_triangle(n)

    print("\nRight Triangle:")
    right_triangle(n)


    print("\n3. Reverse Right Triangle:")
    alphabet_reverse_triangle(n)


    print("\nAlphabet Right Triangle:")
    alphabet_right_triangle(n)

    print("\n2. Inverted Repeated Row Triangle:")
    inverted_repeated_triangle(n)

    print("\n2. Repeated Row Triangle:")
    alphabet_repeated_triangle(n)

    print("\n1. Simple Inverted Number Pyramid:")
    inverted_number_pyramid(n)



    


def square_pattern(n):  # Square pattern
    for i in range(n):
        print("* " * n)


def alphabet_square(n):
    for i in range(n):
        for j in range(n):
            print(chr(65 + j), end=" ")
        print()


def alphabet_row_square(n):
    for i in range(n):
        for j in range(n):
            print(chr(65 + i), end=" ")
        print()


def alphabet_increasing_square(n):  # Increasing Alphabet Square (A, B, C... continuously)
    ch = 65
    for i in range(n):
        for j in range(n):
            print(chr(ch), end=" ")
            ch += 1
            if ch > 90:
                ch = 65
        print()


def hollow_alphabet_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print(chr(65 + j), end=" ")
            else:
                print(" ", end=" ")
        print()


def reverse_alphabet_square(n):
    for i in range(n):
        for j in range(n - 1, -1, -1):
            print(chr(65 + j), end=" ")
        print()


def alphabet_reverse_triangle(n):  # Reverse Right Triangle
    for i in range(n, 0, -1):
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()


def inverted_right_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)


def right_triangle(n):
    for i in range(1, n + 1):
        print("* " * i)


def inverted_repeated_triangle(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print(chr(65 + (n - i)), end=" ")
        print()


def alphabet_right_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(65 + j), end=" ")
        print()


def alphabet_repeated_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print(chr(65 + i), end=" ")
        print()


def inverted_number_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i), end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


def diamond_pattern(n):
    # upper part
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * (2 * i - 1))
    # lower part
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "* " * (2 * i - 1))


def plus_symbol(n):
    for i in range(n):
        for j in range(n):
            if i == n // 2 or j == n // 2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


# Menu function
def main():
    while True:
        print("\n--- Pattern Menu ---")
        print("1. Square Pattern")
        print("2. Alphabet Square")
        print("3. Alphabet Row Square")
        print("4. Increasing Alphabet Square")
        print("5. Hollow Alphabet Square")
        print("6. Reverse Alphabet Square")
        print("7. Right Triangle")
        print("8. Inverted Right Triangle")
        print("9. Alphabet Reverse Triangle")
        print("10. Alphabet Right Triangle")
        print("11. Inverted Repeated Triangle")
        print("12. Alphabet Repeated Triangle")
        print("13. Inverted Number Pyramid")
        print("14. Diamond Pattern")
        print("15. Plus Shape Pattern")
        print("0. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 0:
            print("Exiting... Goodbye!")
            break

        n = int(input("Enter size of pattern (e.g., 5): "))

        if choice == 1:
            square_pattern(n)
        elif choice == 2:
            alphabet_square(n)
        elif choice == 3:
            alphabet_row_square(n)
        elif choice == 4:
            alphabet_increasing_square(n)
        elif choice == 5:
            hollow_alphabet_square(n)
        elif choice == 6:
            reverse_alphabet_square(n)
        elif choice == 7:
            right_triangle(n)
        elif choice == 8:
            inverted_right_triangle(n)
        elif choice == 9:
            alphabet_reverse_triangle(n)
        elif choice == 10:
            alphabet_right_triangle(n)
        elif choice == 11:
            inverted_repeated_triangle(n)
        elif choice == 12:
            alphabet_repeated_triangle(n)
        elif choice == 13:
            inverted_number_pyramid(n)
        elif choice == 14:
            diamond_pattern(n)
        elif choice == 15:
            plus_symbol(n)
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()


    print("\nDiamond Pattern:")
    diamond_pattern(n)

    print("\nPlus Shape Pattern:")
    plus_symbol(n)




if __name__ == "__main__":
    main()

