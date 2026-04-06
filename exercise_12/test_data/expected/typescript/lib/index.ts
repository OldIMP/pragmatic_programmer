class MyClass {
    private my_string: string;

    constructor(my_string: string) {
        this.my_string = my_string;
    }

    get_my_string(): string {
        return this.my_string;
    }

    set_my_string(my_string: string): void {
        this.my_string = my_string;
    }
}

const my_class_instance = new MyClass("helloWorld");
console.log(my_class_instance.get_my_string());
