#SRE Task

This task is done by Python's framework, Flask, and the monitoring tool are Prometheus and Grafana.

The OS system I used is Mac OS. I'll introduce how to use the web service at below.

##Web service 

###Running Environment

Mac OS

Python 3.4+

Flask 1.1.1

prometheus_client

Virtual environment

###Quick Start
```bash
cd SRETask
virtualenv -p python venv
source venv/bin/activate
pip install flask
pip install prometheus_client
cd Task
python FlaskApi.py
```

###How to use 


#####Use the function name as endPoint
   
 Method: GET  
   
 Possible Status Code: 200, 500, 404, 405
   
 Example of input: ```http GET http://127.0.0.1:8000/fibonacci/12```
   
 Example of input: ```http GET http://127.0.0.1:8000/ackermann/1/2```
   
 Example of input: ```http GET http://127.0.0.1:8000/factorial/12```
```
GET /fibonacci/12 HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
User-Agent: PostmanRuntime/7.17.1
Accept: */*
Cache-Control: no-cache
Postman-Token: 0681ff36-dc38-4223-a9e5-3f9481c1140c,ff8e0c53-ad41-4f51-829c-a7b70f47db00
Host: 127.0.0.1:5000
Accept-Encoding: gzip, deflate
Connection: keep-alive
cache-control: no-cache
```
   Example of output:
```
"144"
```

#####Use the payload to pass the factors

 Method: POST

 Possible Status Code: 200, 500, 404, 405
 
 Example of input: ```http POST http://127.0.0.1:8000/calculator```
 
```
POST /calculator HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
User-Agent: PostmanRuntime/7.17.1
Accept: */*
Cache-Control: no-cache
Postman-Token: 924b9266-a979-427e-87f4-ffba12e6ad7f,5df563c8-aa52-4781-8b05-298f1751719f
Host: 127.0.0.1:5000
Accept-Encoding: gzip, deflate
Content-Length: 42
Connection: keep-alive
cache-control: no-cache

{
    "Function":"fibonacci", 
	"FactorN":3
}
```
 Example of output:
 ```
 "2"
 ```

#####Use the query to pass the factors

 Method: GET

 Possible Status Code: 200, 500, 404, 405

 Example of input: ```http GET http://127.0.0.1:5000/calculator?m=20&n=14&function=fibonacci```

```
GET /calculator?m=20&amp; n=14&amp; function=fibonacci HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
User-Agent: PostmanRuntime/7.17.1
Accept: */*
Cache-Control: no-cache
Postman-Token: e43e4dfa-4845-4925-a161-6bee30ccd496,e6e61e68-5e01-4f5b-a5ae-6549e6fcd4b5
Host: 127.0.0.1:5000
Accept-Encoding: gzip, deflate
Connection: keep-alive
cache-control: no-cache
```
Example of output:
```
"377"
```

#####Use the header to pass the factors

 Method: GET  
 
 Possible Status Code: 200, 500, 404, 405
 
 Example of input: ```http GET http://127.0.0.1:5000/HeaderCalculator```	
```
GET /HeaderCalculator HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/json
Function: fibonacci
FactorN: 2
FactorM: 1
User-Agent: PostmanRuntime/7.17.1
Accept: */*
Cache-Control: no-cache
Postman-Token: 9af43d67-df7a-4f00-8c93-4c9ef332bfc3,a886fca1-b83a-485f-bbe3-7c83d9685834
Host: 127.0.0.1:5000
Accept-Encoding: gzip, deflate
Connection: keep-alive
cache-control: no-cache
```
   Example of output:
```
"1"
```

##Monitoring

###Running Environment

Mac OS

Prometheus

Grafana

### Quick Start

#### Prometheus

Please follow the page ```https://prometheus.io/docs/introduction/first_steps/``` to install the Prometheus.

#### Grafana

Please follow the page ```https://grafana.com/docs/installation/mac/``` to install the Grafana.

#### How to use 

After install the Prometheus, open the config.file ```prometheus.yml``` and modify the scrape_configs part as below.

```
  - job_name: 'api_monitor'
    scrape_interval: 5s
    static_configs:
        - targets: ['localhost:5000']
``` 

Use ```./prometheus --config.file=prometheus.yml``` to start the Prometheus and collect the data.
Now, you should be able to see the data via ```https://localhost:9090```, which is only recording the request times and status.
After open th page, you could go to the data collecting dashboard to see the data.
Please be reminded, in the data dashboard there will have different kinds of option in default.
You can check the data which is collected from web service.
For more infomation about how to use the Prometheus, you could see the documentation on the offical website: ```https://prometheus.io/```


For data dashboard, I use the Grafana to show the data.
The data is from the Prometheus, so please make sure the Prometheus is opening in the meantime.
You can see the Grafana via ```https://localhost:3000``` and the account/password should be admin/admin in default.
First step, you will have to select the DB, the Prometheus, and do the setting, select the port and url.
And you should be able to see the dashboard.
For more infomation about the setting, you could see the documentation on the offical website: ```https://grafana.com/```


#### If you have further queries, please don't be hesitate to ask me.
#### Kind regard 
#### Cheng Huan Lai

