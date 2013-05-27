<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
</meta>
<title>clasificacion</title>
</head>
<body>
<h1>resultados</h1>
<table>
<tr>
<td><strong>ronda</strong></td>
<td><strong>local</strong></td>
<td><strong>visitante</strong></td>
<td><strong>fecha partido</strong></td>
<td><strong>hora</strong></td>
<td><strong>minuto</strong></td>
<td><strong>resultado</strong></td>
</tr>

%for i in rondas:
<tr>
%for e in i:
<td>
{{e}}
</td>
%end
</tr>
%end
</table>
<a href="/resultado">Volver a elegir liga</a></p>
<p> <a href="/">Volver al indice</a></p><p> 
</body>
