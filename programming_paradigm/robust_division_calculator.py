def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator/denominator
    except ZeroDivisionError:
        message ="Error: Cannot divide by zero."
    except ValueError:
        message = "Error: Please enter numeric values only."
    else:
        message =f"The result of the division is {result:.1f}"
    finally:
        pass
    print(message)
    return(message)