describe.each([['Peggy parser', require('./time.js')], ['Regex Parser', require('./time.regex.js')]])
("%s", (name, parser) => {
    it.each([
        // from Exercise 7
        ['4pm', 16],
        ['7:38pm', 19, 38],
        ['23:42', 23, 42],
        ['3:16', 3, 16],
        ['3:16am', 3, 16],
        // from Answer 7
        ['1am', 1],
        ['1pm', 13],
        ['2:30', 2, 30],
        ['14:30', 14, 30],
        ['2:30pm', 14, 30],
    ])
    ("should parse '%s'", (input, expectedHour, expectedMin = 0) =>
        expect(parser.parse(input)).toEqual(expectedHour * 60 + expectedMin));

    it.each(['1', ':30pm', '13:24pm', '1:60', '13pm', '01:60am'])
    ("should not parse '%s'", input => expect(() => parser.parse(input)).toThrow(parser.SyntaxError));
});
