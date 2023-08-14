#!/usr/bin/node

const args = process.argv;

if ((typeof args[2] === 'undefined') && (typeof args[3] === 'undefined')) {
  console.log('undefined is undefined');
} else if ((typeof args[3] === 'undefined') && (typeof args[2] !== 'undefined')) {
  console.log(`${args[2]} is undefined`);
} else {
  console.log(`${args[2]} is ${args[3]}`);
}
