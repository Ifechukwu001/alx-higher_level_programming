#!/usr/bin/node

const { argv } = require('process');

const args = argv.slice(2);
let biggest = args[0];
let secondBiggest = 0;

if (args.length <= 1) {
  console.log(0);
} else {
  for (let i = 1; i < args.length; i++) {
    if (args[i] > biggest) {
      secondBiggest = biggest;
      biggest = args[i];
    }
  }
  console.log(secondBiggest);
}
