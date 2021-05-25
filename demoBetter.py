import requests
import html

url = "https://opentdb.com/api.php?amount=1&category=11&difficulty=easy&type=boolean"

webresp = requests.get(url)

finished = webresp.json()

print(finished)
