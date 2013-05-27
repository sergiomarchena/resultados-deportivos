<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
    <link rel="stylesheet" type="text/css" href="/css/respuestresul.css" />
    <title>clasificacion</title>
  </head>
  <body>
    <div id="centrar">
      <div id="cabecera">
	<h1>resultados</h1>
	<ul id="menu">
	  <li><a href="/" title="Indice" class="active">Indice</a></li>
	  <li><a href="/resultado" title="ID">Elegir liga</a></li>
      </div>
      <div id="texto">
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
      </div>
  </body>
</html>
