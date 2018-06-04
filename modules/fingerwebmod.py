#!/usr/bin/python2
# encoding: utf-8
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from subprocess import call
from modules import portsmod
from modules import checker
from modules import logs
import os

def whatw():
    checker.cRojo("Desea Guardar el logs de la informacion? y/n : ")
    resp=input("Introduce tu Respuesta y/n : ")
    if resp=="y":
        web=portsmod.host()
        checker.cAmarillo("Obteniendo informacion del sitio web.")
        checker.bspc()
        logsalida=logs.randomarch("whatweb/","WHATWEB",".log")
        call(["whatweb","-v", web, "--log-verbose",logsalida])
        checker.bspc()
        checker.cAmarillo("--------------------------------------------------------")
        checker.cRojo(["Tu log se ha Guardado en la ruta: ",logsalida])
        checker.cAmarillo("--------------------------------------------------------")
        checker.bspc()
    elif resp=="n":
        web=portsmod.host()
        checker.cAmarillo("Obteniendo informacion del sitio web.")
        checker.bspc()
        call(["whatweb","-v", web])
        execute()


def nickscan():
    checker.cRojo("Desea Guardar el logs de la informacion? y/n : ")
    resp=input("Introduce tu Respuesta y/n : ")
    if resp=="y":
        web=portsmod.host()
        checker.cAmarillo("Buscando vulnerabilidades en el sitio web usando nikto...")
        logsalida=logs.randomarch("nikto/","NIKTO",".html")
        call(["nikto","-no404","-host",web,"-o",logsalida])
        checker.bspc()
        checker.cAmarillo("--------------------------------------------------------")
        checker.cRojo(["Tu log se ha Guardado en la ruta: ",logsalida])
        checker.cAmarillo("--------------------------------------------------------")
        checker.bspc()
    elif resp=="n":
        web=portsmod.host()
        checker.cAmarillo("Buscando vulnerabilidades en el sitio web usando nikto...")
        call(["nikto","-no404","-host",web])
    execute()

def joomsc():
    web=portsmod.host()
    checker.cAmarillo("Buscando vulnerabilidades en el sitio web usando joomlavs...")
    call(["ruby","joomlavs/joomlavs.rb","-u",web,"-a"])
    execute()

def joomsctor():
    web=host=portsmod.host()
    checker.cAmarillo("Buscando vulnerabilidades en el sitio web usando joomlavs usando TOR...")
    call(["ruby","joomlavs/joomlavs.rb","-u",web,"--proxy","SOCKS5://127.0.0.1:9050","-a"])
    execute()

def wordpresscan():
    checker.cRojo("Desea Guardar el logs de la informacion? y/n : ")
    resp=input("Introduce tu Respuesta y/n : ")
    if resp=="y":
        logsdirectory="/opt/wpscan/modules/logs/wpscan/"
        if not os.path.exists(logsdirectory):
            print ("El directorio ",logsdirectory," no existe, se creará.")
            os.system("sudo mkdir -p /opt/wpscan/modules/logs/wpscan/")
        web=portsmod.host()
        logsalida=logs.randomarch("wpscan/","WPSCAN",".log")
        call(["sudo","wpscan","-u",web,"--enumerate","p","--enumerate","t","--enumerate","u","--log",logsalida])
        checker.bspc()
        checker.cAmarillo("--------------------------------------------------------")
        checker.cRojo(["Tu log se ha Guardado en la ruta: ",logsdirectory])
        checker.cAmarillo("--------------------------------------------------------")
        checker.bspc()
    elif resp=="n":
        web=portsmod.host()
        call(["sudo","wpscan","-u",web,"--enumerate","p","--enumerate","t","--enumerate","u"])
    execute()

def wordpresscantor():
    checker.cRojo("Desea Guardar el logs de la informacion? y/n : ")
    resp=input("Introduce tu Respuesta y/n : ")
    if resp=="y":
        logsdirectory="/opt/wpscan/modules/logs/wpscan/"
        if not os.path.exists(logsdirectory):
            print ("El directorio ",logsdirectory," no existe, se creará.")
            os.system("sudo mkdir -p /opt/wpscan/modules/logs/wpscan/")
        web=portsmod.host()
        logsalida=logs.randomarch("wpscan/","WPSCAN",".log")
        web=portsmod.host()
        checker.cAmarillo("Buscando vulnerabilidades en el sitio web usando wpscan...")
        call(["sudo","wpscan","-u",web,"--enumerate","p","--enumerate","t","--enumerate","u","--proxy","socks5://127.0.0.1:9050","--log",logsalida])
        checker.bspc()
        checker.cAmarillo("--------------------------------------------------------")
        checker.cRojo(["Tu log se ha Guardado en la ruta: ",logsdirectory])
        checker.cAmarillo("--------------------------------------------------------")
        checker.bspc()
    elif resp=="n":
        web=portsmod.host()
        call(["sudo","wpscan","-u",web,"--enumerate","p","--enumerate","t","--enumerate","u","--proxy","socks5://127.0.0.1:9050"])
    execute()

def execute():
    checker.cAmarillo("Seleccina una de las siguientes opciones:")
    print("""
    a) Obtener informacion del sitio web, servidor, Ip, CMS, Software del servidor y mas.
    b) Buscar vulnerabilidades web usando nikto.
    c) Buscar vulnerabilidades web de sitios web Joomla.
    d) Buscar vulnerabilidades web de sitios web Joomla usando TOR.
    e) Buscar vulnerabilidades web de sitios web con WordPress
    f) Buscar vulnerabilidades web de sitios web con WordPress usando TOR.
    g) Salir.""")
    sel=input("Introduce tu opcion: ")
    if sel== "a":
        whatw()
    elif sel == "b":
        nickscan()
    elif sel == "c":
        joomsc()
    elif sel == "d":
        joomsctor()
    elif sel == "e":
        wordpresscan()
    elif sel == "f":
        wordpresscantor()
    elif sel == "g":
        print ("Saliendo.")
    else:
        execute()
