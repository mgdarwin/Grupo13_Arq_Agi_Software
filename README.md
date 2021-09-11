# Grupo13_Arq_Agi_Software
Repositorio del grupo 13 de MISO


## Ejecución

Las carpetas reportes_service, facturacion-queue-service, facturacion-service y ________ son proyectos de Python independientes, que requieren su propio virtual environment, tienen dependencias cada una y por lo tanto es mejor iniciar un venv por cada carpeta.

Orden de Ejecución (desde una nueva terminal):

- En caso de estar detenido, ejecutar `redis-server` en una terminal y en el puerto `6379`
- En macOSX se debe ejecutar redis por separado siguiendo los siguientes pasos
  - Descargar redis en este link http://download.redis.io/redis-stable.tar.gz
  - En una terminal ir a la carpeta de descarga y ejecutar `tar xvzf redis-stable.tar` se descomprimar el binario
  - con el conabdo `cd` ir a la carpeta de redis `cd redis-stable` y ejecutar `make`
  - Esto instalará adecuadamente redis, ahora para correrlo se debe agregar al PATH la ruta de la siguiente manera
   - en la terminal ejecutar `export PATH=$PATH:$HOME/Downloads/redis-stable/src`
   - reiciciar la terminal y con el comando `redis-server` ya inciará el servicio en el puerto 6379

----

- Ejecutar la **cola de mensajería** (desde una nueva terminal):

* Acceder a la carpeta `facturacion-queue-service`,
* iniciar el ambiente con `source ./env/bin/activate`,
* instalar dependencias con `pip install -r ./requirements.txt`,
* ejecutar celery con el comando `celery -A tareas worker -l info -Q fact_queue -E`


----

- Ejecutar el microservicio de reportes (desde una nueva terminal):

* Acceder a la carpeta `reportes_service`,
* iniciar el ambiente con `source ./env/bin/activate`,
* instalar dependencias con `pip install -r ./requirements.txt`,
* ejecutar flask con `cd reporte_microserv && flask run`

Para invocar alguno de los dos servicios:

usando postman, llamar a `localhost:5000/report` con los métodos `GET` o `POST`

----

- Ejecutar el microservicio de **gestion médica** (desde una nueva terminal):

* Acceder a la carpeta `gestion_medica_service`,
* iniciar el ambiente con `source ./env/bin/activate`,
* instalar dependencias con `pip install -r ./requirements.txt`,
* ejecutar flask con `cd gestion_medica_microserv && flask run --port 5001`

Para invocar alguno de los dos servicios:

usando postman, llamar a `localhost:5001/servicio` con el método `POST`

----

- Ejecutar el microservicio de **facturacion** (desde una nueva terminal):

* Acceder a la carpeta `facturacion_service`,
* iniciar el ambiente (previamente creado) con `source ./env/bin/activate`,
* instalar dependencias con `pip install -r ./requirements.txt`,
* ejecutar flask con `cd facturacion_microserv && flask run --port 5002`

Para invocar alguno de los dos servicios:

usando postman, llamar a `localhost:5002/facturar` con el método `GET` o `POST`
