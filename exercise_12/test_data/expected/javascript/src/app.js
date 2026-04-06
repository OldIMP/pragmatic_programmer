class MyClass {
    constructor(my_string) {
        this.my_string = my_string;
    }

    get_my_string() {
        return this.my_string;
    }

    set_my_string(my_string) {
        this.my_string = my_string;
    }
}

const my_class_instance = new MyClass("helloWorld");
console.log(my_class_instance.get_my_string());
