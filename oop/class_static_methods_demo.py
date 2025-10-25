class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
class Math:
    calculation_type = "Arithmetic Operations"

    @classmethod
    def multiply(cls, a, b):
        print("Calculation Type:", cls.calculation_type)  # 👈 using the class attribute
        return a * b
