const superagent = require('superagent');

superagent.get('http://localhost:8000/json',function(err,res)
{
    if(err){console.log(err);}
})