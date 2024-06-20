#!/usr/bin/node

exports.esrever = function (list) {
  const result = [];
  let i = (list.length) - 1;
  for (let j = 0; j < list.length && i >= 0; j++, i--) {
    result[j] = list[i];
  }
  return result;
};
