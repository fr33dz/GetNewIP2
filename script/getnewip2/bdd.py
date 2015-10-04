#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                                                                              #
#                     Script [GetNewIp2] MLMConseil     		               #
#                    ----------------------------------                        #
#                      permet d'actualiser l'adresse IP                        #
#                    et l'envoyée vers une base de données                     #
#                    ----------------------------------						   #
#		Ce fichier permet d'inserer  l'Adresse IP vers la base de donnees      #
#                    ---------------------------------- 					   #									   #
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
	def __init__(self, host, dbname, user, password):
		self.host = host
		self.dbname = dbname
		self.user = user
		self.password = password
		self.conn = None

	def connect(self):
		conn_string = "host=\'"+str(sys.argv[1])+"\' dbname=\'"+str(sys.argv[2])+"\' user=\'"+str(sys.argv[3])+"\' password=\'"+str(sys.argv[4])+"\'"

		print "Connecting to database\n	->%s" % (conn_string)
 
		# connection vers le serveur
		try:
			self.conn = psycopg2.connect(conn_string)
			return True
		except:
			print "Une erreur est survenue lors de la connexion a la base de données.\n"
			return False

	def inserer(self, idc, ipc):
		"""" ipc : @Adresse IP 
			 idc : id du client"""
		cursor = self.conn.cursor()
 		# requete
 		req = "UPDATE client_ip SET ip = "+str(ipc)+" WHERE id="+str(idc)
		up = cursor.execute(req)
		self.conn.commit()
		self.conn.close()
		if up:
			return True
		else:
			return False

def main():

	conn_string = "host=\'"+str(sys.argv[1])+"\' dbname=\'"+str(sys.argv[2])+"\' user=\'"+str(sys.argv[3])+"\' password=\'"+str(sys.argv[4])+"\'"
	b = bdd(host, dbname, user, password)
	b.connect()
	if b.inserer('192.168.1.123',1):
		print "La requête a été exécutée avec succès"
	else:
		print "probleme d'inssertion"

if __name__ == "__main__":
	main()
