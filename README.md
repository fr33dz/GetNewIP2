## GetNewIP2
permet de recuperer l'dresse Ip d'une machine et lenvoyée vers une base de donneés PostgreSQL
################################################################################
#                                                                              #
#                     Script [GetNewIP2] MLMConseil                             #
#                    ----------------------------------                        #
#                      permet d'actualiser l'adresse IP                        #
#                    et l'envoyée vers une adresse Email                       #
#                    ----------------------------------                        #
#          				                                       #
#                 -----------------------------------------                    #
#                       langage : Python 2.7                                   #
#                       date creation : 30/09/2015                             #
#                       date modification : /08/2015                           #
#                       version : 0.1                                          #
#                       auteur  : Bouslahi Yacine                              #
#                                                                              #
################################################################################

Utilisation 

1.Configuration :

	dans le repertoire getnewip2 , editer le ficher config.py 
	
########################## POSTGRESQL CONFIG

HOST = '127.0.0.1'
PORT = 5432
DATABASE = 'client'
USER = 'php'    		#'openpg'
PASSWORD = 'php'		#'openpgpwd'

########################## CLIENT CONFIG

ID = 1 # Identifiant du client
TIMER = 120 # temps d'actualisation de l'adresse IP


2.Installation

su 
chmod 755 install.sh
./install.sh
