package com.example;

/** Example class used by the fixture. */
public final class MyClass {
  /** Stores the current string value. */
  private String myString;

  /**
   * Creates an instance with an initial value.
   *
   * @param initialValue the starting value
   */
  public MyClass(final String initialValue) {
    this.myString = initialValue;
  }

  /**
   * Returns the current string value.
   *
   * @return the current value
   */
  public String getMyString() {
    return myString;
  }

  /**
   * Updates the current string value.
   *
   * @param updatedValue the new value to store
   */
  public void setMyString(final String updatedValue) {
    this.myString = updatedValue;
  }

  /**
   * Runs a small example.
   *
   * @param args unused command-line arguments
   */
  public static void main(final String[] args) {
    MyClass myClassInstance = new MyClass("helloWorld");
    System.out.println(myClassInstance.getMyString());
  }
}
