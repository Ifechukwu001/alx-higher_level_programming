#!/usr/bin/node
/* Displays status code */

const { argv } = require('node:process');
const request = require('request');

const url = argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log(`code: ${response.statusCode}`);
});
