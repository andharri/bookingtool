import logging
import requests
import json

## setup logging

logging.basicConfig(
	format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
	level=logging.INFO,
	datefmt='%d-%m-%Y %H:%M:%S')
log = logging.getLogger("logger")

log.info("ROY")

## get auth token

body = {"username":"admin","password":"password"}

response = requests.post("http://10.4.104.171:8080/Services/Authentication/Authenticate", data=json.dumps(body))

print(json.loads(response.text)['sessionToken'])

authToken = json.loads(response.text)['sessionToken']

## get list of labs

header = {
	"X-Booked-SessionToken": authToken,
	"X-Booked-UserId": "2"
}
print(header)

response = requests.get("http://10.4.104.171:8080/Services/Resources/", headers=header)

#print(response.text)

for x in json.loads(response.text)['resources']:
	print(x)

