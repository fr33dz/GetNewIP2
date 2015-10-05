#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                                                                              #
#                     Script [GetNewIp2] MLMConseil   		               #
#                    ----------------------------------                        #
#                      permet d'actualiser l'adresse IP                        #
#                    et l'envoyée vers une base de données                     #
#                    ----------------------------------          	       #
#		Ce fichier permet d'inserer  l'Adresse IP vers la base de donnees      #
#                    ---------------------------------- 	       	       #									   #
#                                                                              #
#                       langage : Python 2.7                                   #
#                       date creation : 01/09/2015                             #
#                       date modification : /10/2015                           #
#                       version : 0.2                                          #
#                       auteur  : Bouslahi Yacine                              #
#                                                                              #
################################################################################
import psycopg2
import sys

class bdd():
	def __init__(self, host, port, database, user, password):
		self.host = host
		self.port = port
		self.database = database
		self.user = user
		self.password = password
		conn = None

	
	def inserer(self, idc, ipc):
		"""" ipc : @Adresse IP 
			idc : id du client"""
		
		con =  None
		try:
	    		con = psycopg2.connect(host=str(self.host), port=self.port ,database=str(self.database), user=str(self.user), password=str(self.password))
				cur = con.cursor()
			try:
				req = "UPDATE client_ip SET ipc= '{0}' WHERE idc={1}".format(ipc, idc)  
    			cur.execute(req)
	
			except Exception as err:
				print "Erreur lors de l'execution de la requete : %s" %err
				return False 
				sys.exit(1)
 					
		except psycopg2.DatabaseError, e:
    			print 'Error %s' % e
    			sys.exit(1)

		finally:

    			if con:
				con.commit()
        			con.close()
				return True


def main():

	b = bdd('192.168.1.10', 5433, 'client','php', 'php')
	b.inserer(1,'192.168.1.3')
	
if __name__ == "__main__":
	main()
