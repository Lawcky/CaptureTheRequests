# CaptureTheRequests 
This is a simple app in Python using Flask that'll create an Endpoint for any CTF challenge.

It'll log every requests it receives inside a file to simplify the process of checking for responses from targets (e.g. RCE or XSS challenges). 

simply use tail -f on the log file to start checking for responses

## for now it can : 
- Log and capture any requests made on its endpoints
- Serv as an HTTP server to offer any files / payload that could be needed both as a web server or simply as an endpoint to download them through the /dl/filename endpoint.

it uses HTTP, port 80 is not recommended.
