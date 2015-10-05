#!/bin/sh
################################################################################
#                                                                              #
#                     Script [GetNewIp2] MLMConseil                            #
#                    ----------------------------------                        #
#                      permet dactualiser l'adresse IP                         #
#                    et l'envoyée vers une adresse Email                       #
#                    ----------------------------------                        #
#                  Ce fichier permet d'installer le Script                     #
#                  ---------------------------------------                     #
#                       langage : Python 2.7                                   #
#                       date creation : 30/09/2015                             #
#                       date modification : /08/2015                           #
#                       version : 0.2                                          #
#                       auteur  : Bouslahi Yacine                              #
#                                                                              #
################################################################################

echo "------------------------Debut d'installation--------------------------- "
cp -R getnewip2/ /usr/src/
chmod -R 777 /usr/src/getnewip2/
cp getnewip2.sh /etc/init.d/
cd /etc/init.d/
chmod 755 getnewip2.sh
update-rc.d getnewip2.sh defaults
/etc/init.d/getnewip2.sh start
echo "------------------------Fin d'installation-----------------------------"
echo "Usage: /etc/init.d/getnewip2 {start|stop}"
exit 1
