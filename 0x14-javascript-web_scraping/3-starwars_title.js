#!/usr/bin/node

// Importing the 'request' module to make HTTP requests
const request = require('request');

// Checking if command line arguments are provided
if (process.argv.length > 2) {
  // Constructing the URL for the Star Wars API endpoint with the movie ID provided as a command line argument
  const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

  // Sending a GET request to the specified URL
  // A callback function is provided to handle the response
  request(url, (err, res, body) => {
    // Error handling: printing the error if an error occurs during the request
    if (err) console.log(err);

    // Parsing the response body as JSON and accessing the 'title' property to retrieve the movie title
    console.log(JSON.parse(body).title);
  });
}
