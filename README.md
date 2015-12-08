### GetNewIP2
	Permet de récupérer l'adresse IP d'une machine et l'envoyée vers une base de données PostgreSQL
	le client X accede avec son navigateur à exemple.dz/client_X , et sera redirigé vers son serveur ODOO 
----------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------                                                                              
                     Script [GetNewIP2] MLMConseil                             
                    ----------------------------------                        
                     permet d'actualiser l'adresse IP                        
                    et l'envoyée vers une adresse Email                       
                    ----------------------------------                        
          				                                       
                -----------------------------------------                    
                       langage : Python 2.7                                   
                       date creation : 30/09/2015                             
                       date modification : /08/2015                           
                       version : 0.1                                          
                       auteur  : Bouslahi Yacine                              
                                                                              
--------------------------------------------------------------
### 1.Fonctionnement

	getnewip2.sh : permet d'ajouter le script comme service , il se trouve dans le répertoire  /etc/init.d/ , usage :       	/etc/init.d/getnewip2.sh {start | stop}
	install.sh : permet d'installer le script.
	main.py : le programme principale du script.
	bdd.py : s'occupe de l'envoi des données vers la base de données.
	myip.py : récupère l'adresse IP de la machine.
	getnewip2.log : fichier log pour le script, se trouve dans le répertoire  /var/log/
	test_connect : Ce fichier permet de tester la connexion à la base de donneés
	README.md : fichier en texte qui explique le fonctionnement , l'utilisation et la configuration du Script



#### 2.Configuration :

	I.dans le repertoire /script/getnewip2/ , editer le fichier config.py 
	

	HOST = '127.0.0.1'
	PORT = 5432
	DATABASE = 'client'
	USER = 'php'    		#'openpg'
	PASSWORD = 'php'		#'openpgpwd'


	ID = 1 # Identifiant du client
	TIMER = 120 # temps d'actualisation de l'adresse IP
	
	II. dans le repertoire /web/client_x/, editez le fichier index.php
	
	define('ID',1);
	define('PORT_ODOO','8069');
	
	define('HOST','127.0.0.1');
	define('PORT',5432);
	define('DATABASE','client');
	define('USER', 'php');
	define('PASSWORD', 'php');


#### 3.Installation
	I. Script Python coté client.
		su 
		chmod 755 install.sh
		./install.sh

	II. Script PHP coté serveur.
		cp /client_1/index.php /var/www/html/

#### 4. Desinstallation
	update-rc.d -f getnewip2 remove
	rm /etc/init.d/getnewip2.sh 
	rm -R /usr/src/getnewip2/

