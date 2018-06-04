#!/usr/bin/bash

ROOT_UID=0

function webhackreinstall() {
    if [ -f /etc/debian_version ] ; then
        echo -e "Procediendo con la reinstalación en tu sistema Debian o basado en Debian."
		cp -R * /opt/webhackshl/
		echo -e "Reinstalación finalizada, ahora puedes ejecutar el comando "webhackshl" directamente desde tu terminal.\n"

    elif [ -f /etc/arch-release ] ; then
		echo -e "Procediendo con la reinstalación en tu sistema ArchLinux o basado en ArchLinux."
		cp -R * /opt/webhackshl/
		echo -e "Reinstalación finalizada, ahora puedes ejecutar el comando "webhackshl" directamente desde tu terminal.\n"
	else
        echo -e "\nSistema no identificado, saliendo."
        exit
    fi
}

if [ "$UID" -ne "$ROOT_UID" ]; then
    esroot=false
    echo "Necesitas tener privilegios root o sudo para la instalación, saliendo..."
else
    esroot=true
	webhackreinstall
fi

