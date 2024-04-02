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
    if (err) {
      console.log(err);
    } else {
      // Parsing the response body as JSON to access the movie data
      const movie = JSON.parse(body);

      // Mapping over the characters array of the movie to retrieve character details
      movie.characters.map(char => {
        // Sending a GET request to the character URL
        request(char, (err, res, body) => {
          // Error handling: printing the error if an error occurs during the request
          if (err) {
            console.log(err);
          } else {
            // Parsing the response body as JSON and printing the character name
            console.log(JSON.parse(body).name);
          }
        });
        return (char); // Dummy return to satisfy map's requirements
      });
    }
  });
}
