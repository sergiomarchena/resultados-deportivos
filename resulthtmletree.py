from lxml import etree

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

tdELT = etree.SubElement(trELT, 'td')

strongELT = etree.SubElement(tdELT, 'strong')

strongELT.text = "id"

tdye = etree.SubElement(trELT, 'td')

strongye = etree.SubElement(tdye, 'strong')

strongye.text = "year"

tdgr = etree.SubElement(trELT, 'td')

strongtr = etree.SubElement(tdgr, 'strong')

strongtr.text = "group"

tdro = etree.SubElement(trELT, 'td')

strongro = etree.SubElement(tdro, 'strong')

strongro.text = "round"

tdlo = etree.SubElement(trELT, 'td')

stronglo = etree.SubElement(tdlo, 'strong')

stronglo.text = "local"

tdvi = etree.SubElement(trELT, 'td')

strongvi = etree.SubElement(tdvi, 'strong')

strongvi.text = "visitor"

tdsc = etree.SubElement(trELT, 'td')

strongsc = etree.SubElement(tdsc, 'strong')

strongvi.text = "schedule"

tdda = etree.SubElement(trELT, 'td')

strongda = etree.SubElement(tdda, 'strong')

strongda.text = "date"

tdho = etree.SubElement(trELT, 'td')

strongho = etree.SubElement(tdho, 'strong')

strongho.text = "hour"

tdmi = etree.SubElement(trELT, 'td')

strongmi = etree.SubElement(tdmi, 'strong')

strongmi.text = "minute"

tdlg = etree.SubElement(trELT, 'td')

stronglg = etree.SubElement(tdlg, 'strong')

stronglg.text = "local_goals"

tdvg = etree.SubElement(trELT, 'td')

strongvg = etree.SubElement(tdvg, 'strong')

strongvg.text = "visitor_goals"

tdre = etree.SubElement(trELT, 'td')

strongre = etree.SubElement(tdre, 'strong')

strongre.text = "result"

tdli = etree.SubElement(trELT, 'td')

strongli = etree.SubElement(tdli, 'strong')

strongli.text = "live_minute"

tdst = etree.SubElement(trELT, 'td')

strongst = etree.SubElement(tdst, 'strong')

strongst.text = "status"

tdch = etree.SubElement(trELT, 'td')

strongch = etree.SubElement(tdch, 'strong')

strongch.text = "channels"

#aqui un bucle 16 veces

trALT = etree.SubElement(tableELT, 'tr')

td1 = etree.SubElement(trALT, 'td')

td2 = etree.SubElement(trALT, 'td')

td3 = etree.SubElement(trALT, 'td')

td4 = etree.SubElement(trALT, 'td')

td5 = etree.SubElement(trALT, 'td')

td6 = etree.SubElement(trALT, 'td')

td7 = etree.SubElement(trALT, 'td')

td8 = etree.SubElement(trALT, 'td')

td9 = etree.SubElement(trALT, 'td')

td10 = etree.SubElement(trALT, 'td')

td11 = etree.SubElement(trALT, 'td')

td12 = etree.SubElement(trALT, 'td')

td13 = etree.SubElement(trALT, 'td')

td14 = etree.SubElement(trALT, 'td')

td15 = etree.SubElement(trALT, 'td')

td16 = etree.SubElement(trALT, 'td')


print etree.tostring (pag, pretty_print = True)


