import requests
from helpers import registerIP
url = "https://find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com/iplocation"

def getIp(ip):
	querystring = {"ip":ip,"apikey":"873dbe322aea47f89dcf729dcc8f60e8"}
	headers = {
	"X-RapidAPI-Key": "6e4025ecc2msh6bf47163f0b5d0bp18cbd2jsn912cdad9e3d4",
	"X-RapidAPI-Host": "find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring).json()

	if response['status'] == 200:
		return response
	else:
		return None

def validateIP(ip,user):
	if not ip:
		return False
	else:
		registerIP(ip,user)
		return True

