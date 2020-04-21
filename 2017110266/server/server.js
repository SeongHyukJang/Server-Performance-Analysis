const http = require('http');
const fs = require('fs');
const PORT = 8000;

const server = http.createServer(function(req,res)
{
    if(req.method == "GET")
    {
        if(req.url == "/data")
        {
            console.log(req.method + " / HTTP/" + req.httpVersion);
            res.writeHead(200,{'Content-Type' : 'application/json'});
            fs.readFile('data.json', function(error,data)
            {
                res.write(data);
                res.end();
            })
        }
        if(req.url == "/calc")
        {
            console.log(req.method);
            res.writeHead(200);
            var sum = 0, count = 1;
            while(count <= 100)
            {
                sum += count;
                count++;
            }
            res.end();
        }
    }
    else if(req.method == "POST")
    {   
        console.log(req.method + " / HTTP/" + req.httpVersion);

        var newData;

        req.on('data', function(data)
        {
            newData = data;
        });

        req.on('end', function()
        {
            fs.readFile('data.json',function(error,data)
            {
                newData = JSON.parse(newData);
                if(data.toString() == '')
                {
                    data = JSON.parse('[]');
                    data.push(newData)
                }
                else
                {
                    data = JSON.parse(data);
                    data.push(newData)
                }
                fs.writeFileSync('data.json', JSON.stringify(data,null,4));
                res.writeHead(200);
                res.end();
            })
        })
    }
})

server.listen(PORT,function(error)
{
    console.log("server on PORT " + PORT);
});