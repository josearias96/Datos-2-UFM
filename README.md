# Datos-2-UFM
Proyecto del curso de Datos 2

Primera entrega del proyecto. 

Descripción: programa hecho con python que recibe 2 parámetros de búsqueda (acerca de artículos de NY Times). Al recibir ambos 
parámetros, verifica en una base de datos de MySQL (cache) si algún artículo con esos parámetros (keywords) está almacenado. 
Si no lo está, hace la consulta al API de NY Times, muestra los datos de la consulta y los inserta a la base de datos. 

Requisitos para el proyecto:

La base de datos de MySQL fue almacenada en un servidor local de apache, XAMPP. (Versión 3.2.2)
Se utilizó Python versión 3.6, con requisitos de los modulos: requests, json, mysql connector,  y pprofile (para el profiling).
Saber utilizar PHPMyAdmin.

MVP del proyecto: alguién que quiera hacer una consulta a un api desde algún endpoint, que quiera recibir una respuesta rápida y 
confiable del contenido y las url's de artículos de NY Times.

Segunda entrega del proyecto.

Se utilizó Flask para que el script de python pudiera ser convertido en un RESTful API. A partir del método GET, se llama a la clase Search o History del programa. Con la sintaxis: http://127.0.0.1:5000/search/kwd1/kwd2/tkn y http://127.0.0.1:5000/history/tkn respectivamente. Se implementó un token individual para poder identificar a cada usuario que realize a busqueda. Al momento de hacer la búsqueda a cualquiera de las 2 clases, se crea un log de la búsqueda, con el cual logstash recopila la información para la inserción a ELK. Se continuó usando el API de New York Times y la instancia de MySQL alojada en el servidor de XAMPP para las búsquedas .

Implementar ELK al proyecto: Se configuró Elastic Cloud con AWS para recibir la información a travéz de un pipeline de Logstash, insertandolo a Elasticsearch y para poder visualizar la actividad en Kibana. 
