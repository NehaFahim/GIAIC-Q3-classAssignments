def divide_numbers():
    try:
        a = int(input("Enter first number (numerator): "))
        b = int(input("Enter second number (denominator): "))
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    
    except ValueError:
        print("Error: Please enter valid integers only.")
    
    except Exception as e:
        print("Unexpected error occurred:", e)

    else:
        print("Division successful!")

    finally:
        print("Program finished.")

# Run the function
divide_numbers()
