<!DOCTYPE html>
<html>
<head>
    <title>Modifier un professeur</title>
</head>
<body>
    <h1>Modifier un professeur</h1>

    <?php
    // Vérifier si l'ID du professeur est passé en paramètre
    if (isset($_GET['id'])) {
        $id_professeur = $_GET['id'];

        // Connexion à la base de données
        $dsn = "mysql:host=localhost;dbname=gdn";
        $username = "root";
        $password = "";

        try {
            $db = new PDO($dsn, $username, $password);
            $db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            // Récupérer les détails du professeur
            $query = "SELECT * FROM professeurs WHERE ID_Professeur = :id";
            $stmt = $db->prepare($query);
            $stmt->bindValue(':id', $id_professeur);
            $stmt->execute();
            $professeur = $stmt->fetch(PDO::FETCH_ASSOC);

            if (!$professeur) {
                die("Professeur introuvable.");
            }

            // Traitement du formulaire de modification
            if ($_SERVER['REQUEST_METHOD'] === 'POST') {
                // Récupérer les nouvelles valeurs du formulaire
                $nom = $_POST['nom'];
                $prenom = $_POST['prenom'];
                $situation_matrimoniale = $_POST['situation_matrimoniale'];
                $lieu_naissance = $_POST['lieu_naissance'];
                $date_naissance = $_POST['date_naissance'];
                $diplome_formation = $_POST['diplome_formation'];
                $autre_diplome = $_POST['autre_diplome'];
                $matieres_enseignees = $_POST['matieres_enseignees'];
                $autre_matiere = $_POST['autre_matiere'];
                $login = $_POST['login'];
                $passwd = $_POST['passwd'];

                // Mettre à jour les informations du professeur dans la base de données
                $query = "UPDATE professeurs SET Nom_Professeur = :nom, Prenom_Professeur = :prenom, Situation_Matrimoniale = :situation_matrimoniale, Lieu_Naissance = :lieu_naissance, Date_Naissance = :date_naissance, Diplome_Formation = :diplome_formation, Autre_Diplome = :autre_diplome, Matieres_Enseignees = :matieres_enseignees, Autre_Matiere = :autre_matiere, Login_Professeur = :login, Passwd_Professeur = :passwd WHERE ID_Professeur = :id";
                $stmt = $db->prepare($query);
                $stmt->bindValue(':nom', $nom);
                $stmt->bindValue(':prenom', $prenom);
                $stmt->bindValue(':situation_matrimoniale', $situation_matrimoniale);
                $stmt->bindValue(':lieu_naissance', $lieu_naissance);
                $stmt->bindValue(':date_naissance', $date_naissance);
                $stmt->bindValue(':diplome_formation', $diplome_formation);
                $stmt->bindValue(':autre_diplome', $autre_diplome);
                $stmt->bindValue(':matieres_enseignees', $matieres_enseignees);
                $stmt->bindValue(':autre_matiere', $autre_matiere);
                $stmt->bindValue(':login', $login);
                $stmt->bindValue(':passwd', $passwd);
                $stmt->bindValue(':id', $id_professeur);

                $stmt->execute();

                echo "Les informations du professeur ont été mises à jour avec succès.";
            }
        } catch (PDOException $e) {
            die("Erreur : " . $e->getMessage());
        }
    } else {
        die("ID du professeur non spécifié.");
    }
    ?>

    <!-- Formulaire de modification -->
    <form method="POST" action="">
        <label for="nom">Nom:</label>
        <input type="text" id="nom" name="nom" value="<?php echo $professeur['Nom_Professeur']; ?>"><br>

        <label for="prenom">Prénom:</label>
        <input type="text" id="prenom" name="prenom" value="<?php echo $professeur['Prenom_Professeur']; ?>"><br>

        <label for="situation_matrimoniale">Situation Matrimoniale :</label>
        <input type="text" id="situation_matrimoniale" name="situation_matrimoniale" list="marital_status" required><br>
        <datalist id="marital_status">
        <option value="Célibataire">
        <option value="Marié(e)">
        <option value="Veuf(ve)">
        </datalist>

        <label for="lieu_naissance">Lieu de Naissance:</label>
        <input type="text" id="lieu_naissance" name="lieu_naissance" value="<?php echo $professeur['Lieu_Naissance']; ?>"><br>

        <label for="date_naissance">Date de Naissance:</label>
        <input type="text" id="date_naissance" name="date_naissance" value="<?php echo $professeur['Date_Naissance']; ?>"><br>

        <label for="diplome_formation">Diplôme de Formation:</label>
        <input type="text" id="diplome_formation" name="diplome_formation" value="<?php echo $professeur['Diplome_Formation']; ?>"><br>

        <label for="autre_diplome">Autre Diplôme:</label>
        <input type="text" id="autre_diplome" name="autre_diplome" value="<?php echo $professeur['Autre_Diplome']; ?>"><br>

        <label for="matieres_enseignees">Matières Enseignées:</label>
        <input type="text" id="matieres_enseignees" name="matieres_enseignees" value="<?php echo $professeur['Matieres_Enseignees']; ?>"><br>

        <label for="autre_matiere">Autre Matière:</label>
        <input type="text" id="autre_matiere" name="autre_matiere" value="<?php echo $professeur['Autre_Matiere']; ?>"><br>

        <label for="login">Login:</label>
        <input type="text" id="login" name="login" value="<?php echo $professeur['Login_Professeur']; ?>"><br>

        <label for="passwd">Mot de passe:</label>
        <input type="password" id="passwd" name="passwd" value="<?php echo $professeur['Passwd_Professeur']; ?>"><br>

        <input type="submit" value="Enregistrer">
    </form>

    <a href="gestion_professeurs.php"><button>Retour</button></a>

</body>
</html>