#!/usr/bin/env node

"user strict";

const path = require("path");
const fs = require("fs");
const minimist = require("minimist");
const { Transform } = require("stream");

const BASE_PATH = path.resolve(process.env.BASE_PATH || __dirname);
const OUT_PATH = path.join(BASE_PATH, "out.txt");

const args = minimist(process.argv.slice(2), {
  boolean: ["help"],
  string: ["file"]
});

if (args.input || args._.includes("-")) {
  processFile(process.stdin);
} else if (args.file) {
  const filePath = path.join(BASE_PATH, args.file);
  processFile(fs.createReadStream(filePath));
}

function processFile(inputStream) {
  let stream = inputStream;
  let outStream;

  const upperCaseTrans = new Transform({
    transform(chunk, encoding, callback) {
      this.push(chunk.toString().toUpperCase());
      callback();
    }
  });

  stream = stream.pipe(upperCaseTrans);
  outStream = fs.createWriteStream(OUT_PATH);
  stream.pipe(outStream);
}
