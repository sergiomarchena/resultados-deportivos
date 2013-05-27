<html xmlns="http://www.w3.org/1999/xhtml"><head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8"/>
    <title>clasificacion</title>
    <link rel="stylesheet" type="text/css" href="/css/respuestaclas.css" />
  </head>
  <body>
    <div id="centrar">

      <div id="cabecera">
	<h1>clasificacion primera division</h1>
	<ul id="menu">
	  <li><a href="/" title="Indice" class="active">Indice</a></li>
	  <li><a href="clasificacion" title="ID">Elegir liga</a></li>
      </div>
      <div id="texto">
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
      </div>
    </div>
  </body>
</html>
