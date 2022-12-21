#!/usr/bin/node

exports.converter = function (base) {
  function baseConvertor (num) {
    return num.toString(base);
  }
  return baseConvertor;
};
