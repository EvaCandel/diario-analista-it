#!/bin/bash
echo "==========================="
echo " COMPROBANDO RED INTERNA Y EXTERNA "
echo "==========================="
echo "Haciendo ping a Google (Internet)..."
ping -c 2 google.com
echo "---------------------------"
echo "Haciendo ping a DNS secundario..."
ping -c 2 1.1.1.1
echo "==========================="
echo " DIAGNOSTICO FINALIZADO "
echo "==========================="
