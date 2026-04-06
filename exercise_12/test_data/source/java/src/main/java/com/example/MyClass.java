package com.example;

public class MyClass {
    private String myString;

    public MyClass(String myString) {
        this.myString = myString;
    }

    public String getMyString() {
        return myString;
    }

    public void setMyString(String myString) {
        this.myString = myString;
    }

    public static void main(String[] args) {
        MyClass myClassInstance = new MyClass("helloWorld");
        System.out.println(myClassInstance.getMyString());
    }
}
