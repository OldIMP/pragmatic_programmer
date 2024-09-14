let parser = require('./time.js');

function testTime(input, expectedHour, extractedMin = 0) {
    test('parse ' + input, () => {
        expect(parser.parse(input)).toEqual(expectedHour * 60 + extractedMin);
    });
}

testTime('4pm', 16);
testTime('7:38pm', 19, 38);
testTime('23:42', 23, 42);
testTime('3:16', 3, 16);
testTime('3:16am', 3, 16);