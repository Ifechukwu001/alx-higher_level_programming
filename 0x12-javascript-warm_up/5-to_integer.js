#!/usr/bin/node

const { argv } = require('process');

const resultNum = parseInt(argv[2]);

if (isNaN(resultNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + resultNum);
}
