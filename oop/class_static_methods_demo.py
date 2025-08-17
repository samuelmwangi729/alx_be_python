# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: Does not depend on class or instance.
        Simply adds two numbers.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: Has access to class-level attributes via 'cls'.
        Prints calculation_type before performing multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
