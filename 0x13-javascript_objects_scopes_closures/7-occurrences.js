#!/usr/bin/node

/*
 * A function that returns the number of occurrences in a list
 */

exports.nbOccurences = function (list, searchElement) {
  let countNum = 0;
  for (const i of list) {
    if (i === searchElement) {
      countNum = countNum + 1;
    }
  }
return countNum;
};
