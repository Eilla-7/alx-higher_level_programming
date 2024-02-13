#!/usr/bin/node
const times = process.argv[2];
const parse = parseInt(times);
if (!isNaN(parse)) {
  for (let i = 0; i < parse; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
