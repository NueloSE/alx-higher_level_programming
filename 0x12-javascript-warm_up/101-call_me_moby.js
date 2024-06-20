#!/usr/bin/node

exports.callMeMoby = function (x, theFunction) {
  x = Number(x);
  for (let i = 0; i < x; i++) {
    theFunction();
  }
};
