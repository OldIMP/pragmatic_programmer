class MyClass {
    private myString: string;

    constructor(myString: string) {
        this.myString = myString;
    }

    getMyString(): string {
        return this.myString;
    }

    setMyString(myString: string): void {
        this.myString = myString;
    }
}

const myClassInstance = new MyClass("helloWorld");
console.log(myClassInstance.getMyString());
