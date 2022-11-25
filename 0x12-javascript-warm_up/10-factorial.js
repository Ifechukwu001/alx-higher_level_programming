#!/usr/bin/node

const { argv } = require('process');

const num = Number(argv[2]);

function factorial (number) {
  if (number <= 1) return (1);

  return (number * factorial(number - 1));
}

const result = isNaN(num) ? 1 : factorial(num);
console.log(result);
