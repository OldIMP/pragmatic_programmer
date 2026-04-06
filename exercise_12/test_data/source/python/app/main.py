#pylint: disable=invalid-name
"""This is the main module."""

class MyClass:
    """This is the `MyClass` docstring."""
    def __init__(self, myString):
        """This is the `__init__` docstring."""
        self.myString = myString

    def getMyString(self):
        """This is the `getMyString` docstring."""
        return self.myString

    def setMyString(self, myString):
        """This is the `setMyString` docstring."""
        self.myString = myString

if __name__ == "__main__":
    myClassInstance = MyClass("helloWorld")
    print(myClassInstance.getMyString())
