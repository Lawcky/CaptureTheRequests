# CaptureTheRequests 
This is a simple app in Python using Flask that'll create an Endpoint for any CTF challenge.

It'll log every requests it receives inside a file to simplify the process of checking for responses from targets. (simply use tail -f to check it)

## for now it can : 
- Log and capture any requests made on its endpoints
- Serv as an HTTP server for any files / payload that could be needed
- Download files through the /dl/filename endpoint

## Next steps
- add a way for the app to catch and offer a connection to any reverse_shells it receives
