const today = new Date()
const year = Math.floor(today.getTime()/(60*60*24*365*1000))+1970
console.log(year)