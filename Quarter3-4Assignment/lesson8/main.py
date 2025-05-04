import calculator  

def main():
    print("Simple Calculator using Functions and Modules")
    
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    
    print("Addition:", calculator.add(x, y))
    print("Subtraction:", calculator.subtract(x, y))
    print("Multiplication:", calculator.multiply(x, y))
    print("Division:", calculator.divide(x, y))

if __name__ == "__main__":
    main()
