<?php

session_start();

$host = '';
$db_name = '';
$db_user = '';
$db_password = '';

try {
	$bdd = new PDO('mysql:host='.$host.';dbname='.$db_name.';charset=utf8', $db_user, $db_password);
} catch (Exception $e) {
	die('Erreur: '.$e->getMessage());
}

if (isset($_POST['submit'])) {
	$user = htmlspecialchars($_POST['utilisateur']);
	$password = htmlspecialchars($_POST['password']);
	$passwd_hashed = sha1($password);

	if (!empty($user) AND !empty($password)) {
		$req = $bdd->prepare('SELECT * FROM admin_info WHERE utilisateur = ? AND motdepasse = ?');
		$req->execute(array($user, $passwd_hashed));
		$userexist = $req->rowCount();

		if ($userexist == 1) {
			$_SESSION['Auth'] = array(
				'User' => $user,
				'Password' => $password
			);

			$user_info = $req->fetch();
			$_SESSION['id'] = $user_info['id'];
			header('Location: logs.php');
		} else {
			$msg = "Mauvais identifiant ou mot de passe.";
		}
	} else {
		$msg = "Tous les champs doivent être remplit.";
	}
}
?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Connexion</title>
	<meta http-equiv="Content-Language" content="fr-FR" />
    <meta name="author" content="jesuisroot123">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="viewport" content="width=device-width, minimum-scale=0.25"/>
    <meta name="viewport" content="width=device-width, maximum-scale=5.0"/>
    <meta name="viewport" content="width=device-width, target-densitydpi=device-dpi"/>
    <meta name="description" content="Administration de KeyCroc">
    <link rel="stylesheet" type="text/css" href="stylesheets_admin/style.css">
    <link rel="stylesheet" type="text/css" href="stylesheets_admin/formulaire_style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
	<link href="https://fonts.googleapis.com/css2?family=Yaldevi:wght@200&display=swap" rel="stylesheet">
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
</head>
<body>
	<center>
		<div class="container">
			<h1>Connexion</h1>
			<form method="POST" action="">
				<input type="text" name="utilisateur" placeholder="Nom d'utilisateur" required>
				<input type="password" name="password" placeholder="Mot de passe" required>
				<input class="btn-grad" type="submit" name="submit" value="Valider">
			</form>
			<?php
			if (isset($msg)) {
				echo '<font style="color: red">'.$msg.'</font>';
			}
			?>
		</div>
	</center>
</body>
</html>
