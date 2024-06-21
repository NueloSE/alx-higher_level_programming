#!/usr/bin/node

exports.converter = function (base) {
  const myConvert = function (num) {
    return num.toString(base);
  };

  return myConvert;
};
