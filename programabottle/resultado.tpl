<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title> Resultados </title>
    <link href="css/resultado.css" rel="stylesheet" type="text/css" />
  </head>
  <body>
    <div id="centrar">
      <div id="cabezera">
	<h1> Ligas de Fútbol </h1>
      </div>
      <div id="texto">
       <form action="/respuestaresul" method="POST"> 	
	<img src="css/indice.png" alt="image" title="image" />	
	<p>Elige la liga de la que quieras obtener los resultados</p>	  
	<select name="resultado">
	  <option value="1">bbva</option>
	  <option value="2">liga adelante</option>
	  <option value="3">2ºB</option>
	  <option value="10">premier</option>
	  <option value="25">2º Inglesa</option>
	  <option value="87">3º Inglesa</option>
	  <option value="102">4º Inglesa</option>
	  <option value="7">serie A</option>
	  <option value="89">serie B</option>
	  <option value="90">3º Italiana</option>
	  <option value="91">4ºItaliana</option>
	  <option value="16">liga Francesa</option>
	  <option value="92">2º Francesa</option>
	  <option value="103">3º Francesa</option>
	  <option value="8">bundesliga</option>
	  <option value="93">2º Alemana</option>
	  <option value="94">3º Alemana</option>
	  <option value="178">4º Alemana</option>
	  <option value="9">liga holandesa</option>
	  <option value="104">2º Holandesa</option>
	  <option value="225">3º Holandesa</option>
	  <option value="226">4º Holandesa</option>
	  <option value="19">liga portuguesa</option>
	  <option value="96">2º Portuguesa</option>
	  <option value="223">3º Portuguesa</option>
	  <option value="224">4º Portuguesa</option>
	</select>
	  <form action="/respuestaresul" method="POST">  
	    <br/><p>Indica una Jornada con un número, si lo dejas en blanco mostrara los resultados mas recientes o los próximos encuentros que se disputan</p>
	    <input type="number" name="num_liga" value=""/>
	    <br/>
	    <br>
	      <input type='submit' value='Submit'/>
	    </form>
	  </form>
	</div>
       </div>
      </body>
    </html>
