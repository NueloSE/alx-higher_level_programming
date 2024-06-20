#!/usr/bin/node

exports.addMeMaybe = function (x, theFunction) {
  x = Number(x);
  theFunction(x + 1);
};
