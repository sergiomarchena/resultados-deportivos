#esta es la peticion y la que nos proporciona los datos
import requests
from lxml import etree

clasificacion = requests.get("http://www.resultados-futbol.com/scripts/api/api.php",  params = {"key":"2b42a02ecec6a92d100a0b1b5e3a6e4d", "format":"xml", "req":"tables", "league":"1"}) 

texto = clasificacion.text

#con xpath seleccionamos los datos
xml = etree.fromstring(texto)

equipos = xml.xpath("/tables/table/team/text()")
puntos = xml.xpath("/tables/table/points/text()")
pganados = xml.xpath("/tables/table/wins/text()")
pempate = xml.xpath("/tables/table/draws/text()")
pperdidos = xml.xpath("/tables/table/losses/text()")
golesfavor = xml.xpath("/tables/table/gf/text()")
golescontra = xml.xpath("/tables/table/ga/text()")
promedio =  xml.xpath("/tables/table/avg/text()")
marca =  xml.xpath("/tables/table/mark/text()")

#construccion html final
pag = etree.Element("html")

doc = etree.ElementTree(pag)

headELT = etree.SubElement (pag, 'head')

title = etree.SubElement (headELT, 'title')

title.text = "clasificacion"

bodyELT = etree.SubElement(pag, 'body')

h1ELT = etree.SubElement(bodyELT, 'h1')

h1ELT.text = "clasificacion"

tableELT = etree.SubElement(bodyELT, 'table')

trELT = etree.SubElement(tableELT, 'tr')

tdELT = etree.SubElement(trELT, 'td')

strongELT = etree.SubElement(tdELT, 'strong')

strongELT.text = "equipos"

tdpo = etree.SubElement(trELT, 'td')

strongpo = etree.SubElement(tdpo, 'strong')

strongpo.text = "points"

tdwi = etree.SubElement(trELT, 'td')

strongwi = etree.SubElement(tdwi, 'strong')

strongwi.text = "wins"

tddr= etree.SubElement(trELT, 'td')

strongdr = etree.SubElement(tddr, 'strong')

strongdr.text = "draws"

tdlo = etree.SubElement(trELT, 'td')

stronglo = etree.SubElement(tdlo, 'strong')

stronglo.text = "losses"

tdgf = etree.SubElement(trELT, 'td')

stronggf = etree.SubElement(tdgf, 'strong')

stronggf.text = "gf"

tdga = etree.SubElement(trELT, 'td')

strongga = etree.SubElement(tdga, 'strong')

strongga.text = "schedule"

tdav = etree.SubElement(trELT, 'td')

strongav = etree.SubElement(tdav, 'strong')

strongav.text = "avg"

tdma = etree.SubElement(trELT, 'td')

strongma = etree.SubElement(tdma, 'strong')

strongma.text = "mark"

tdro = etree.SubElement(trELT, 'td')

strongro = etree.SubElement(tdro, 'strong')

strongro.text = "round"


for i in range(20):

    trALT = etree.SubElement(tableELT, 'tr')

    td1 = etree.SubElement(trALT, 'td')

    td1.text = "%s" % (equipos[i])

    td2 = etree.SubElement(trALT, 'td')

    td2.text = "%s" % (puntos[i]) 

    td3 = etree.SubElement(trALT, 'td')

    td3.text = "%s" % (pganados[i])

    td4 = etree.SubElement(trALT, 'td')

    td4.text = "%s" % (pempate[i])

    td5 = etree.SubElement(trALT, 'td')

    td5.text = "%s" % (pperdidos[i])
    
    td6 = etree.SubElement(trALT, 'td')

    td6.text = "%s" % (golesfavor[i])

    td7 = etree.SubElement(trALT, 'td')

    td7.text = "%s" % (golescontra[i])

    td8 = etree.SubElement(trALT, 'td')

    td8.text = "%s" % (promedio[i])

    td9 = etree.SubElement(trALT, 'td')

    td9.text = "%s" % (marca[i])


print etree.tostring (pag, pretty_print = True)
