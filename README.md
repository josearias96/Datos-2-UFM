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
