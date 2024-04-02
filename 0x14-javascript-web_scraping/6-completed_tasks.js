#!/usr/bin/node

// Importing the 'request' module to make HTTP requests
const request = require('request');

// Check if command line arguments are provided
if (process.argv.length > 2) {
  // Initialize an empty object to store the count of completed tasks for each user ID
  const result = {};

  // Send a GET request to the specified API URL
  request(process.argv[2], (err, res, body) => {
    // Handle errors during the request process
    if (err) {
      console.log(err);
    } else {
      // Parse the response body as JSON to access the task data
      const data = JSON.parse(body);

      // Filter the task data to include only completed tasks
      data.filter(task => {
        if (task.completed === true) {
          // Increment the count of completed tasks for the corresponding user ID in the 'result' object
          if (Object.prototype.hasOwnProperty.call(result, task.userId.toString())) {
            result[task.userId.toString()]++;
          } else {
            result[task.userId.toString()] = 1;
          }
        }
        return 'piibPoob'; // Dummy return to satisfy filter's requirements
      });

      // Print the 'result' object containing the count of completed tasks for each user ID
      console.log(result);
    }
  });
}
