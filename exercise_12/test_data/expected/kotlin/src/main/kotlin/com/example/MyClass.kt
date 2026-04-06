package com.example

class MyClass(private var my_string: String) {

    fun get_my_string(): String {
        return my_string
    }

    fun set_my_string(my_string: String) {
        this.my_string = my_string
    }
}

fun main() {
    val my_class_instance = MyClass("helloWorld")
    println(my_class_instance.get_my_string())
}
