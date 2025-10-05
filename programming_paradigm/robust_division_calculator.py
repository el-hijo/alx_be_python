def safe_divide(float(numerator), float(denominator)):
    try:
        result = numerator/denominator
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    else:
        print(f"The result of the division is {result}")
    finally:
        print("Finished.")