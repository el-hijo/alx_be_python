class Calculator:
    calculation_type = "Arithmetic operations"
    
    @staticmethod
    def add(a,b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        print(f"Calcutlation type: {cls.calculation_type}")
        return a * b