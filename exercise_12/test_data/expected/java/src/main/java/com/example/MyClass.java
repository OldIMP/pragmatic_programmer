package com.example;

/** Example class used by the fixture. */
public final class MyClass {
  /** Stores the current string value. */
  private String my_string;

  /**
   * Creates an instance with an initial value.
   *
   * @param initial_value the starting value
   */
  public MyClass(final String initial_value) {
    this.my_string = initial_value;
  }

  /**
   * Returns the current string value.
   *
   * @return the current value
   */
  public String get_my_string() {
    return my_string;
  }

  /**
   * Updates the current string value.
   *
   * @param updated_value the new value to store
   */
  public void set_my_string(final String updated_value) {
    this.my_string = updated_value;
  }

  /**
   * Runs a small example.
   *
   * @param args unused command-line arguments
   */
  public static void main(final String[] args) {
    MyClass my_class_instance = new MyClass("helloWorld");
    System.out.println(my_class_instance.get_my_string());
  }
}
