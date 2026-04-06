#pylint: disable=invalid-name
"""This is the main module."""

class MyClass:
    """This is the `MyClass` docstring."""
    def __init__(self, my_string):
        """This is the `__init__` docstring."""
        self.my_string = my_string

    def get_my_string(self):
        """This is the `get_my_string` docstring."""
        return self.my_string

    def set_my_string(self, my_string):
        """This is the `set_my_string` docstring."""
        self.my_string = my_string

if __name__ == "__main__":
    my_class_instance = MyClass("helloWorld")
    print(my_class_instance.get_my_string())
