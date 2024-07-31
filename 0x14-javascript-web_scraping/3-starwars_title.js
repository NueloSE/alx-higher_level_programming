#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;
let res;
request.get(url, (error, response, body) => {
  if (error) { return; }
  res = JSON.parse(body);
  console.log(res.title);
});
