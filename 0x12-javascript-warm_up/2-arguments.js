#!/usr/bin/node

let myVar = process.argv.forEach((index) => {
  myVar = index + 1;
});

if (myVar === 0) {
  console.log('No argument');
}
if (myVar === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
