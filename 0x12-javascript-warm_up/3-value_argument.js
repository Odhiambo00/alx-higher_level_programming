#!/usr/bin/node

const args = process.argv;

console.log(typeof args[2] === 'undefined' ? 'No argument' : args[2]);
