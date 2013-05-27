<html xmlns="http://www.w3.org/1999/xhtml"><head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
</meta>
<title>clasificacion</title>
</head>
<body>
<h1>clasificacion primera division</h1>
<table>
<tr>
<td><strong>Equipos</strong></td>
<td><strong>puntos</strong></td>
<td><strong>ganados</strong></td>
<td><strong>empates</strong></td>
<td><strong>perdidos</strong></td>
<td><strong>gfavor</strong></td>
<td><strong>gcontra</strong></td>
<td><strong>avg</strong></td>
</tr>

%for i in equipos:
<tr>
%for e in i:
<td>
{{e}}
</td>
%end
</tr>
%end
</table>
<a href="/clasificacion">Volver a elegir liga</a></p>
<p> <a href="/">Volver al indice</a></p><p> 
</body>
