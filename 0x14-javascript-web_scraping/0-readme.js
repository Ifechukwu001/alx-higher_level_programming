#!/usr/bin/node
/* Ouputs content of a file. */

const fs = require('node:fs');
const { argv } = require('node:process');

const filename = argv[2];

fs.readFile(filename, 'utf8', function (err, data) {
  if (err) { console.log(err); } else { console.log(data); }
});