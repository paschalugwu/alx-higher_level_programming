#!/usr/bin/node

// Importing the 'fs' module to work with the file system
const fs = require('fs');

// Importing the 'request' module to make HTTP requests
const request = require('request');

// Sending a GET request to the specified URL and piping the response to a writable stream
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
