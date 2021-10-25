<?php

session_start();

if (!empty($_SESSION['Auth']['User']) AND !empty($_SESSION['Auth']['Password'])) {

} else {
	header('Location: index.php');
}

$host = '';
$db_name = '';
$db_user = '';
$db_password = '';

try {
	$bdd = new PDO('mysql:host='.$host.";dbname=".$db_name.";charset=utf8", $db_user, $db_password);
} catch (Exception $e) {
	die('Erreur: '.$e->getMessage());
}

$req = $bdd->query('SELECT * FROM logger ORDER BY id');

while ($donnees = $req->fetch())
{
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Logs</title>
	<meta http-equiv="Content-Language" content="fr-FR" />
    <meta name="author" content="jesuisroot123">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="viewport" content="width=device-width, minimum-scale=0.25"/>
    <meta name="viewport" content="width=device-width, maximum-scale=5.0"/>
    <meta name="viewport" content="width=device-width, target-densitydpi=device-dpi"/>
    <meta name="description" content="Administration de KeyCroc">
    <link rel="stylesheet" type="text/css" href="stylesheets_admin/style.css">
    <link rel="stylesheet" type="text/css" href="stylesheets_admin/log_style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Yaldevi:wght@200&display=swap" rel="stylesheet">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
	<link href='https://unpkg.com/boxicons@2.0.9/css/boxicons.min.css' rel='stylesheet'>
</head>
<body>
	<?php include('sidebar.php'); ?>

	<center>
		<div class="container_central">
			<div class="container_data">
				<h4>
					Utilisateur: <?php echo $donnees['utilisateur']; ?><br>
					Le: <?php echo $donnees['dates']; ?><br>
					A: <?php echo $donnees['heure']; ?><br>
					Log: <?php echo $donnees['log']; ?><br>
				</h4>
			</div>
		</div>
	</center>
</body>
</html>
<?php
}

$req->closeCursor();
?>
