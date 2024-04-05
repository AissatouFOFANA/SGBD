<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="recuperationinfo.css">
    <title>Bulletin Eleve</title>
</head>
<body>
    <div class="background-circle"></div>
    <div class="small-circle"></div>
    <div class="small-circle1"></div>
    <div class="container">
    <h1>Notes des élèves</h1>

    <?php
    // Informations de connexion à la base de données
    $servername = "localhost";
    $username = "root";
    $password = "";
    $dbname = "gdn";

    // Connexion à la base de données
    $conn = new mysqli($servername, $username, $password, $dbname);

    // Vérification de la connexion
    if ($conn->connect_error) {
        die("La connexion a échoué : " . $conn->connect_error);
    }

    // Requête SQL pour récupérer les notes des élèves avec leur classe et les matières
    $sql = "SELECT eleves.nom AS nom_eleve, classes.nom AS nom_classe, matieres.nom AS nom_matiere, notes.note_tp, notes.note_cc, notes.note_ds
            FROM notes
            INNER JOIN eleves ON notes.eleve_id = eleves.id
            INNER JOIN classes ON eleves.classe_id = classes.id
            INNER JOIN matieres ON notes.matiere_id = matieres.id";
    $result = $conn->query($sql);

    // Vérification des résultats de la requête
    if ($result->num_rows > 0) {
        // Variables pour stocker les informations de l'élève en cours
        $current_eleve = "";
        $current_classe = "";

        // Affichage des notes pour chaque élève
        while ($row = $result->fetch_assoc()) {
            // Vérification si l'élève a changé
            if ($current_eleve !== $row["nom_eleve"]) {
                $current_eleve = $row["nom_eleve"];
                echo "<h2>Élève : " . $current_eleve . "</h2>";
                echo "<p>Classe : " . $row["nom_classe"] . "</p>";
            }

            // Affichage des notes par matière
            echo "<h3>Matière : " . $row["nom_matiere"] . "</h3>";
            echo "<p>TP : " . $row["note_tp"] . "</p>";
            echo "<p>CC : " . $row["note_cc"] . "</p>";
            echo "<p>DS : " . $row["note_ds"] . "</p>";
        }
    } else {
        echo "Aucune note trouvée.";
    }

    // Fermeture de la connexion à la base de données
    $conn->close();
    ?>

</body>
</html>