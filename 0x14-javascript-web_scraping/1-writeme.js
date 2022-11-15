#!/usr/bin/node
/* Writes a string to a file */

const { writeFile } = require('node:fs');
const { argv } = require('node:process');

const filepath = argv[2];
const data = argv[3];

writeFile(filepath, data, 'utf8', (err) => {
  if (err) { console.log(err); }
});
