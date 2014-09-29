Title: Descargar
En_menu: Si
Url: descargar

Aquí podrás descargar las herramientas necesarias para usar Pylares en tu
computadora.

<div class="pure-g">
<div class="pure-u-1 pure-u-md-1-2">
<a class="pure-button pure-button-primary" href="/Instalador_Pylares- 0.1.exe">Descargar para Windows XP/7/8</a>
</div>
<div class="pure-u-1 pure-u-md-1-2">
<a class="pure-button pure-button-primary" href="#instalar-en-linux">Instrucciones para GNU/Linux</a>
</div>
</div>

## ¿Qué hace el instalador?

El proceso de instalación realizará las siguientes acciones:

- Instala el lenguaje de programación Python.
- Instala el entorno de desarrollo Geany.
- Instala las dependencias necesarias para por generar interfaces gráficas.
- Instala las dependencias necesarias para trabajar con imágenes en python.
- Instala la biblioteca Pylares.

## Instrucciones de uso

Una vez que finalizó el proceso de instalación, simplemente hay que buscar el
programa Geany para empezar a probar Pylares.

El boton con el texto "Ejecutar" convertirá el código en Python en un programa
listo para usar.

![Geany]({filename}/imagenes/geany-ejecutar.jpg)

<div id="instalar-en-linux"></div>
## Instrucciones para instalar en GNU/Linux

El instalador solo está disponible para Ubuntu 12.04 y 14.04 y distribuciones
derivadas, como Xubuntu y Kubuntu.

Para instalar Pylares abre una terminal (Presionando **Ctrl + Alt + T**) y copia
y pega la siguiente línea de código.

    cd /tmp && wget http://pylares.org/instalador-linux.sh && chmod u+x instalador-linux.sh && sudo ./instalador-linux.sh
