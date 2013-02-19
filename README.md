resultados-deportivos
=====================

aplicacion python

consistiria en hacer una aplicacion de consultas sobre el futbol,y sus diferentes ligas, las consultas que se pueden hacer son las siguientes:


-Ligas:
Devuelve un listado de todas las ligas ordenadas por importancia.


-Clasificación:
Al igual que la petición de resultados, dada una competición y un grupo (en el caso de que sea una competición con varios grupos), devuelve el listado de equipos con sus estadísticas ordenados por la clasificación actual en su competición, totalmente en directo.


-Partidos por jornada:
Dada una competición y un grupo (en el caso de que sea una competición con varios grupos), devuelve los partidos con sus resultados en una jornada específica y si están jugandose en este momento y en por que minuto va en el momento de la petición.


-Partidos de una fecha concreta:
Con esta petición podemos obtener los partidos que se juegan en la fecha que facilitemos, si no se facilita ninguna, por defecto sera la del día de la petición. En el caso de que pidamos la fecha de hoy, además se podrá filtrar por los que se están jugando en direceto en el momento de la petición. La estructura devuelta es exactamente el mismo que el de los 'Partidos por jornada'.



Tambien podriamos añadir si resulta muy sencillo podriamos poner una consulta de una api de geolocalizacion que muestre donde se encuentra el estadio en el que se ha jugado o se juega el partido.

la pagina web:

http://www.resultados-futbol.com/api/documentacion#req_tables


-primero la aplicacion dara un listados de liga a elegir. seleccionaremos la liga que queremos consultar

-segundo dentro de esa liga nos mostrara los resultados y la clasificacion 
