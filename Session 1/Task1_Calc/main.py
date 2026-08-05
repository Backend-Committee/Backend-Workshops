import add
import sub
import mul
import div

print("===== Welcome to the Calculator Program =====")

while True:
    print("\nChoose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Thank you for using the calculator!")
        break

    try:
        # Addition & Multiplication
        if choice in ["1", "3"]:
            numbers = list(map(float, input(
                "Enter numbers separated by spaces: "
            ).split()))

            if choice == "1":
                print("Result:", add.addition(*numbers))

            else:
                print("Result:", mul.mul(*numbers))

        # Subtraction & Division
        elif choice in ["2", "4"]:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "2":
                print("Result:", sub.sub(num1, num2))

            else:
                print("Result:", div.div(num1, num2))

        else:
            print("Invalid choice. Please select from 1 to 5.")

    except ValueError:
        print("Please enter valid numbers.")