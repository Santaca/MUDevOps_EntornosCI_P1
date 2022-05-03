# Repo para EIEC - DevOps - UNIR

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.

---

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Ejecución

python3 main.py <filename> <dup>
filename: **ruta** al fichero que contiene la lista de palabras, una por línea
dup: **yes|no**, yes para eliminar palabras duplicadas, no para mantener la lista

## Ejemplo de ejecución con Makefile

vagrant@ubuntu-focal:~/MUDevOps_EntornosCI_P1$ make -f Makefile
docker run --rm --volume `pwd`:/opt/app --env PYTHON_PATH=/opt/app -w /opt/app python:3.6-slim python3 main.py words.txt yes
Unable to find image 'python:3.6-slim' locally
3.6-slim: Pulling from library/python
a2abf6c4d29d: Pull complete
625294dad115: Pull complete
838e3a5a04bf: Pull complete
e93b4e59b689: Pull complete
c4401b8c7f9e: Pull complete
Digest: sha256:2cfebc27956e6a55f78606864d91fe527696f9e32a724e6f9702b5f9602d0474
Status: Downloaded newer image for python:3.6-slim
Se leerán las palabras del fichero words.txt
El fichero words.txt no existe
['gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin']
