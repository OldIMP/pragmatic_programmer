let parser = require('./time.js');

describe("time.js can parse", () => {
    it.each([
        ['4pm', 16],
        ['7:38pm', 19, 38],
        ['23:42', 23, 42],
        ['3:16', 3, 16],
        ['3:16am', 3, 16],

        ['1am', 1],
        ['1pm', 13],
        ['2:30', 2, 30],
        ['14:30', 14, 30],
        ['2:30pm', 14, 30],
    ])
    ("when parsing '%s'", (input, expectedHour, extractedMin = 0) =>
        expect(parser.parse(input)).toEqual(expectedHour * 60 + extractedMin));
});

test('num is invalid', () => expect(() => parser.parse('1')).toThrow(parser.SyntaxError));
