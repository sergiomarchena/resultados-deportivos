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
<td><strong>visitor</strong></td>
<td><strong>date</strong></td>
<td><strong>hour</strong></td>
<td><strong>minute</strong></td>
<td><strong>local_goals</strong></td>
<td><strong>visitor_goals</strong></td>
<td><strong>result</strong></td>
</tr>

<tr>
<td>
%for i in ronda:
{{i}}
%end
</td>
<td>
%for i in local:
{{i}}
%end
</td>
<td>
%for i in visitor:
{{i}}
%end
</td>
<td>
%for i in date_partido:
{{i}}
%end
</td>
<td>
%for i in hour:
{{i}}
%end
</td>
<td>
%for i in minute:
{{i}}
%end
</td>
<td>
%for i in local_goals:
{{i}}
%end
</td>
<td>
%for i in visitor_goals:
{{i}}
%end
</td>
<td>
%for i in result:
{{i}}
%end
</td>
</tr>
</table>
<a href="/resultado">Volver a elegir liga</a></p>
<p> <a href="/">Volver al indice</a></p><p> 
</body>