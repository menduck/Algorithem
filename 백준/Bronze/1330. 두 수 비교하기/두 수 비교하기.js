const fs = require('fs');
const inputData = fs.readFileSync(0,'utf8').toString().split(" ");

const A = Number(inputData[0]);
const B = Number(inputData[1]);

if (A > B) {
    console.log (">");
} else if (A < B) {
    console.log("<");
} else {
    console.log("==");
}