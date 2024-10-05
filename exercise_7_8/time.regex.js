/**
 * Exercise 8: Implement the time parser using regex & JS.
 */

module.exports = {SyntaxError, parse};

function SyntaxError(message = "The input is not a valid time!") {
    this.name = 'SyntaxError';
    this.message = message;
}

SyntaxError.prototype = Error.prototype;

function parse(input) {
    let result = /(?<hour>\d{1,2})(:(?<min>\d{1,2}))?(?<ampm>(am|pm))?/i.exec(input);
    if (!result) {
        throw new SyntaxError();
    }

    let {hour, min, ampm} = result.groups
    if (!hour) {
        throw new SyntaxError("No hour!");
    }
    if (!min && !ampm) {
        throw new SyntaxError("Just a number!")
    }

    hour = Number(hour);
    let hour24 = 'PM' === ampm?.toUpperCase() ? (hour + 12) : hour;
    if (23 < hour24) {
        throw new SyntaxError("Not a valid hour!");
    }

    min = min ? Number(min) : 0;
    if (59 < min) {
        throw new SyntaxError("Not a valid minute!");
    }

    return hour24 * 60 + min;
}