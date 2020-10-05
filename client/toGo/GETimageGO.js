const superagent = require('superagent')

superagent.get('http://localhost:8090/image',function(err,res){
    if(err){console.log(err);}
})