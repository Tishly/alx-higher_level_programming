#!/usr/bin/node

/*
 * A script that imports a dictionary of occcurences by user ID and
 *computs a dictionary of the user IDs by occurrence
 */

const dict = require('./101-data.js').dict;

var keys = Object.keys(dict);
keys.sort();

for (var i = 0; i < keys.lenght; i++) {
  var key = keys[i];
  var value = dict[key];

}
