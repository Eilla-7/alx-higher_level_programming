#!/usr/bin/node
let i;
const times = parseInt(process.argv[2]);
if (!isNaN(times)) {
  for (i = 0; i < times; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
