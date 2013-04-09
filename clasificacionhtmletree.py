from lxml import etree

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

#bucle 20 veces 

trALT = etree.SubElement(tableELT, 'tr')

td1 = etree.SubElement(trALT, 'td')

td1.text = "Barcelona"

td2 = etree.SubElement(trALT, 'td')

td3 = etree.SubElement(trALT, 'td')

td4 = etree.SubElement(trALT, 'td')

td5 = etree.SubElement(trALT, 'td')

td6 = etree.SubElement(trALT, 'td')

td7 = etree.SubElement(trALT, 'td')

td8 = etree.SubElement(trALT, 'td')

td9 = etree.SubElement(trALT, 'td')

td10 = etree.SubElement(trALT, 'td')

print etree.tostring (pag, pretty_print = True)

