import random
import requests

looping=True
while looping:
    randomtal = random.randint(1, 1000)
    url = f"https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763/json?_offset={random}&_limit=1"

    req =requests.get(url)

    json = req.json()
    print(req)
    lista = json["results"]
    print(lista)

    svar=input("vill du köra programmet en gång till? j/n")
    if (svar == "n" or svar == "N"):
        break
