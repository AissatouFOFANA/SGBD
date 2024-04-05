<?php
// Vérifier si l'identifiant de l'enseignant est passé en paramètre
if (isset($_GET['id'])) {
  // Récupérer l'identifiant de l'enseignant
  $enseignantId = $_GET['id'];

  // Se connecter à la base de données
  $host = 'localhost';
  $username = 'root';
  $password = 'passer';
  $database = 'gdn';

  $conn = new mysqli("localhost", "root", "", "gdn");

  // Vérifier si la connexion à la base de données a réussi
  if ($conn->connect_error) {
    die("Erreur de connexion à la base de données : " . $conn->connect_error);
  }

  // Supprimer l'enseignant de la base de données
  $query = "DELETE FROM enseignant WHERE id = $enseignantId";

  if ($conn->query($query) === TRUE) {
    echo "Enseignant supprimé avec succès.";
  } else {
    echo "Erreur lors de la suppression de l'enseignant : " . $conn->error;
  }

  // Fermer la connexion à la base de données
  $conn->close();
} else {
  echo "Identifiant de l'enseignant non spécifié.";
}
?>