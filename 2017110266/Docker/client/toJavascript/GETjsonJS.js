const superagent = require('superagent');

superagent.get('http://localhost:8080/json',function(err,res)
{
    if(err){console.log(err);}
})