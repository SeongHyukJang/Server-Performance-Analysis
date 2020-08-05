const http = require('http');
const fs = require('fs');
const PORT = 8080;

const server = http.createServer(function(req,res)
{
    var startTime, endTime;
    if(req.method == "GET")
    {
        res.writeHead(200);
        if(req.url == "/server-speed/json")
        {
            startTime = process.hrtime();

            console.log(req.method + ' ' + req.url + " / HTTP/" + req.httpVersion);
            res.writeHead(200,{'Content-Type' : 'application/json'});
            fs.readFile('GETdata.json', function(error,data)
            {
                res.write(data);
                res.end();
            })

            endTime = process.hrtime(startTime);
            endTime = Number(endTime[1] * Math.pow(10,-6));
            writeResults(endTime,'json','GET');
        }

        else if(req.url == "/json")
        {
            console.log(req.method + ' ' + req.url + " / HTTP/" + req.httpVersion);
            res.writeHead(200,{'Content-Type' : 'application/json'});
            fs.readFile('GETdata.json', function(error,data)
            {
                res.write(data);
                res.end();
            })
        }

        if(req.url == "/server-speed/calc")
        {
            startTime = process.hrtime();

            console.log(req.method + ' ' + req.url + " / HTTP/" + req.httpVersion);
            res.writeHead(200);

            let x = 1.0;
            let pi = 1.0;
            let i = 2;
            while(i != 100000)
            {
                x *= -1;
                pi += x / (2*i -1);
                i++;
            }
            pi *= 4;

            res.write(pi.toString());
            res.end();

            endTime = process.hrtime(startTime);
            endTime = Number(endTime[1] * Math.pow(10,-6));
            writeResults(endTime,'calc','GET');
        }

        else if(req.url == "/calc")
        {
            console.log(req.method + ' ' + req.url + " / HTTP/" + req.httpVersion);
            res.writeHead(200);

            let x = 1.0;
            let pi = 1.0;
            let i = 2;
            while(i != 10000)
            {
                x *= -1;
                pi += x / (2*i -1);
                i++;
            }
            pi *= 4;

            res.write(pi.toString());
            res.end();
        }
        if(req.url == "/server-speed/html")
        {
            startTime = process.hrtime();

            console.log(req.method + ' ' + req.url + " / HTTP/" + req.httpVersion);
            res.writeHead(200,{'Content-Type':'text/html'});
            fs.readFile('index.html',function(err,data)
            {
                res.write(data);
                res.end()
            })

            endTime = process.hrtime(startTime);
            endTime = Number(endTime[1] * Math.pow(10,-6));
            writeResults(endTime,'html','GET');
        }
        else if(req.url == "/html")
        {
            console.log(req.method + ' ' + req.url + " / HTTP/" + req.httpVersion);
            res.writeHead(200,{'Content-Type':'text/html'});
            fs.readFile('index.html',function(err,data)
            {
                res.write(data);
                res.end()
            });
        }
    }
    else if(req.method == "POST")
    {   
        if(req.url == "/server-speed/post")
        {
            startTime = process.hrtime();
            console.log(req.method + ' ' + req.url + " / HTTP/" + req.httpVersion);

            var newData;
            req.on('data', function(data)
            {
                newData = data;
            });

            req.on('end', function()
            {
                newData = JSON.parse(newData);

                data = fs.readFileSync('POSTdataJS.json');
                if(data.toString() == '')
                {
                    data = JSON.parse('[]');
                }
                else
                {
                    data = JSON.parse(fs.readFileSync('POSTdataJS.json'));
                }
                
                data.push(newData);
                fs.writeFileSync('POSTdataJS.json',JSON.stringify(data,null,4));
                res.writeHead(200,{'Content-Type' : 'application/json'});
                res.end();

                endTime = process.hrtime(startTime);
                endTime = Number(endTime[1] * Math.pow(10,-6));
                writeResults(endTime,'json','POST');
            })
        }
        else
        {
            console.log(req.method + ' ' + req.url + " / HTTP/" + req.httpVersion);

            var newData;
            req.on('data', function(data)
            {
                newData = data;
            });

            req.on('end', function()
            {
                newData = JSON.parse(newData);

                data = fs.readFileSync('POSTdataJS.json');
                if(data.toString() == '')
                {
                    data = JSON.parse('[]');
                }
                else
                {
                    data = JSON.parse(fs.readFileSync('POSTdataJS.json'));
                }
                
                data.push(newData);
                fs.writeFileSync('POSTdataJS.json',JSON.stringify(data,null,4));
                res.writeHead(200,{'Content-Type' : 'application/json'});
                res.end();
            })
        }
    }
})

function writeResults(newData, resource, method)
{
    var data = JSON.parse(fs.readFileSync('ServerSpeedResult.json'));
    data['ServerLanguage']['javascript'][resource][method].push(newData);
    fs.writeFileSync('ServerSpeedResult.json',JSON.stringify(data,null,4));
}

server.listen(PORT,function(error)
{
    console.log("server on PORT " + PORT);
});