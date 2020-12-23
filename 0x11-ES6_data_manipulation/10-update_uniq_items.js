function updateUniqueItems(map) {
  if (!(map instanceof Map)) {
    throw Error('Cannot process');
  }

  for (const [key] of map) {
    if (map.get(key) === 1) map.set(key, 100);
  }

  return map;
}

export default updateUniqueItems;
