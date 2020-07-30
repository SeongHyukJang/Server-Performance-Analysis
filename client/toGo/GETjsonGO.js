const superagent = require('superagent');

superagent.get('http://localhost:8090/json',function(err,res)
{
    if(err){console.log(err);}
})