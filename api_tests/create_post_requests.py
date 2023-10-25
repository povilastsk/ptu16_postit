import requests
import json

reqUrl = "http://localhost:8000/posts/"

headersList = {
 "Accept": "*/*",
 "User-Agent": "PTU16 browser",
 "Authorization": "Token b8dbfc6de36191708f81a8b0cca47bd3601098d0",
 "Content-Type": "application/json" 
}

payload = json.dumps({
  "title": "papostinam per requests biblioteka",
  "body": "naudojant token autorizacija ir kitus simbolius",
  "likes": []
})

response = requests.request("POST", reqUrl, data=payload,  headers=headersList)

print(response.text)