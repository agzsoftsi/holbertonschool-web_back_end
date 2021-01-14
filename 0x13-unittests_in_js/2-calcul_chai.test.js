const mocha = require('mocha');
const { expect } = require('chai');

const calculateNumber = require('./1-calcul');

const SUM = 'SUM';
const SUBTRACT = 'SUBTRACT';
const DIVIDE = 'DIVIDE';
const INVALID = 'INVALID';

describe('calculateNumber', () => {
  describe('type SUM', () => {
    it('should return sum of integers', () => {
      expect(calculateNumber('SUM', 1, 3)).to.equal(4);
      expect(calculateNumber(SUM, 2, -2)).to.equal(0);
      expect(calculateNumber(SUM, 1, -4)).to.equal(-3);
    });

    it('should return sum of rounded floats', () => {
      expect(calculateNumber(SUM, 1.4, 5)).to.equal(6);
      expect(calculateNumber(SUM, 1, 4.5)).to.equal(6);
      expect(calculateNumber(SUM, 1.4, 4.5)).to.equal(6);

      expect(calculateNumber(SUM, 8, -8.2)).to.equal(0);
      expect(calculateNumber(SUM, 7.8, -8)).to.equal(0);
      expect(calculateNumber(SUM, 7.8, -8.2)).to.equal(0);

      expect(calculateNumber(SUM, 3, -5.2)).to.equal(-2);
      expect(calculateNumber(SUM, 3.1, -5)).to.equal(-2);
      expect(calculateNumber(SUM, 3.1, -5.2)).to.equal(-2);
    });

    it('should return rounded number if only one is provided', () => {
      expect(calculateNumber(SUM, 8.7)).to.equal(9);
      expect(calculateNumber(SUM, 0.3)).to.equal(0);
      expect(calculateNumber(SUM, -8.7)).to.equal(-9);
    });
  });

  describe('type SUBTRACT', () => {
    it('should return difference of integers', () => {
      expect(calculateNumber(SUBTRACT, 5, 1)).to.equal(4);
      expect(calculateNumber(SUBTRACT, 5, 5)).to.equal(0);
      expect(calculateNumber(SUBTRACT, 1, 5)).to.equal(-4);
    });

    it('should return difference of rounded floats', () => {
      expect(calculateNumber(SUBTRACT, 8.6, 4.1)).to.equal(5);
      expect(calculateNumber(SUBTRACT, 8.6, 4)).to.equal(5);
      expect(calculateNumber(SUBTRACT, 9, 4.1)).to.equal(5);

      expect(calculateNumber(SUBTRACT, 10.2, 9.8)).to.equal(0);
      expect(calculateNumber(SUBTRACT, 10.2, 10)).to.equal(0);
      expect(calculateNumber(SUBTRACT, 10, 9.8)).to.equal(0);

      expect(calculateNumber(SUBTRACT, 8.2, 9.2)).to.equal(-1);
      expect(calculateNumber(SUBTRACT, 8.2, 9)).to.equal(-1);
      expect(calculateNumber(SUBTRACT, 8, 9.2)).to.equal(-1);
    });

    it('should return rounded number if only one is provided', () => {
      expect(calculateNumber(SUBTRACT, 8.7)).to.equal(9);
      expect(calculateNumber(SUBTRACT, 0.3)).to.equal(0);
      expect(calculateNumber(SUBTRACT, -8.7)).to.equal(-9);
    });
  });

  describe('type DIVIDE', () => {
    it('should return quotient of integers', () => {
      expect(calculateNumber(DIVIDE, 9, 4)).to.equal(2.25);
      expect(calculateNumber(DIVIDE, -9, 4)).to.equal(-2.25);
      expect(calculateNumber(DIVIDE, 9, -4)).to.equal(-2.25);
      expect(calculateNumber(DIVIDE, -9, -4)).to.equal(2.25);
    });

    it('should return quotient of non-zero rounded floats', () => {
      expect(calculateNumber(DIVIDE, 1.6, 5.2)).to.equal(0.4);
      expect(calculateNumber(DIVIDE, 1.6, 5)).to.equal(0.4);
      expect(calculateNumber(DIVIDE, 2, 5.2)).to.equal(0.4);

      expect(calculateNumber(DIVIDE, -1.6, 5.2)).to.equal(-0.4);
      expect(calculateNumber(DIVIDE, -1.6, 5)).to.equal(-0.4);
      expect(calculateNumber(DIVIDE, -2, 5.2)).to.equal(-0.4);

      expect(calculateNumber(DIVIDE, 1.6, -5.2)).to.equal(-0.4);
      expect(calculateNumber(DIVIDE, 1.6, -5)).to.equal(-0.4);
      expect(calculateNumber(DIVIDE, 2, -5.2)).to.equal(-0.4);

      expect(calculateNumber(DIVIDE, -1.6, -5.2)).to.equal(0.4);
      expect(calculateNumber(DIVIDE, -1.6, -5)).to.equal(0.4);
      expect(calculateNumber(DIVIDE, -2, -5.2)).to.equal(0.4);
    });

    it('should return 0 if dividend rounds to 0', () => {
      expect(calculateNumber(DIVIDE, 0.3, 3.6)).to.equal(0);
      expect(calculateNumber(DIVIDE, -0.3, 3.6)).to.equal(0);
      expect(calculateNumber(DIVIDE, 0, 3.6)).to.equal(0);
    });

    it('should return "ERROR" if divisor rounds to 0', () => {
      expect(calculateNumber(DIVIDE, 8.4, 0.4)).to.equal('ERROR');
      expect(calculateNumber(DIVIDE, 8.4, -0.4)).to.equal('ERROR');
      expect(calculateNumber(DIVIDE, 8.4, 0)).to.equal('ERROR');
    });
  });

  describe('invalid operation type', () => {
    it('should throw error if type is invalid', () => {
      expect(() => calculateNumber(INVALID, 5.7, 4.6)).to.throw();
    });
  });
});