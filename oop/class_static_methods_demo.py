class Calculator:
    """
    A class to perform basic arithmetic operations.

    Class Attributes:
    -----------------
    calculation_type : str
        A description of the type of calculations the class performs (default is "Arithmetic Operations").
    """

    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a: float, b: float):
        """
        Adds two numbers.

        Parameters:
        -----------
        a : float
            The first number.
        b : float
            The second number.

        Returns:
        --------
        float
            The sum of the two numbers.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Multiplies two numbers, displaying the calculation type.

        Parameters:
        -----------
        a : float
            The first number.
        b : float
            The second number.

        Returns:
        --------
        float
            The product of the two numbers.

        Prints:
        -------
        str
            The calculation type from the class attribute.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
