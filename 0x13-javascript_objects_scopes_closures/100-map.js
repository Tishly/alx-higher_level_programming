#!/usr/bin/node
const list = require('./100-data.js').list;
/*
 * A script that imports an array and computes a new array
 * A new list must be created with each value equal to the
 *value of the initial list, multipled by the index in the list
 * Print both the initial list and the new list
 */

console.log(list);
console.log(list.map((elem, index) => elem * index));
