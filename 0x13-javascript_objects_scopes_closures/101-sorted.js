#!/usr/bin/node
/*
Your script must import dict from the file 101-data.js
In the new dictionary:
A key is a number of occurrences
A value is the list of user ids
Print the new dictionary at the end
*/
const occurence = require('./101-data').dict;
const newDict = {};
for (const key in occurence) {
  if (newDict[occurence[key]] === undefined) {
    newDict[occurence[key]] = [];
  }
  newDict[occurence[key]].push(key);
}
console.log(newDict);
