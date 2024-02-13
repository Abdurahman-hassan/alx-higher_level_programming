#!/usr/bin/node

// Include the filesystem module
const fs = require('fs');

// Grab command-line arguments for file paths
const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const fileCPath = process.argv[4];

// Read the content of the first file
fs.readFile(fileAPath, 'utf8', (err, dataA) => {
  if (err) throw err;

  // Read the content of the second file
  fs.readFile(fileBPath, 'utf8', (err, dataB) => {
    if (err) throw err;

    // Concatenate the content of both files
    const concatenatedData = dataA + '\n' + dataB;

    // Write the concatenated content to the destination file
    fs.writeFile(fileCPath, concatenatedData, (err) => {
      if (err) throw err;
    });
  });
});
