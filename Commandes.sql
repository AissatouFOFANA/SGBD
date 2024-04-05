CREATE TABLE etudiant (
  IdEtu int PRIMARY KEY AUTO_INCREMENT,
  nom varchar(50),
  prenom varchar(50),
  DateNaissance varchar(50),
  AdresseMail varchar(50),
  specialisation varchar(50)
);

CREATE TABLE cours (
  Code int PRIMARY KEY,
  nom varchar(50),
  description varchar(50),
  NombreCredit int,
  ProfesseurIntervenant varchar(50)
);

CREATE TABLE FicheEvaluation (
  IdEtu int,
  Code varchar(50),
  DateEvaluation date,
  commentaires varchar(50),
  FOREIGN KEY (IdEtu) REFERENCES etudiant(IdEtu),
  FOREIGN KEY (Code) REFERENCES cours(Code)
);

CREATE TABLE classe (
  Code_classe int PRIMARY KEY,
  nom varchar(50),
  Responsable_classe varchar(50)
);

CREATE TABLE DirecteurEtudes (
  nom varchar(50),
  prenom varchar(50),
  AdresseMail varchar(50),
  Telephone varchar(50)
);

CREATE TABLE departement (
  code int PRIMARY KEY,
  nom_departement varchar(50),
  chef_departement varchar(50)
);

CREATE TABLE CahierTexte (
  libelle varchar(50),
  date_cours date,
  programme varchar(50)
);

CREATE TABLE ChefDepartement (
  nom varchar(50),
  prenom varchar(50),
  AdresseMail varchar(50),
  telephone varchar(50)
);

CREATE TABLE CommissionPedagogique (
  nom varchar(50),
  membres varchar(50)
);

INSERT INTO etudiant (IdEtu, nom, prenom, DateNaissance, AdresseMail, specialisation) VALUES (1, "Magatte", "Diawara", "21-10-2003", "magattediawara@esp.sn", "Genie-logiciel");

INSERT INTO etudiant (IdEtu, nom, prenom, DateNaissance, AdresseMail, specialisation) VALUES (2, "Boubacar", "Diouf", "02-01-2003", "boubacardiouf@esp.sn", "Genie-logiciel");

INSERT INTO etudiant (IdEtu, nom, prenom, DateNaissance, AdresseMail, specialisation) VALUES (3, "Aissatou", "Fofana", "04-01-2004", "aissatoufofana@esp.sn", "Cybersécurité");

INSERT INTO etudiant (IdEtu, nom, prenom, DateNaissance, AdresseMail, specialisation) VALUES (4, "Assane", "Gueye", "10-02-2002", "assanegueye1esp.sn", "Cybersécurité");

SELECT * FROM etudiant;

-- Incorrect syntax for inserting into NombreCredits field
INSERT INTO cours (Code, nom, description, NombreCredits) VALUES (210, "Probabilités", "CM", 4);

INSERT INTO cours (Code, nom, description, NombreCredit) VALUES (211, "Statistiques", "CM", 4);

-- Duplicate entry for Code 211
INSERT INTO cours (Code, nom, description, NombreCredit) VALUES (211, "Programmation JAVA", "CM", 2);

INSERT INTO cours (Code, nom, description, NombreCredit) VALUES (213, "Programmation JAVA", "CM", 2);

INSERT INTO cours (Code, nom, description, NombreCredit) VALUES (214, "Developpement Web", "TP", 2);

SELECT * FROM cours;

-- Trying to insert ProfesseurIntervenant directly into table 'cours' with wrong syntax
INSERT INTO cours (ProfesseurIntervenant) VALUES ("Dahirou Wane") WHERE Code="210";

UPDATE cours SET ProfesseurIntervenant = "Dahirou Wane" WHERE Code = "210";

UPDATE cours SET ProfesseurIntervenant = "Oumar Fall" WHERE Code = "211";

UPDATE cours SET ProfesseurIntervenant = "Mouhamed Diop" WHERE Code = "213";

UPDATE cours SET ProfesseurIntervenant = "Fatou Ngom" WHERE Code = "214";

SELECT * FROM cours;

INSERT INTO classe (Code_classe, nom, Responsable_classe) VALUES (201
