const calculateNumber = require("./1-calcul.js");
const assert = require("assert");

describe('SUM', () => {
  it('returns rounded positive sum', () => {
    assert.strictEqual(calculateNumber('SUM', 6.1, 6.1), 12);
    assert.strictEqual(calculateNumber('SUM', 0.1, 0.2), 0);
    assert.strictEqual(calculateNumber('SUM', 0.1, 0.6), 1);
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
    assert.strictEqual(calculateNumber('SUM', 4, 8), 12);
    assert.strictEqual(calculateNumber('SUM', 1.9, 0), 2);
   
  });

  it('returns rounded negative sum', () => {
    assert.strictEqual(calculateNumber('SUM', -1, -3), -4);
    assert.strictEqual(calculateNumber('SUM', -1.4, -3.6), -5);
  });

  it('returns TypeError', () => {
    assert.throws(() => calculateNumber('SUM', NaN, NaN), { name: 'TypeError' });
    assert.throws(() => calculateNumber('SUM', NaN, 5.6), { name: 'TypeError' });
    assert.throws(() => calculateNumber('SUM', 5.6, NaN), { name: 'TypeError' });
  });
});

describe('SUBTRACT', () => {
  it('returns rounded positive substract', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 0.6, 0.1), 1);
    assert.strictEqual(calculateNumber('SUBTRACT', 4.5, 1.4), 4);
    assert.strictEqual(calculateNumber('SUBTRACT', 8, 4), 4);
    assert.strictEqual(calculateNumber('SUBTRACT', 1.9, 0), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', 6.1, 6.1), 0);
    assert.strictEqual(calculateNumber('SUBTRACT', 1, 0.2), 1);
  });

  it('returns rounded negative substract', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', -1, -3), 2);
    assert.strictEqual(calculateNumber('SUBTRACT', -1.4, -3.6), 3);
  });

  it('returns TypeError', () => {
    assert.throws(() => calculateNumber('SUBTRACT', NaN, 5.6), { name: 'TypeError' });
    assert.throws(() => calculateNumber('SUBTRACT', 5.6, NaN), { name: 'TypeError' });
    assert.throws(() => calculateNumber('SUBTRACT', NaN, NaN), { name: 'TypeError' });
  });
});

describe('DIVIDE', () => {
  it('returns rounded positive divide', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 0.6, 0.9), 1);
    assert.strictEqual(calculateNumber('DIVIDE', 8, 4), 2);
    assert.strictEqual(calculateNumber('DIVIDE', 6.1, 1.7), 3);
    assert.strictEqual(calculateNumber('DIVIDE', 6.1, 6.1), 1);
    assert.strictEqual(calculateNumber('DIVIDE', 2.0, 1.1), 2);
    assert.strictEqual(calculateNumber('DIVIDE', 4.5, 5), 1);
  });

  it('returns rounded negative divide', () => {
    assert.strictEqual(calculateNumber('DIVIDE', -2, 1.1), -2);
    assert.strictEqual(calculateNumber('DIVIDE', -4.4, -2.2), 2);
  });

  it('returns Error', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 2, 0), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 3, 0), 'Error');
    assert.strictEqual(calculateNumber('DIVIDE', 4, 0), 'Error');
  });

  it('returns TypeError', () => {
    assert.throws(() => calculateNumber('DIVIDE', NaN, 5.6), { name: 'TypeError' });
    assert.throws(() => calculateNumber('DIVIDE', 5.6, NaN), { name: 'TypeError' });
    assert.throws(() => calculateNumber('DIVIDE', NaN, NaN), { name: 'TypeError' });
  });
});