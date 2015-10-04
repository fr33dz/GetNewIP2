#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                                                                              #
#                     Script [GetNewIp2] MLMConseil   		        	       #
#                    ----------------------------------                        #
#                      permet d'actualiser l'adresse IP                        #
#                    et l'envoyée vers une base de données                     #
#                    ----------------------------------    					   #
#                   Ce fichier sert a configurer le script                     #
#                  ----------------------------------------                    #
#                       langage : Python 2.7                                   #
#                       date creation : 01/10/2015                             #
#                       date modification : /10/2015                           #
#                       version : 0.2                                          #
#                       auteur  : Bouslahi Yacine                              #
#                                                                              #
################################################################################



########################## POSTGRESQL CONFIG

HOST = '192.168.1.10'		#'127.0.0.1'
PORT = 5433					#5432
DATABASE = 'client'
USER = 'php'    		#'openpg'
PASSWORD = 'php'		#'openpgpwd'

########################## CLIENT CONFIG

ID = 1 # Identifiant du client
TIMER = 120 # temps d'actualisation de l'adresse IP
