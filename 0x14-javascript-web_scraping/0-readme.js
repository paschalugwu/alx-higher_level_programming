#!/usr/bin/node

// Importing the 'fs' module to work with the file system
const fs = require('fs');

// Using fs.readFile() method to read the content of the file asynchronously
// process.argv[2] contains the file path provided as the first command line argument
// 'utf8' specifies the encoding of the file content to be read
// A callback function is provided to handle errors and content retrieval
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // Printing the error if it exists, otherwise printing the file content
  console.log(error || content);
});
