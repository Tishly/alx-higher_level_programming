#!/usr/bin/node

/*
 * A script that prints a factorial
 */

const varFact = process.argv[2];

function fact (num) {
  if (isNaN(num) === true) {
    num = 1;
    return (num);
  } else if (isNaN(num) === false) {
    for (let i = 1; i <= num; i++) {
      num = num * i;
    }
    return (parseInt(num));
  }
}
console.log(fact(varFact));
