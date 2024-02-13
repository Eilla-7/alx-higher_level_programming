#!/usr/bin/node
const number = process.argv[2];
const parse = parseInt(number);
if (!isNaN(number)) {
  console.log('My number:', parse);
} else {
  console.log('Not a number');
}
