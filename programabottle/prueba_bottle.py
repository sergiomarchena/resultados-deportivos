import bottle
import requests
import json
@bottle.route('/')
def home_page():
    return bottle.template("index2")



@bottle.route('/clasificacion')
def home_page():
    return bottle.template('clasificacion')

@bottle.route('/respuesta', method='POST')
def respuesta():
    clasificacion = bottle.request.forms.get("clasificacion")
    respuesta = requests.get("http://www.resultados-futbol.com/scripts/api/api.php", params = {"key":"2b42a02ecec6a92d100a0b1b5e3a6e4d", "format":"json", "req":"tables", "league":clasificacion}) 
    respuestas = respuesta.text
    equipos = []
    puntos = []
    pganados = []
    pempate = []
    pperdidos = []
    golesfavor = []
    golescontra = []
    promedio = []

    for i in xrange(20):
        equipos.append(json.loads(respuesta.text)["table"][i]["team"])
        puntos.append(json.loads(respuesta.text)["table"][i]["points"])
        pganados.append(json.loads(respuesta.text)["table"][i]["wins"])
        pempate.append(json.loads(respuesta.text)["table"][i]["draws"])
        pperdidos.append(json.loads(respuesta.text)["table"][i]["losses"])
        golesfavor.append(json.loads(respuesta.text)["table"][i]["gf"])
        golescontra.append(json.loads(respuesta.text)["table"][i]["ga"])
        promedio.append(json.loads(respuesta.text)["table"][i]["avg"])
        

        
        return bottle.template('respuesta',equipos=equipos, puntos= puntos,pganados=pganados, pempate= pempate,pperdidos=pperdidos,golesfavor=golesfavor,golescontra=golescontra,promedio=promedio)

@bottle.route('/resultado')
def home_page():
    return bottle.template('resultado')

@bottle.route('/respuestaresul', method='POST')
def respuesta():
    clasificacion = bottle.request.forms.get("resultado")
    respuesta = requests.get("http://www.resultados-futbol.com/scripts/api/api.php", params = {"key":"2b42a02ecec6a92d100a0b1b5e3a6e4d", "format":"json", "req":"matchs", "league":resultado})
    respuestas = resultados.text
    ronda = []
    local = []
    visitor = []
    date_partido = []
    hour = []
    minute = []
    local_goals = []
    visitor_goals = []
    result = []
    for i in xrange(10):
        ronda.append(json.loads(resultados.text)["match"][i]["round"])
        local.append(json.loads(resultados.text)["match"][i]["local"])
        visitor.append(json.loads(resultados.text)["match"][i]["visitor"])
        date_partido.append(json.loads(resultados.text)["match"][i]["date"])
        hour.append(json.loads(resultados.text)["match"][i]["hour"])
        minute.append(json.loads(resultados.text)["match"][i]["minute"])
        local_goals.append(json.loads(resultados.text)["match"][i]["local_goals"])
        visitor_goals.append(json.loads(resultados.text)["match"][i]["visitor_goals"])
        result.append(json.loads(resultados.text)["match"][i]["result"])
    return bottle.template('respuesta', ronda= ronda,local=local,visitor=visitor, date_partido=date_partido,hour=hour,minute=minute,local_goals=local_goals,visitor_goals=visitor_goals,result=result)
bottle.run(host="localhost", port=8080)


