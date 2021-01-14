function calculateNumber(type, a, b) {
    const a = Math.round(a);
    const b = Math.round(b);
  
    if (type === 'SUBTRACT') {
      return a - b;
    }
  
    if (type === 'DIVIDE') {
      if (b === 0) {
        return 'Error';
      }
      return a / b;
    }
  
    return a + b;
  }
  
  module.exports = calculateNumber;