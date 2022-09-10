#!/usr/bin/node

/*
 * A function that prints the number of arguments
 *already printed and the new argument value
 */
let i = 0;
exports.logMe = function (item) {
  if (item) {
    console.log(i + ': ' + item);
    ++i;
  }
};
