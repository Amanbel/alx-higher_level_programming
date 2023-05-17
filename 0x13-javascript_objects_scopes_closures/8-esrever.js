#!/usr/bin/node

exports.esrever = function (list) {
  const count = list.length - 1;
  const rev = [];
  let j = 0;
  for (let i = count; i >= 0; i--) {
    rev[j] = list[i];
    j++;
  }
  return rev;
};
