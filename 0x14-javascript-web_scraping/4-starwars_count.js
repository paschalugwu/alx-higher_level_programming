#!/usr/bin/node

// Importing the 'request' module to make HTTP requests
const request = require('request');

// Sending a GET request to the specified Star Wars API URL
request(process.argv[2], function (error, response, body) {
  // Checking if there are no errors during the request process
  if (!error) {
    // Parsing the response body as JSON and accessing the 'results' property
    const results = JSON.parse(body).results;

    // Filtering the movies to count the number of movies where "Wedge Antilles" is present
    const count = results.reduce((count, movie) => {
      // Checking if "Wedge Antilles" character ID (18) is present in the characters array of the movie
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1 // Incrementing the count if "Wedge Antilles" is found in the characters array
        : count; // Keeping the count unchanged if "Wedge Antilles" is not found
    }, 0);

    // Printing the total count of movies where "Wedge Antilles" is present
    console.log(count);
  }
});
