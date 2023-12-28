#! /bin/bash

#EXIBE MENU DE ESCOLHA
OPC=$(dialog --menu "Programs essencials: " 0 0 0 \
1 "TAKE A PICTURE" \
2 "DETECT EMOTION FROM IMAGE" \
3 "LIVE EMOTION DETECTION" \
4 "EXIT FROM PROGRAM"  --stdout)


case $OPC in

	1)
	python picture.py
	bash face.sh;;

	2)
	python imgdetect.py
	bash face.sh;;

	3)
	python livedetect.py
	bash face.sh;;

	*)
	clear

esac
