#!/usr/bin/node

exports.logMe = (function (item) {
  let currArg = -1;
  return function (item) {
    currArg++;
    console.log(currArg + ': ' + item);
  };
})();
