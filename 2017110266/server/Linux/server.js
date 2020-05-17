const http = require('http');
const fs = require('fs');
const PORT = 8080;

const server = http.createServer(function(req,res)
{
    var startTime, endTime;
    if(req.method == "GET")
    {
        if(req.url == "/json")
        {
            startTime = new Date().getTime();

            console.log(req.method + ' ' + req.url + " / HTTP/" + req.httpVersion);
            res.writeHead(200,{'Content-Type' : 'application/json'});
            fs.readFile('GETdata.json', function(error,data)
            {
                res.write(data);
                res.end();
            })

            endTime = new Date().getTime();
            writeResults(endTime-startTime,'json','GET');
            
        }
        if(req.url == "/calc")
        {
            startTime = new Date().getTime();

            console.log(req.method + ' ' + req.url + " / HTTP/" + req.httpVersion);
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

            endTime = new Date().getTime();
            writeResults(endTime-startTime,'calc','GET');
        }
        if(req.url == "/html")
        {
            startTime = new Date().getTime();

            console.log(req.method + ' ' + req.url + " / HTTP/" + req.httpVersion);
            res.writeHead(200,{'Content-Type':'text/html'});
            fs.readFile('index.html',function(err,data)
            {
                res.write(data);
                res.end()
            })

            endTime = new Date().getTime();
            writeResults(endTime-startTime,'html','GET');
        }
    }
    else if(req.method == "POST")
    {   
        startTime = new Date().getTime()

        console.log(req.method + ' ' + req.url + " / HTTP/" + req.httpVersion);

        var newData;
        req.on('data', function(data)
        {
            newData = data;
        });

        req.on('end', function()
        {
            newData = JSON.parse(newData);

            data = fs.readFileSync('POSTdata.json');
            if(data.toString() == '')
            {
                data = JSON.parse('[]');
            }
            else
            {
                data = JSON.parse(fs.readFileSync('POSTdata.json'));
            }
            
            data.push(newData);
            fs.writeFileSync('POSTdata.json',JSON.stringify(data,null,4));
            res.writeHead(200);
            res.end();
            endTime = new Date().getTime();
            writeResults(endTime-startTime,'json','POST');
        })
    }
})

function writeResults(newData, resource, method)
{
    var data = JSON.parse(fs.readFileSync('serverResults.json'));
    data['ServerLanguage']['javascript'][resource][method].push(newData);
    fs.writeFileSync('serverResults.json',JSON.stringify(data,null,4));
}

server.listen(PORT,function(error)
{
    console.log("server on PORT " + PORT);
});