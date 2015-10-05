#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                                                                              #
#                     Script [GetNewIp2] MLMConseil     	 	       #
#                    ----------------------------------                        #
#                      permet d'actualiser l'adresse IP                        #
#                    et l'envoyée vers une base de données                     #
#                    ----------------------------------                        #
#                                                                              #
#                       langage : Python 2.7                                   #
#                       date creation : 01/09/2015                             #
#                       date modification : /10/2015                           #
#                       version : 0.1                                          #
#                       auteur  : Bouslahi Yacine                              #
#                                                                              #
################################################################################
import sys, os, time
import myip, bdd
from config import *
from threading import Thread
import logging
from logging.handlers import RotatingFileHandler

class GetNewIp2(Thread):
	"""cette classe recupere l'adresse IP chaque timer en seconde 
	et le comparre avec l'ancienne adresse IP, si l'adresse a changée 
	une requete sera envoyé vers une base de données PostgreSQL avec cette nouvelle adresse
	la classe prends 7 parametres
	host : Adresse IP de la base de données PostgreSQL
	port : port de connexion  
	database : nom de la base de données
	user : nom de l'utilisateur de la base de données
	password : mot de passe de l'utilisateur de la base de donnéestemps d'actualisation de l'adresse IP
	id : identifiant du client 
	timer : temps en secondes
	"""
	def __init__(self, host, port, database, user, password, id, timer):
		Thread.__init__(self)
		self.arret = False
		self.timer = timer
		self.id = id
		self.host = host
		self.port = port
		self.database = database
		self.user = user
		self.password = password
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.DEBUG)
		formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
		file_handler = RotatingFileHandler('/var/log/getnewip2.log', 'a', 1000000, 1)
		file_handler.setLevel(logging.DEBUG)
		file_handler.setFormatter(formatter)
		self.logger.addHandler(file_handler)

	def run(self):
		self.logger.info("démarrage du service")
		ip_1 = '0.0.0.0'
		ip_2 = '0.0.0.0'

		while not self.arret:
			try:
				ip_2 = str(myip.myip())
			except:
				self.logger.warning('pas de connexion... tentative de reconnexion dans  1 minute')
				time.sleep(60)

			if ip_1 == ip_2:
				self.logger.info("le processus s'arrete pour %d seconde"%self.timer)
				time.sleep(self.timer)
			else:
				self.logger.info( "le processus vas executer une requete \n")
				b = bdd.bdd(self.host, self.port, self.database, self.user, self.password)
				info = str(self.host)+" | " +str(self.port)+" | "+str(self.database)+" | "+str(self.user)+" --\n "
				req = b.inserer(self.id, ip_2)
				if req:
					self.logger.info("une nouvelle adresse a été ajoutée dans la base de données:  --> %s"%ip_2)
				else:
					self.logger.warning("Probleme dans la requete --> %s"%info)
				ip_1 = ip_2

	def stop(self):
		self.logger.info("arret du service")
		self.arret = True

def main():
	g = GetNewIp2(HOST, PORT, DATABASE, USER, PASSWORD, ID, TIMER)
	if sys.argv[1] == 'start':
		g.start()
	elif sys.argv[1] ==  'stop':
		g.stop()
	else:
		print " \n main.py : Usage :  /etc/init.d/getnewip {start|stop} \n"

if __name__ == '__main__':
    main()
