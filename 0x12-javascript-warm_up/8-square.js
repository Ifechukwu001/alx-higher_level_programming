#!/usr/bin/node

const { argv } = require('process');

const num = parseInt(argv[2]);

if (isNaN(num)) {
  console.log('Missing size');
} else {
    for (let i = 0; i < num; i++) {
	line = ""
	for (let j = 0; j < num; j++) {
	    line += "X"
	}
	console.log(line);
  }
}
