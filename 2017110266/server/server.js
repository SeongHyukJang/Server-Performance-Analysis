const http = require('http');
const fs = require('fs');
const PORT = 8000;

const server = http.createServer(function(req,res)
{
    var startTime, endTime;
    if(req.method == "GET")
    {
        if(req.url == "/json")
        {
            startTime = new Date().getTime();

            console.log(req.method + " / HTTP/" + req.httpVersion);
            res.writeHead(200,{'Content-Type' : 'application/json'});
            fs.readFile('GETdata.json', function(error,data)
            {
                res.write(data);
                res.end();
            })

            endTime = new Date().getTime();
            writeResults(endTime-startTime,req.headers['user-agent'],'json','GET');
            
        }
        if(req.url == "/calc")
        {
            startTime = new Date().getTime();

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

            endTime = new Date().getTime();
            writeResults(endTime-startTime,req.headers['user-agent'],'calc','GET');
        }
        if(req.url == "/html")
        {
            startTime = new Date().getTime();

            console.log(req.method + " / HTTP/" + req.httpVersion);
            res.writeHead(200,{'Content-Type':'text/html'});
            fs.readFile('GEThtml.html',function(err,data)
            {
                res.write(data);
                res.end()
            })

            endTime = new Date().getTime();
            writeResults(endTime-startTime,req.headers['user-agent'],'html','GET');
        }
    }
    else if(req.method == "POST")
    {   
        startTime = new Date().getTime()

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
            endTime = new Date().getTime();
            writeResults(endTime-startTime, req.headers['user-agent'],'json','POST');
        })
    }
})

function writeResults(newData, userAgent, resource, method)
{
    fs.readFile('serverResults.json',function(error, data)
    {
        var user,resourceIndex;
        data = JSON.parse(data);
        if(userAgent == "python-requests/2.23.0"){user = "python";}
        else if(userAgent == "curl/7.58.0"){user = "curl";}
        else{user = "javascript";}


        data['ServerLanguage']['javascript'][resource][method].push(newData)

        fs.writeFileSync('serverResults.json',JSON.stringify(data,null,4));
    })
}

server.listen(PORT,function(error)
{
    console.log("server on PORT " + PORT);
});