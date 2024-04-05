<?php
// Vérifier si le formulaire a été soumis
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Récupérer le code saisi par l'utilisateur
    $code_saisi = $_POST['code'];

    // Récupérer le code envoyé par e-mail depuis votre système de stockage (base de données, fichier, etc.)
    $code_envoye = "123456"; // Remplacez cela par le code envoyé réel

    // Vérifier si le code saisi est un nombre
    if (is_numeric($code_saisi)) {
        // Comparer le code saisi avec le code envoyé
        if ((int)$code_saisi === (int)$code_envoye) {
            // Les codes correspondent, rediriger l'utilisateur vers la page de réinitialisation
            header('Location: reinitialiser.php');
            exit();
        } else {
            // Les codes ne correspondent pas, afficher un message d'erreur ou rediriger l'utilisateur vers une autre page
            echo "Le code saisi est incorrect.";
        }
    } else {
        // Le code saisi n'est pas un nombre, afficher un message d'erreur
        echo "Veuillez saisir un code numérique.";
    }
}
?>

<!DOCTYPE html>
<html>
<head>
    <title>Traitement de récupération de compte</title>
</head>
<body>
    <h1>Récupération de compte</h1>
    <form method="POST" action="traitement.php">
        <label for="code">Code de récupération :</label>
        <input type="number" name="code" id="code" required>
        <button type="submit">Valider</button>
    </form>
</body>
</html>
