import logging
import requests
import json
import pprint
import time

def isLabPoweredOn(lab):
	#TODO
	log.info("lab: "+lab+" is powered on!")
	return False
	
def powerOnLab(lab):
	log.info("Powering on: "+lab)
	#TODO
	log.info("Lab is powered on: "+lab)
	
def powerOffLab(lab):
	log.info("Powering off: "+lab)
	#TODO
	log.info("Lab is powered off: "+lab)

def isBookingActive(startTime,endTime):
	currentEpoch = time.time()
	startTimeEpoch = time.mktime(time.strptime(startTime, "%Y-%m-%dT%H:%M:%S+0000"))
	endTimeEpoch = time.mktime(time.strptime(endTime, "%Y-%m-%dT%H:%M:%S+0000"))
	
	if currentEpoch < endTimeEpoch and currentEpoch > startTimeEpoch:
		log.info("Booking is active")
		return True
	else:
		log.info("Booking is not active")
		return False

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
authToken = json.loads(response.text)['sessionToken']

## get list of labs

labs = []
header = {
	"X-Booked-SessionToken": authToken,
	"X-Booked-UserId": "2"
}

response = requests.get("http://10.4.104.171:8080/Services/Resources/", headers=header)

for x in json.loads(response.text)['resources']:
	lab = {
		'id': x['resourceId'],
		'name': x['name']
	}
	labs.append(lab)

## for each lab work out if we are in an active booking

for lab in labs:

	response = requests.get("http://10.4.104.171:8080/Services/Reservations/?resourceId="+lab['id'], headers=header)
	
	for x in json.loads(response.text)['reservations']:
		if isBookingActive(x['startDate'],x['endDate']):
			# check that lab is powered on or not
			if not isLabPoweredOn(lab['name']):
				#power on lab
				powerOnLab(lab['name'])
		elif isBookingSoon(x['startDate'],x['endDate']):
			if isLabPoweredOn(lab['name']):
				resetLabConfig(lab['name'])
			else:
				powerOnLab(lab['name'])
		else:
			if isLabPoweredOn(lab['name']):
				powerOffLab(lab['name'])
				