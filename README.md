# Grupo13_Arq_Agi_Software
Repositorio del grupo 11 de MISO


## Ejecución

Las carpetas reportes_service, facturacion-queue-service y _______, ________ son proyectos de Python independientes, que requieren su propio virtual environment, tienen dependencias cada una y por lo tanto es mejor iniciar un venv por cada carpeta.

Orden de Ejecución (desde una nueva terminal):

- En caso de estar detenido, ejecutar `redis-server` en una terminal y en el puerto `6379`

----

- Ejecutar la cola de mensajería (desde una nueva terminal):

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

- Ejecutar el microservicio de reportes (desde una nueva terminal):

* Acceder a la carpeta `gestion_medica_service`,
* iniciar el ambiente con `source ./env/bin/activate`,
* instalar dependencias con `pip install -r ./requirements.txt`,
* ejecutar flask con `cd gestion_medica_microserv && flask run --port 5001`

Para invocar alguno de los dos servicios:

usando postman, llamar a `localhost:5001/servicio` con el método `POST`
