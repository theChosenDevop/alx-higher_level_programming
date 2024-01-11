#!/usr/bin/node
/* A script that concats 2 files. */
const fs = require('fs');

const srcFile1 = process.argv[2];
const srcFile2 = process.argv[3];
const srcFile3 = process.argv[4];

function concatFiles (file1, file2, dest) {
  /* concatenates file1 and file2 and writes into dest */
  const content1 = fs.readFileSync(file1, 'utf8');
  const content2 = fs.readFileSync(file2, 'utf8');

  const result = content1 + content2;

  fs.writeFileSync(dest, result);
}

concatFiles(srcFile1, srcFile2, srcFile3);
