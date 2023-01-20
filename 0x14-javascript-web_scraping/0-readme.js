#!/usr/bin/node
/* Ouputs content of a file. */

const { readFile } = require('node:fs');
const { argv } = require('node:process');

const filename = argv[2];

readFile(filename, 'utf8', function (err, data) {
  if (err) { console.log(err); } else { console.log(data); }
});
