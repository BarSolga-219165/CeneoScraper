import requests as req

respons = req.get("https://www.ceneo.pl/55892514#tab=reviews")

print(respons.text)