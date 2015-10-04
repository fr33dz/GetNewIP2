#!/usr/bin/python
# -*- coding: utf-8 -*-
################################################################################
#                                                                              #
#                     Script [GetNewIp2] MLMConseil     		        	       #
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
import config, myip, bdd
from threading import Thread
import logging
from logging.handlers import RotatingFileHandler

class GetNewIp2(Thread):
	"""cette classe recupere l'adresse IP chaque tmp en seconde 
	et le comparre avec l'ancienne adresse IP, si l'adresse a changée 
	un message sera envoyé a l'dresse email avec cette nouvelle adresse
	la classe prends 4 parametres
	timer : temps d'actualisation de l'adresse IP
	"""
	def __init__(self, timer):
		Thread.__init__(self)
		self.arret = False
		self.timer = timer
		self.logger = logging.getLogger()
		self.logger.setLevel(logging.DEBUG)
		formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
		file_handler = RotatingFileHandler('getnewip.log', 'a', 1000000, 1)
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
				self.logger.info("le processus s'arrete pour %d seconde"%self.tmp)
				time.sleep(self.tmp)
			else:
				self.logger.info( "le processus vas executer une requete \n")
				b = bdd.bdd(HOST, PORT, DATABASE, USER, PASSWORD)
				b.connect()
				b.inserer(ID, ip_2)
				self.logger.warning("une nouvelle adresse a été ajoutée --> %s "%ip_2)
				ip_1 = ip_2

	def stop(self):
		self.logger.info("arret du service")
		self.arret = True

def main():
	g = GetNewIp2(120)
	g.start()
	# if sys.argv[1] == 'start':
	# 	g.start()
	# elif sys.argv[1] ==  'stop':
	# 	g.stop()
	# else:
	# 	print " \n main.py : Usage :  /etc/init.d/getnewip {start|stop} \n"
	pause = 300
	time.sleep(pause)
	g.stop()

	print "Exit apres %d seconde de mise en marche" %pause

if __name__ == '__main__':
    main()
