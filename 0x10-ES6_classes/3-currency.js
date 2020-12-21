class Currency {
  constructor(code, name) {
    this.code = code;
    this.name = name;
  }

  get code() {
    return this._code;
  }

  set code(code) {
    if (typeof code === 'string') this._code = code;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name === 'string') this._name = name;
  }

  displayFullCurrency() {
    return `${this.name} (${this.code})`;
  }
}

export default Currency;
