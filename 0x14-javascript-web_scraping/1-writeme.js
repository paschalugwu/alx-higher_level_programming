#!/usr/bin/node

// Importing the 'fs' module to work with the file system
const fs = require('fs');

// Using fs.writeFile() method to write the string to the file asynchronously
// process.argv[2] contains the file path provided as the first command line argument
// process.argv[3] contains the string to be written provided as the command line argument
// A callback function is provided to handle errors during the writing process
fs.writeFile(process.argv[2], process.argv[3], error => {
  // Printing the error if it exists
  if (error) console.log(error);
});
