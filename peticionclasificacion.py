import requests

clasificacion = requests.get("http://www.resultados-futbol.com/scripts/api/api.php",  params = {"key":"2b42a02ecec6a92d100a0b1b5e3a6e4d", "format":"xml", "req":"tables", "league":"1"}) 


if clasificacion.status_code == 200:

    print clasificacion.text
