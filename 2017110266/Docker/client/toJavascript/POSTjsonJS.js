var request = require('request');

var headers = {
    'Content-Type': 'application/json'
};

var dataString = '{ "userID" : "2017110266", "usrPW" : "1234", "name" : "JSH", "age" : 25 }';

var options = {
    url: 'http://localhost:8080',
    method: 'POST',
    headers: headers,
    body: dataString
};

function callback(error, response, body) {
    if (!error && response.statusCode == 200) {
        console.log(body);
    }
}

request(options, callback);
