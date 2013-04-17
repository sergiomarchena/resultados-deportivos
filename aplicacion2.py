from lxml import etree
import requests

resultados = requests.get("http://www.resultados-futbol.com/scripts/api/api.php", params = {"key":"2b42a02ecec6a92d100a0b1b5e3a6e4d", "format":"xml", "req":"matchs", "league":"1"})


resultado = resultados.text

#xpath

xml = etree.fromstring(resultado)

ronda = xml.xpath("/matchs/match/round/text()")
local = xml.xpath("/matchs/match/local/text()")
visitor = xml.xpath("/matchs/match/visitor/text()")
date_partido = xml.xpath("/matchs/match/date/text()")
hour = xml.xpath("/matchs/match/hour/text()")
minute = xml.xpath("/matchs/match/minute/text()")
local_goals = xml.xpath("/matchs/match/local_goals/text()")
visitor_goals = xml.xpath("/matchs/match/visitor_goals/text()")
result = xml.xpath("/matchs/match/result/text()")
channels = xml.xpath("/matchs/match/channels/text()")

#html final
pag = etree.Element("html")

doc = etree.ElementTree(pag)

headELT = etree.SubElement (pag, 'head')

title = etree.SubElement (headELT, 'title')

title.text = "clasificacion"

bodyELT = etree.SubElement(pag, 'body')

h1ELT = etree.SubElement(bodyELT, 'h1')

h1ELT.text = "resultados"

tableELT = etree.SubElement(bodyELT, 'table')

trELT = etree.SubElement(tableELT, 'tr')

tdro = etree.SubElement(trELT, 'td')

strongro = etree.SubElement(tdro, 'strong')

strongro.text = "round"

tdlo = etree.SubElement(trELT, 'td')

stronglo = etree.SubElement(tdlo, 'strong')

stronglo.text = "local"

tdvi = etree.SubElement(trELT, 'td')

strongvi = etree.SubElement(tdvi, 'strong')

strongvi.text = "visitor"

tdda = etree.SubElement(trELT, 'td')

strongda = etree.SubElement(tdda, 'strong')

strongda.text = "date_partidos"

tdlg = etree.SubElement(trELT, 'td')

stronglg = etree.SubElement(tdlg, 'strong')

stronglg.text = "local_goals"

tdvg = etree.SubElement(trELT, 'td')

strongvg = etree.SubElement(tdvg, 'strong')

strongvg.text = "visitor_goals"

tdre = etree.SubElement(trELT, 'td')

strongre = etree.SubElement(tdre, 'strong')

strongre.text = "result"

for i in range(10):

    trALT = etree.SubElement(tableELT, 'tr')

    td4 = etree.SubElement(trALT, 'td')

    td4.text = "%s" % (ronda[i])

    td5 = etree.SubElement(trALT, 'td')

    td5.text = "%s" % (local[i])

    td6 = etree.SubElement(trALT, 'td')

    td6.text = "%s" % (visitor[i])

    td8 = etree.SubElement(trALT, 'td')

    td8.text = "%s" % (date_partido[i])

    td11 = etree.SubElement(trALT, 'td')

    td11.text = "%s" % (local_goals[i])

    td12 = etree.SubElement(trALT, 'td')

    td12.text = "%s" % (visitor_goals[i])
    
    td13 = etree.SubElement(trALT, 'td')

    td13.text = "%s" % (result[i])

print etree.tostring (pag, pretty_print = True)
