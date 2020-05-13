const superagent = require('superagent');

var data = '{ "userID" : "2017110266", "usrPW" : "1234", "name" : "JSH", "age" : 25 }';

function callback(error, response, body) {
    if (!error && response.statusCode == 200) {
        console.log(body);
    }
}

superagent.post('http://localhost:8000')
        .set('Content-Type','application/json')
        .send(data)
        .end((err,res)=>{
            if(err){console.log(err);}
        });