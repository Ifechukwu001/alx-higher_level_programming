#!/usr/bin/node
// Returns a title from an API

const { argv } = require('node:process');
const request = require('request');

const id = argv[2];

request(`https://swapi-api.hbtn.io/api/films/${id}`, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const jsonResponse = JSON.parse(body);
    console.log(jsonResponse.title);
  }
});
