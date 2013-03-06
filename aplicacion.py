import requests

resultados = requests.get("http://www.resultados-futbol.com/scripts/api/api.php", params = {"key":"2b42a02ecec6a92d100a0b1b5e3a6e4d", "format":"xml", "req":"matchs", "league":"1"}) 


if resultados.status_code == 200:

    print resultados.text
