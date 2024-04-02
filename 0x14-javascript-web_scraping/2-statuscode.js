#!/usr/bin/node

// Importing the 'request' module to make HTTP requests
const request = require('request');

// Sending a GET request to the URL provided as the first command line argument
// Using request.get() method to make the GET request
// The response object contains the status code, which is accessed using the 'response' event
request.get(process.argv[2]).on('response', function (response) {
  // Printing the status code of the response
  console.log(`code: ${response.statusCode}`);
});
