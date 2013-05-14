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
<td><strong>gf</strong></td>
<td><strong>ga</strong></td>
<td><strong>avg</strong></td>
</tr>

<tr>
<td>
%for i in equipos:
{{i}}
%end
</td>
<td>
%for i in puntos:
{{i}}
%end
</td>
<td>
%for i in pganados:
{{i}}
%end
</td>
<td>
%for i in pempate:
{{i}}
%end
</td>
<td>
%for i in pperdidos:
{{i}}
%end
</td>
<td>
%for i in golesfavor:
{{i}}
%end
</td>
<td>
%for i in golescontra:
{{i}}
%end
</td>
<td>
%for i in promedio:
{{i}}
%end
</td>
</tr>




