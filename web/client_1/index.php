<?php
/*
*  Configuration du Client
*/
define('ID',1);
define('PORT_ODOO','71');
/*
*  Configuration du serveur PostgreSQL
*/
define('HOST','127.0.0.1');
define('PORT',5432);
define('DATABASE','client');
define('USER', 'php');
define('PASSWORD', 'php');

/*
*  Connexion au serveur PostgreSQL
*/

$conn = pg_connect('host=' . HOST . ' port=' . PORT . ' dbname=' . DATABASE . ' user=' . USER . ' password=' . PASSWORD) or die('Connexion impossible : ' . pg_last_error());

/*
*  Requete au serveur PostgreSQL
*/

$result = pg_query($conn, "SELECT ipc,idc,name FROM client_ip WHERE idc=".ID) or die('Échec de la requête : ' . pg_last_error());


/*
*  Récuperation des données
*/


while ($row = pg_fetch_row($result)) {
   $idc =  $row[1];     //id du client
   $ipc = $row[0];              //ip du client
   $name = $row[2];             //nom du client
}

$ipc =$ipc.':'.PORT_ODOO;
$ipc = str_replace(' ','',$ipc);

echo "<center>";
echo "vous serez rediriger vers votre Serveur ODOO dans quelques secondes <br>";
echo "Si votre navigateur ne supporte pas la redirection automatique <br>";
echo "cliquez <a target='_blank' href='http:/\/".$ipc."'>ICI<a>";

echo "<br> --------------------------------------------------------<br>";
echo "<br> idc = ".$idc;
echo "<br> ipc = ".$ipc;
echo "<br> name = ".$name;
echo "</center>";
header('Location: http://'.$ipc);
exit();
?>

