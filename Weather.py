from asyncio import protocols
import json
import requests
from datetime import datetime
time = datetime.today().strftime('%Y-%m-%d')

def Refresh(ip):
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {"q":ip,"days":"3"}

    headers = {
        "X-RapidAPI-Key": "6e4025ecc2msh6bf47163f0b5d0bp18cbd2jsn912cdad9e3d4",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    return response