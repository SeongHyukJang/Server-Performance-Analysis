const superagent = require('superagent');

superagent.get('http://localhost:8080/html',function(err,res)
{
    if(err){console.log(err);}
})