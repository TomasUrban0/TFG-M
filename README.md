# TFG-Modificaciones configurador y firmware 

Este es el repositorio del TFG de Miguel Ángel Montero, donde se almacenan las modificaciones realizadas al configurador del AudioMoth y su firmware, además de la aplicación que envía comandos a la Orange Pi y los scripts que se ejecutan en la Orange Pi.

## Apliacón-kotlin

Carpeta que contiene la aplicación de Kotlin que envía comandos a la Orange Pi y muestra los resultados de estos.
## AudioMoth-Configuration-App

Carpeta que contiene el configurador del AudioMoth con sus modificaciones para añadir una entrada de un ID numérico y enviárselo por USB a la grabadora. Las modificaciones principales se encuentran en los ficheros *main.js* y *uiIndex.js*.

## AudioMoth-Project-master

Carpeta que contiene el firmware del AudioMoth modificado para que use el ID enviado por el configurador como prefijo en el nombre de todas sus grabaciones. Las modificaciones se encuentran en los ficheros *audioMoth.c* y *main.c* de la carpeta /src.

## Orangepi-Scripts

Carpeta que contiene los scripts usados en la Orange Pi que se usan para comunicarse o recibir los mensajes enviados por la aplicación de Kotlin.


