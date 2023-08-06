# Bedrock-2 (CGI)
CGI implementation of Bedrock-2 in python 

### Testing the Bedrock service
```
curl -X POST -d '{ "blah": "boo", "event": "ok" }' -H "Content-Type: application/json; charset=UTF-8" http://localhost/cgi-bin/rpi_sensor.py -i
```
