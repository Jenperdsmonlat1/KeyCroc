<?php

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
	$id = htmlspecialchars($_POST['id']);
	$password = htmlspecialchars($_POST['password']);

	if (!empty($id) AND !empty($password)) {
		$passwd_hashed = sha1($password);
		$req = $bdd->prepare('SELECT * FROM utilisateurs WHERE id = ? AND motdepasse = ?');
		$req->execute(array($id, $password));
		$user_exist = $req->rowCount();

		if ($user_exist == 1) {
			$info = $req->fetch();
			$_SESSION['Auth'] = array(
				'id' => $id,
				'password' => $password
			);
			header('Location: data.php');
		} else {
			$msg = 'Erreur mot de passe ou identifiant incorrect';
		}
	} else {
		$msg = 'Les champs ne sont pas tous rempli.';
	}
}

?>
<!DOCTYPE html>
<html>
<head>
	<title>Login</title>
	<meta charset="utf-8">
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
			<form method="post" action="">
				<label>Identifiant</label>
				<input type="text" name="id" placeholder="Votre identifiant" required>
				<label>Mot de passe</label>
				<input type="password" name="password" placeholder="Votre mot de passe" required>
				<input class="btn-grad" type="submit" name="submit" value="Valider">
			</form>
			<?php
			if (isset($msg)) {
				echo '<font style="color: red;">'.$msg.'</font>';
			}
			?>
		</div>
	</center>
</body>
</html>