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
            fs.readFile('GETdata.json', function(error,data)
            {
                res.write(data);
                res.end();
            })
        }
        if(req.url == "/calc")
        {
            console.log(req.method + " / HTTP/" + req.httpVersion);
            res.writeHead(200);

            let x = 1.0;
            let pi = 1.0;
            let i = 2;
            while(i != 1000000)
            {
                x *= -1;
                pi += x / (2*i -1);
                i++;
            }
            pi *= 4;

            res.write(pi.toString());
            res.end();
        }
        if(req.url == "/html")
        {
            console.log(req.method + " / HTTP/" + req.httpVersion);
            res.writeHead(200,{'Content-Type':'text/html'});
            fs.readFile('GEThtml.html',function(err,data)
            {
                res.write(data);
                res.end()
            })
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
            fs.readFile('POSTdata.json',function(error,data)
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
                fs.writeFileSync('POSTdata.json', JSON.stringify(data,null,4));
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