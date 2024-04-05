<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Authentification</title>
    <link rel="stylesheet" href="page1.css">
</head>

</html>

<body>
    <div class="background-circle"></div>
    <div class="small-circle"></div>
    <div class="small-circle1"></div>
    <div class="container">
        <div class="logo">
            <img src="R-removebg-preview.png" alt="Logo Université Cheikh Anta Diop">
        </div>
        <div class="user-icon">
            <img src="user_icon.png" alt="user-icon">
        </div>
        <h1>Authentification</h1>
        <input type="email" name="Login" id="log" placeholder="Login">
        <input type="password" name="Password" id="pwd" placeholder="Password">
        <div class="link">
            <a href="recuperation.php" id="forget">Mot de passe oublié ?</a>
            <a href="page2.php" id="inscription">S'inscrire</a>
        </div>
        <a href="pageprof1.php">
            <input type="button" value="Se connecter" name="loginButton" class="valid">
        </a>
    </div>
    <?php

$profil = $_POST['Profil'];// Récupérer le profil de l'utilisateur à partir de la base de données

// Effectuer la redirection en fonction du profil
if ($profil === 'Professeur') {
    header('Location: pageprof1.php');
    exit();
}// else {
   // header('Location: pageetudiant.php');
    //exit();
//}
?>

    
</body>

</html>