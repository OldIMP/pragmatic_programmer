package com.example;

public class MyClass {
    private String my_string;

    public MyClass(String my_string) {
        this.my_string = my_string;
    }

    public String get_my_string() {
        return my_string;
    }

    public void set_my_string(String my_string) {
        this.my_string = my_string;
    }

    public static void main(String[] args) {
        MyClass my_class_instance = new MyClass("helloWorld");
        System.out.println(my_class_instance.get_my_string());
    }
}
