#!/bin/bash

# Vérification du port 80
if netstat -tuln | grep ':80 ' > /dev/null; then
    echo "Le port 80 est ouvert et en écoute."
else
    echo "Le port 80 n'est pas ouvert ou n'est pas en écoute."
fi
