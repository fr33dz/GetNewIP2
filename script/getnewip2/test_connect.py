#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                                                                              #
#                     Script [GetNewIp2] MLMConseil                            #
#                    ----------------------------------                        #
#                      permet d'actualiser l'adresse IP                        #
#                    et l'envoyée vers une base de données                     #
#                    ----------------------------------                        #
#        Ce fichier permet de tester la connexion à la base de donneés         #
#                    ----------------------------------                        #                                       #
#                                                                              #
#                       langage : Python 2.7                                   #
#                       date creation : 01/09/2015                             #
#                       date modification : /10/2015                           #
#                       version : 0.1                                          #
#                       auteur  : Bouslahi Yacine                              #
#                                                                              #
################################################################################
import psycopg2
import sys
from config import *     

con = None

try:
     
    con = psycopg2.connect(host=HOST, port=PORT ,database=DATABASE, user=USER, password=PASSWORD) 
    cur = con.cursor()
    try:
        cur.execute('SELECT version()')          
        ver = cur.fetchone()
        print ver
    except Exception as err:
        print "Probleme de requete :  %s"%err  
    

except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
      con.close()
