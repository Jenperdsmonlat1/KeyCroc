<?php

$host = '';
$db_name = '';
$db_user = '';
$db_password = '';

try {
	$bdd = new PDO('mysql:host='.$host.';dbname='.$db_name.';charset=utf8', $db_user, $db_password);
	$bdd->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	$bdd->exec("CREATE TABLE IF NOT EXISTS logger(
		id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
		utilisateur VARCHAR(255) NOT NULL,
		log TEXT NOT NULL,
		dates VARCHAR(255) NOT NULL,
		heure VARCHAR(255) NOT NULL
		)"
	);

	$bdd->exec("CREATE TABLE IF NOT EXISTS admin_info(
		id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
		utilisateur VARCHAR(255) NOT NULL,
		motdepasse VARCHAR(255) NOT NULL
		)"
	);
} catch (Exception $e) {
	die('Erreur: '.$e->getMessage());
}

if (isset($_POST['submit'])) {
	$user = htmlspecialchars($_POST['utilisateur']);
	$date = htmlspecialchars($_POST['date']);
	$heure = htmlspecialchars($_POST['heure']);
	$log = htmlspecialchars($_POST['log']);

	if (!empty($user) AND !empty($date) AND !empty($heure) AND !empty($log)) {
		$req = $bdd->prepare('INSERT INTO logger(utilisateur, log, dates, heure) VALUES(:utilisateur, :log, :dates, :heure)');
		$req->execute(
			array(
				'utilisateur' => $user,
				'log' => $log,
				'dates' => $date,
				'heure' => $heure,
			)
		);
	} else {
		$msg = "Erreur tous les champs n'ont pas été rempli.";
	}
}
?>
<!DOCTYPE html>
<html>
<head>
	<title>Report</title>
	<meta charset="utf-8">
	<meta http-equiv="Content-Language" content="fr-FR" />
    <meta name="author" content="jesuisroot123">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="viewport" content="width=device-width, minimum-scale=0.25"/>
    <meta name="viewport" content="width=device-width, maximum-scale=5.0"/>
    <meta name="viewport" content="width=device-width, target-densitydpi=device-dpi"/>
    <meta name="description" content="Administration de KeyCroc">
    <link rel="stylesheet" type="text/css" href="stylesheets_report/style.css">
    <link rel="stylesheet" type="text/css" href="stylesheets_report/formulaire_style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Yaldevi:wght@200&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
</head>
<body>
	<center>
		<div class="container">
			<h1>Connexion</h1>
			<form method="post" action="">
				<input type="text" name="utilisateur" placeholder="Nom de l'utilisateur." required>
				<input type="text" name="date" placeholder="La date." required>
				<input type="text" name="heure" placeholder="L'heure." required>
				<input type="text" name="log" placeholder="Le log." required>
				<input class="btn-grad" type="submit" name="submit" value="Valider">
			</form>
			<?php
			if (isset($msg)) {
				echo '<font style="red";>'.$msg."</font>";
			}
			?>
		</div>
	</center>
</body>
</html>
