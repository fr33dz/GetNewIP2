#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                                                                              #
#                     Script [GetNewIp2] MLMConseil                            #
#                    ----------------------------------                        #
#                      permet d'actualiser l'adresse IP                        #
#                    et l'envoyée vers une base de données                     #
#                    ----------------------------------			       #
#		Ce fichier permet de recuperer l'Adresse I		       #
#                    ---------------------------------- 		       #									   #
#                                                                              #
#                       langage : Python 2.7                                   #
#                       date creation : 01/09/2015                             #
#                       date modification : /10/2015                           #
#                       version : 0.1                                          #
#                       auteur  : Bouslahi Yacine                              #
#                                                                              #
################################################################################
from urllib2 import urlopen

def myip():
	return urlopen('http://ip.42.pl/raw').read()
