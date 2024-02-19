#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length;
  for (let i = 0; i < len / 2; i++) {
    const aux = list[i];
    list[i] = list[len - 1 - i];
    list[len - 1 - i] = aux;
  }
  return list;
};
