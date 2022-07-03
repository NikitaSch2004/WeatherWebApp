import requests

url = "https://hourmailer.p.rapidapi.com/send"

def sendMail(mail,subject,body):
    payload = {
	"toAddress": mail,
	"title": subject,
	"message": body
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "6e4025ecc2msh6bf47163f0b5d0bp18cbd2jsn912cdad9e3d4",
        "X-RapidAPI-Host": "hourmailer.p.rapidapi.com"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    return response