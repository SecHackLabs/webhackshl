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
from modules import checker
from modules import logs

def host():
    global target
    target=input("Introduce el host al que deseas hacerle el scan: ")
    if target:
        return target
    else:
        checker.cRojo("Host invalido.")
        host()

def port():
    global portnumber
    portnumber=input("Introduce el puerto o los puertos que deseas escanear (Si deseas un rango de puertos, escribelos de la manera 1-1000): ")
    if portnumber:
        return portnumber
    else:
        checker.cRojo("Puerto invalido.")
        port()

def intensescan():
    checker.cRojo("Desea Guardar el logs de la informacion? y/n : ")
    resp=input("Introduce tu Respuesta y/n : ")
    if resp=="y":
        host()
        logsalida=logs.randomarch("nmap-full/","NMAP-FULL",".log")
        checker.cRojo("Para este tipo de escaneo necesitas privilegios sudo o root, por favor introduzca su contrasena si no eres root.")
        call(["sudo","nmap","-A","-T4","-sS","-Pn","-O","-sV","-p","1-10000","-v",target,"-oN",logsalida])
        checker.bspc()
        checker.cAmarillo("--------------------------------------------------------")
        checker.cRojo(["Tu log se ha Guardado en la ruta: ",logsalida])
        checker.cAmarillo("--------------------------------------------------------")
        checker.bspc()
    elif resp=="n":
        host()
        checker.cRojo("Para este tipo de escaneo necesitas privilegios sudo o root, por favor introduzca su contrasena si no eres root.")
        call(["sudo","nmap","-A","-T4","-sS","-Pn","-O","-sV","-p","1-10000","-v",target])

def fastscan():
    checker.cRojo("Desea Guardar el logs de la informacion? y/n : ")
    resp=input("Introduce tu Respuesta y/n : ")
    if resp=="y":
        host()
        logsalida=logs.randomarch("nmap-rapido/","NMAP-Rapido",".log")
        call(["nmap","--open","-F",target,"-oN",logsalida])
        checker.bspc()
        checker.cAmarillo("--------------------------------------------------------")
        checker.cRojo(["Tu log se ha Guardado en la ruta: ",logsalida])
        checker.cAmarillo("--------------------------------------------------------")
        checker.bspc()
    elif resp=="n":
        host()
        call(["nmap","--open","-F",target])

def detectserv():
    checker.cRojo("Desea Guardar el logs de la informacion? y/n : ")
    resp=input("Introduce tu Respuesta y/n : ")
    if resp=="y":
        host()
        logsalida=logs.randomarch("nmap-servhost/","SERV-HOST",".log")
        call(["nmap","-sP",target,"-oN",logsalida])
        checker.bspc()
        checker.cAmarillo("--------------------------------------------------------")
        checker.cRojo(["Tu log se ha Guardado en la ruta: ",logsalida])
        checker.cAmarillo("--------------------------------------------------------")
        checker.bspc()        
    elif resp=="n":
        host()
        call(["nmap","-sP",target])

def detectver():
    checker.cRojo("Desea Guardar el logs de la informacion? y/n : ")
    resp=input("Introduce tu Respuesta y/n : ")
    if resp=="y":
        host()
        logsalida=logs.randomarch("nmap-serviciosver/","SERVICIO-VER",".log")
        call(["nmap","-sV",target,"-oN",logsalida])
        checker.bspc()
        checker.cAmarillo("--------------------------------------------------------")
        checker.cRojo(["Tu log se ha Guardado en la ruta: ",logsalida])
        checker.cAmarillo("--------------------------------------------------------")
        checker.bspc()
    elif resp=="n":
        host()
        call(["nmap","-sV",target])

def escanport():
    checker.cRojo("Desea Guardar el logs de la informacion? y/n : ")
    resp=input("Introduce tu Respuesta y/n : ")
    if resp=="y":
        host()
        port()
        logsalida=logs.randomarch("nmap-puertorango/","PUERTORANGO",".log")
        call(["nmap","-p",portnumber,target,"-oN",logsalida])
        checker.bspc()
        checker.cAmarillo("--------------------------------------------------------")
        checker.cRojo(["Tu log se ha Guardado en la ruta: ",logsalida])
        checker.cAmarillo("--------------------------------------------------------")
        checker.bspc()
    elif resp=="n":
        host()
        port()
        call(["nmap","-p",portnumber,target])

def recsystem():
    checker.cRojo("Desea Guardar el logs de la informacion? y/n : ")
    resp=input("Introduce tu Respuesta y/n : ")
    if resp=="y":
        host()
        logsalida=logs.randomarch("nmap-so-host/","SYTEMOPERHOST",".log")
        checker.cRojo("Para este tipo de escaneo necesitas privilegios sudo o root, por favor introduzca su contrasena si no eres root.")
        call(["sudo","nmap","-O",target,"-oN",logsalida])
        checker.bspc()
        checker.cAmarillo("--------------------------------------------------------")
        checker.cRojo(["Tu log se ha Guardado en la ruta: ",logsalida])
        checker.cAmarillo("--------------------------------------------------------")
        checker.bspc()
    elif resp=="n":
        host()
        call(["sudo","nmap","-O",target])

def enumdns():
    checker.cRojo("Desea Guardar el logs de la informacion? y/n : ")
    resp=input("Introduce tu Respuesta y/n : ")
    if resp=="y":
        host()
        logsalida=logs.randomarch("dnsenum/","DNSENUM",".xml")
        checker.cAmarillo("Enumerando DNS's")
        call(["dnsenum",target,"-o",logsalida])
        checker.bspc()
        checker.cAmarillo("--------------------------------------------------------")
        checker.cRojo(["Tu log se ha Guardado en la ruta: ",logsalida])
        checker.cAmarillo("--------------------------------------------------------")
        checker.bspc()
    elif resp=="n":
        host()
        call(["dnsenum",target])

def bypasscloud():
    checker.cRojo("Desea Guardar el logs de la informacion? y/n : ")
    resp=input("Introduce tu Respuesta y/n : ")
    if resp=="y":
        try:
            host()
            logsalida=logs.randomarch("bypass/","BYPASSER",".log")
            checker.cAmarillo("Intentando Bypassear Cloudflare usando fierce...")
            call(["fierce","-dns",target,"-fulloutput",logsalida]) 
            checker.bspc()
            checker.cAmarillo("--------------------------------------------------------")
            checker.cRojo(["Tu log se ha Guardado en la ruta: ",logsalida])
            checker.cAmarillo("--------------------------------------------------------")
            checker.bspc()
        except OSError:
            call(["fierce.pl","-dns",target,"-fulloutput",logsalida])
        except:
            print ("Ha ocurrido un error, saliendo.")
            pass
    elif resp=="n":
        try:
            host()
            call(["fierce","-dns",target]) 
        except OSError:
            call(["fierce.pl","-dns",target])
        except:
            print ("Ha ocurrido un error, saliendo.")
            pass

def menu():
    checker.cAmarillo("Por favor selecciona una de las siguientes opciones")
    print("""
    a) Escaneo full de un host (Lento pero el mas completo).
    b) Escaneo rapido de un host.
    c) Detectar servidores corriendo de un host.
    d) Detectar versiones de los servicios corriendo en un host.
    e) Escanear un puerto especifico o un rango de puertos.
    f) Detectar el sistema operativo de un host.
    g) Enumerar los DNS de un host.
    h) Bypassear cloudflare.
    i) Salir.
    """)
    sel=input("Introduce tu opcion: ")
    if sel == "a":
        intensescan()
        menu()
    elif sel == "b":
        fastscan()
        menu()
    elif sel == "c":
        detectserv()
        menu()
    elif sel == "d":
        detectver()
        menu()
    elif sel == "e":
        escanport()
        menu()
    elif sel == "f":
        recsystem()
        menu()
    elif sel == "g":
        enumdns()
        menu()
    elif sel == "h":
        bypasscloud()
        menu()
    elif sel == "i":
        print ("Saliendo.")
    else:
        checker.cRojo("Opcion invalida.")
        menu()         
