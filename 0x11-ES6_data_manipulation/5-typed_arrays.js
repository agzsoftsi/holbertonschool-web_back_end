function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer, 0);

  if (position > length - 1) {
    throw Error('Position outside range');
  }

  view.setInt8(position, value);

  return view;
}

export default createInt8TypedArray;
