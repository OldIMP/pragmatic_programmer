/**
 * Exercise 8: Implement the time parser using regex & JS.
 */

module.exports = { TimeSyntaxError, parse };

function TimeSyntaxError(message = "The input is not a valid time!") {
  this.name = "TimeSyntaxError";
  this.message = message;
}

TimeSyntaxError.prototype = Error.prototype;

function parse(input) {
  let result = /(?<hour>\d{1,2})(:(?<min>\d{1,2}))?(?<ampm>(am|pm))?/i.exec(
    input,
  );
  if (!result) {
    throw new TimeSyntaxError();
  }

  let { hour, min, ampm } = result.groups;
  if (!hour) {
    throw new TimeSyntaxError("No hour!");
  }
  if (!min && !ampm) {
    throw new TimeSyntaxError("Just a number!");
  }

  hour = Number(hour);
  let hour24 = "PM" === ampm?.toUpperCase() ? hour + 12 : hour;
  if (23 < hour24) {
    throw new TimeSyntaxError("Not a valid hour!");
  }

  min = min ? Number(min) : 0;
  if (59 < min) {
    throw new TimeSyntaxError("Not a valid minute!");
  }

  return hour24 * 60 + min;
}
