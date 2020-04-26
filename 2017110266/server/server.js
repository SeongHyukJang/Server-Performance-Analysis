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

            var a_0 = 1;
            var a_n = a_0;
            var count = 0;
            while(count != 10000)
            {
                a_n1 = (a_n/2) +(1/a_n);
                a_n = a_n1;
                count++;
            }
            res.write(a_n.toString());
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