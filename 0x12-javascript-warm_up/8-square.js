#!/usr/bin/node
const size = process.argv[2];
const parse = parseInt(size);
if (!isNaN(parse)) {
  for (let r = 0; r < parse; r++) {
    for (let row = 0; row < parse; row++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
