from calculator import (
    add,
    subtract,
    multiply,
    divide,
    InvalidOperationError
)


def show_menu():
    print("\nCalculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")


def main():

    while True:

        try:
            show_menu()

            choice = input("Choose operation (1-4): ")

            if choice not in ["1", "2", "3", "4"]:
                raise InvalidOperationError("Invalid operation choice")

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))


            if choice == "1":
                result = add(num1, num2)

            elif choice == "2":
                result = subtract(num1, num2)

            elif choice == "3":
                result = multiply(num1, num2)

            elif choice == "4":
                result = divide(num1, num2)


            print("Result =", result)


        except ValueError:
            print("Please enter valid numbers.")

        except ZeroDivisionError as e:
            print(e)

        except InvalidOperationError as e:
            print(e)


        again = input("\nDo you want to continue? (y/n): ")

        if again.lower() != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()