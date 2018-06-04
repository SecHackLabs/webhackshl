#!/usr/bin/bash
  
ROOT_UID=0

function uninstall() {
	echo -e "Desinstalando WebHackSHL..."
	rm -rf /opt/webhackshl/
	rm -f /usr/bin/webhackshl
	echo -e "\nDesinstalación finalizada."
}

if [ "$UID" -ne "$ROOT_UID" ]; then
    esroot=false
    echo "Necesitas tener privilegios root o sudo para desinstalar la herramienta."
else
    esroot=true
    uninstall
fi
