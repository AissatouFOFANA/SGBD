<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Récupération de compte email</title>
    <link rel="stylesheet" href="recuperation.css">
</head>
<body>
    <div class="background-circle"></div>
    <div class="small-circle"></div>
    <div class="small-circle1"></div>
    <div class="container">
        <h1>Récupération de compte email</h1>
        <p>Veuillez entrer l'adresse email associée à votre compte :</p>
        <form action="recuperation.php" method="GET">
            <input type="email" name="email" placeholder="Votre adresse email" required>
           <a href="saisiecode.php">
               <button type="submit">Envoyer un code de récupération</button>    
           </a>
        </form>
       <?php
// Fonction pour générer un code de récupération aléatoire
function generateRecoveryCode() {
    // Générez un code unique selon vos besoins (par exemple, un code aléatoire à 6 chiffres)
    return rand(100000, 999999);
}

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    if (isset($_GET['email'])) {
        $email = $_GET['email'];

        // Génération du code de récupération
        $code = generateRecoveryCode();

        // Adresse e-mail de l'utilisateur
        $userEmail = $email;

        // Envoi du code de récupération par e-mail
        $to='.$userEmail';
        $subject = 'Code de récupération de compte';
        $message = 'Votre code de récupération est : ' . $code;
        $headers = 'From: noreply@example.com' . "\r\n" .
                   'Reply-To: noreply@example.com' . "\r\n" .
                   'X-Mailer: PHP/' . phpversion();

        if (mail($userEmail, $subject, $message, $headers)) {
            // L'e-mail a été envoyé avec succès
            echo 'Le code de récupération a été envoyé à votre adresse e-mail.';
        } else {
            // Une erreur s'est produite lors de l'envoi de l'e-mail
            echo 'Une erreur s\'est produite lors de l\'envoi du code de récupération.';
        }
        header('location:saisiecode.php');
        exit;
    }
}
?>

    </div>
</body>
</html>
