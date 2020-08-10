const add = require("../src/calculator");

test('should return 0 if empty string provided', () => {
    expect(add('')).toBe(0);
  });