class MyClass {
    constructor(myString) {
        this.myString = myString;
    }

    getMyString() {
        return this.myString;
    }

    setMyString(myString) {
        this.myString = myString;
    }
}

const myClassInstance = new MyClass("helloWorld");
console.log(myClassInstance.getMyString());
