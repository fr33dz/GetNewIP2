#!/bin/bash
#/etc/init.d/getnewip
################################################################################
#                                                                              #
#                     Script [GetNewIp2] MLMConseil                            #
#                    ----------------------------------                        #
#                      permet d'actualiser l'adresse IP                        #
#                    et l'envoyée vers une base de données                     #
#                    ----------------------------------                        #
#           Ce fichier permet d'ajouter le script /usr/src/getnewip2/main.py   #
#                               comme service.                                  #
#                 -----------------------------------------                    #
#                       langage : Python 2.7                                   #
#                       date creation : 30/09/2015                             #
#                       date modification : /08/2015                           #
#                       version : 0.2                                          #
#                       auteur  : Bouslahi Yacine                              #
#                                                                              #
################################################################################
#
RUN=0
case "$1" in
  start)
    echo "Starting script GetNewIP2 "
    RUN=1
    python /usr/src/getnewip2/main.py start &
    ;;
  stop)
    echo "Stopping script GetNewIP2"
    RUN=0
    python /usr/src/getnewip2/main.py stop &
    ;;
  status)
    if [ $RUN -eq 0 ]
    then
    	return 0
    	exit 1
    else
	    return 1
	    exit 1
    fi
    ;;
  *)
    echo "Usage: /etc/init.d/getnewip2 {start|stop}"
    exit 1
    ;;
esac

exit 0
