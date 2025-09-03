def reverse_number(n: int) -> int:
    """Return the reverse of a number."""
    return int(str(n)[::-1])


def fibonacci_series(limit: int) -> list:
    """Return Fibonacci series up to 'limit' terms."""
    series = [0, 1]
    while len(series) < limit:
        series.append(series[-1] + series[-2])
    return series[:limit]


def multiplication_table(n: int) -> list:
    """Return multiplication table for a number."""
    return [f"{n} x {i} = {n * i}" for i in range(1, 11)]


def square_properties(side: float) -> tuple:
    """Return perimeter and area of a square."""
    perimeter = 4 * side
    area = side * side
    return perimeter, area


def alphabet_pyramid_left(rows: int) -> str:
    result = ""
    for i in range(rows):
        result += " ".join(chr(65 + j) for j in range(i + 1)) + "\n"
    return result


def alphabet_pyramid_center(rows: int) -> str:
    result = ""
    for i in range(rows):
        result += " " * (rows - i - 1)
        result += " ".join(chr(65 + j) for j in range(i + 1))
        result += "\n"
    return result


def alphabet_pyramid_symmetric(rows: int) -> str:
    result = ""
    for i in range(rows):
        left = "".join(chr(65 + j) for j in range(i + 1))
        right = left[:-1][::-1]  # mirror except last char
        result += " " * (rows - i - 1) + left + right + "\n"
    return result


def pyramid_menu():
    print("\nChoose Pyramid Type:")
    print("1. Left Pyramid")
    print("2. Centered Pyramid")
    print("3. Symmetric Pyramid")

    choice = input("Enter your choice (1-3): ")
    rows = int(input("Enter number of rows: "))

    if choice == "1":
        print(alphabet_pyramid_left(rows))
    elif choice == "2":
        print(alphabet_pyramid_center(rows))
    elif choice == "3":
        print(alphabet_pyramid_symmetric(rows))
    else:
        print("Invalid choice!")


def main():
    while True:
        print("\n--- PYTHON   PROJECT ---")
        print("1. Reverse a Number")
        print("2. Fibonacci Series")
        print("3. Multiplication Table")
        print("4. Perimeter & Area of Square")
        print("5. Alphabet Pyramid Pattern")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            num = int(input("Enter a number: "))
            print("Reversed Number:", reverse_number(num))

        elif choice == "2":
            terms = int(input("Enter number of terms: "))
            print("Fibonacci Series:", fibonacci_series(terms))

        elif choice == "3":
            num = int(input("Enter a number: "))
            print("\n".join(multiplication_table(num)))

        elif choice == "4":
            side = float(input("Enter side length of square: "))
            perimeter, area = square_properties(side)
            print(f"Perimeter: {perimeter}, Area: {area}")

        elif choice == "5":
            pyramid_menu()

        elif choice == "6":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
