import requests 
import json


def browse(term):
    print(term.replace(' ', '+'))
    url = f"https://google-search3.p.rapidapi.com/api/v1/search/q={term}"

    headers = {
	"X-User-Agent": "desktop",
	"X-Proxy-Location": "IN",
	"X-RapidAPI-Key": "cc4bcff068msh4a1c941cf322004p176518jsndd2a674ed7ad",
	"X-RapidAPI-Host": "google-search3.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    content = json.loads(response.text)
    return(content['results'][0]['title'], content['results'][0]['link'])