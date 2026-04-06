package com.example

class MyClass(private var myString: String) {

    fun getMyString(): String {
        return myString
    }

    fun setMyString(myString: String) {
        this.myString = myString
    }
}

fun main() {
    val myClassInstance = MyClass("helloWorld")
    println(myClassInstance.getMyString())
}
