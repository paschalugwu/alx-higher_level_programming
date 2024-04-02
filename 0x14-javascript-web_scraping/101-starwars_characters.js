#!/usr/bin/node

// Importing the 'request' module to make HTTP requests
const request = require('request');

// Check if command line arguments are provided
if (process.argv.length > 2) {
  // Construct the URL for the Star Wars API endpoint with the movie ID provided as a command line argument
  const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

  // Sending a GET request to the specified URL
  request(url, (err, res, body) => {
    // Error handling: printing the error if an error occurs during the request
    if (err) {
      console.log(err);
    } else {
      // Parsing the response body as JSON to access the movie data
      const movie = JSON.parse(body);

      // Map over the characters array of the movie to retrieve character details
      const namesPromises = movie.characters.map(char =>
        // Creating a promise for each character to handle the request
        new Promise((resolve, reject) => {
          // Sending a GET request to the character URL
          request(char, (err, res, body) => {
            // Error handling: rejecting the promise if an error occurs during the request
            if (err) {
              reject(err);
            } else {
              // Resolving the promise with the character's name parsed from the response body
              resolve(JSON.parse(body).name);
            }
          });
        })
      );

      // Using Promise.all() to handle all promises concurrently and wait for all requests to complete
      Promise.all(namesPromises).then(names => console.log(names.join('\n')));
    }
  });
}
