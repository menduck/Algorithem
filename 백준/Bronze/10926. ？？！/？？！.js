const fs = require('fs');
const id = fs.readFileSync(0,'utf8').toString().trim(); 

console.log(`${id}??!`);