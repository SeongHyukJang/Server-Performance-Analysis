const EventEmitter = require('events');

console.log(__filename);
console.log(__dirname);

var url =  'http://www.khu.ac.kr';

class Logger extends EventEmitter
{
    log(msg)
    {
        // Send an HTTP request
        console.log(msg);

        // Raise an event
        this.emit('messageLogged', {id : 1, url : 'https://www.khu.ac.kr'});
    }
}

//module.exports.Log = log;
module.exports = Logger;
//module.exports.url = url;