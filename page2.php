<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <link rel="stylesheet" href="page1.css">
    <title>Inscripti</title>
    <style>
         input,select{
  display: inline-block;
  padding: 5px 15px;
  font-size: 12px;
  font-weight: bold;
  text-align: center;
  text-decoration: none;
  border-radius: 25px;
  cursor: pointer;

  display: flex;
  flex-direction: column;
  margin-bottom: 10px;
  margin-bottom: 15px;
}
    </style>
</head>

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
        <h1>Inscription</h1>
        <form action="" method="POST">
            <input type="email" name="Login" id="log" placeholder="Login" required>
            <input type="password" name="Password" id="pwd" placeholder="Password" required>
            <input type="password" name="Confirm_Password" placeholder="Confirm Password" required>
            <select name="Profil" id="Profil">
                <option value="Etudiant">Etudiant</option>
                <option value="Professeur">Professeur</option>
            </select>
            <div class="link">
                <a href="recuperation.php" id="forget">Mot de passe oublié ?</a>
                <a href="page1.php" id="inscription">Se connecter</a>
            </div>
            <input type="submit" value="S'inscrire" name="loginButton" class="valid">
        </form>
    </div>

    <?php
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $login = $_POST['Login'];
        $password = $_POST['Password'];
        $confirm = $_POST['Confirm_Password'];
        $profil = $_POST['Profil'];

        if ($profil === 'Professeur') {
            header('Location: pageprof1.php');
            exit();
        } else {
            // Traitement pour le profil "Etudiant" ou autre
            // Redirection vers la page correspondante
        }
    }
    ?>
</body>


</html>