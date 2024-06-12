# TFG-Modificaciones configurador y firmware 

Este es el repositorio de el TFG de Miguel Ángel Montero, donde se almacenan las modificaciones realizadas al configurador del Audimoth y su firmware ademas de la aplicacion que envia comandos a la Orange Pi y los srcipts que se ejecutan en la Orange Pi.

## Apliacón-kotlin

Carpeta que contiene la aplicacion de kotlin que envia comandos a la Orange Pi y muestra los resultados de estos.

## AudioMoth-Configuration-App

Carpeta que contiene el configurador del Audimoth con sus modificaciones para añadir un input de un ID numerico y enviarselo por USB a la grabadora. Las modificaciones principales se encuentran en los fichero *main.js* y *uiIndex.js*.

## AudioMoth-Project-master

Carpeta que contiene el firmware del Audimoth modificado para que use el ID enviado por el configurador como prefijo en el nombre de todas sus grabaciones. Las modificaciones se encuentran en los ficheros *audioMorh.c* y *main.c* de la carpeta /src.

## Orangepi-Scripts

Carpeta que continene los scripts usados en la Orange Pi que se usan para comunicarse o recivir los mensajes enviados por la aplicacion kotlin.



