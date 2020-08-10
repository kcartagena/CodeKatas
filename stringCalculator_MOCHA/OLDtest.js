//beforEach() and it() should have been nested inside describe()
describe('String Calculator', function() {
    var calculator;

});

beforeEach(function(){
    calculator = stringCalculator();

});

it("empty string", function() {
    expect(calculator.value()).toEqual(0)
});

it('can take one value', function() {
    calculator.add(1);
    expect(calculator.value()).toEqual(2);
});

it('can take two values', function() {
    calculator.add(1);
    calculator.add(2);
    expect(calculator.value()).toEqual(3);
});

it('can take unknown amount of values', function() {
    calculator.add(1);
    calculator.add(2);
    calculator.add(3);
    calculator.add(4);
    expect(calculator.value()).toEqual(10); 
});
