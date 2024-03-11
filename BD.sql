CREATE TABLE Eleves(
    id_eleve INTEGER PRIMARY KEY AUTOINCREMENT,
    matricule_eleve VARCHAR(25) NOT NULL,
    nom_eleve VARCHAR(255) NOT NULL,
    prenom_eleve VARCHAR(255) NOT NULL,
    date_naissance DATETIME NOT NULL,
    lieu_naissance VARCHAR(255) NOT NULL,
    adresse_eleve VARCHAR(255) NOT NULL,
    adresse_postal VARCHAR(255),
    telephone_eleve NUMBER NOT NULL,
    niveau_eleve FOREIGN KEY (id_classe) REFERENCES Classes(id_classe) ON DELETE SET NULL NOT NULL,
    titeur FOREIGN KEY (id_parent) REFERENCES Parents(id_parent) ON DELETE SET NULL NOT NULL,
);

CREATE TABLE Parents(
    id_parent INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_parent VARCHAR(255) NOT NULL,
    prenom_parent VARCHAR(255) NOT NULL,
    telephone VARCHAR(255) NOT NULL,
    email_parent VARCHAR(255),
    adresse_parent VARCHAR(255) NOT NULL,
    mot_de_passe VARCHAR(255) NOT NULL,
);

CREATE TABLE Ecoles(
    id_ecole INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_ecole VARCHAR(255) NOT NULL,
    email_ecole VARCHAR(255) NOT NULL,
    telephone_1 NUMBER(30) NOT NULL,
    telephone_2 NUMBER(30),
    date_creation DATE NOT NULL,
    ville_residence VARCHAR(255) NOT NULL,
    adresse_ecole VARCHAR(255) NOT NULL,
    logo_ecole IMAGE,
);

CREATE TABLE ResponsableEcole(
    id_responsable INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(255) NOT NULL,
    nom_responsable VARCHAR(255) NOT NULL,
    email_responsable VARCHAR(255) NOT NULL,
    telephone_responsable NUMBER(30) NOT NULL,
    ville_residence VARCHAR(255) NOT NULL,
    adresse VARCHAR(255) NOT NULL,
    piece_identite IMAGE NOT NULL,
    photo_profile IMAGE,
    mot_de_passe VARCHAR(255) NOT NULL,
); 

CREATE TABLE Classes(
    id_classe INTEGER PRIMARY KEY AUTOINCREMENT,
    libelle_classe VARCHAR(255) NOT NULL,
    numero_classe NUMBER(20),
);

CREATE TABLE EmploiDuTemps(
    id_emp INTEGER PRIMARY KEY AUTOINCREMENT,
    jour VARCHAR(255) NOT NULL,
    heure_debut TIME NOT NULL,
    heure_fin TIME NOT NULL,
    classe FOREIGN KEY (id_classe) REFERENCES Classes(id_classe) ON DELETE CASCADE NOT NULL,
    matiere FOREIGN KEY (id_matiere) REFERENCES Matieres(id_matiere) ON DELETE CASCADE NOT NULL,
    professeur FOREIGN KEY (id_professeur) REFERENCES professeurs(id_professeur) ON DELETE SET NULL,
    salle FOREIGN KEY (id_salle) REFERENCES Salles(id_salle),
);

CREATE TABLE NOTES(
    id_note INTEGER PRIMARY KEY AUTOINCREMENT,
    matiere FOREIGN KEY (id_matiere) REFERENCES Matieres(id_matiere) ON DELETE CASCADE NOT NULL,
    type_note CHOICES("devoir", "examen")
    eleve FOREIGN KEY (id_eleve) REFERENCES Eleves(id_eleve) ON DELETE CASCADE NOT NULL,
);

CREATE TABLE Matieres(
    id_matiere INTEGER PRIMARY KEY AUTOINCREMENT,
    libelle_matiere VARCHAR(255) NOT NULL,
    coeficient INTEGER NOT NULL,
    niveau FOREIGN key (id_classe) REFERENCES Classe(id_classe) ON DELETE CASCADE NOT NULL,
    professeur FOREIGN KEY (id_professeur) REFERENCES Professeur(id_professeur) ON DELETE SET NULL,
);

CREATE TABLE Annonces(
    id_annonce INTEGER PRIMARY KEY AUTOINCREMENT,
    titre_annonce VARCHAR(255) NOT NULL,
    type_annonce  CHOICES ('paiement', 'examen', 'autre'),
    message_annonce TEXT NOT NULL,
    date_annonce DATETIME NOT NULL,
);

CREATE TABLE Professeurs(
    id_professeur INTEGER PRIMARY KEY AUTOINCREMENT,
    matricule VARCHAR(30) NOT NULL,
    nom_professeur VARCHAR(255) NOT NULL,
    prenom_professeur VARCHAR(255) NOT NULL,
    telephone NUMBER(30) NOT NULL,
    niveau FOREIGN key (id_classe) REFERENCES Classe(id_classe) ON DELETE CASCADE NOT NULL,
);

CREATE TABLE Appreciacions(
    id_appreciacion INTEGER PRIMARY KEY AUTOINCREMENT,
    eleve FOREIGN KEY (id_eleve) REFERENCES Eleves(id_eleve) ON DELETE CASCADE NOT NULL,
    progression_eleve VARCHAR(255) NOT NULL,
    comportement VARCHAR(255) NOT NULL, 
    assiduite VARCHAR(255) NOT NULL,
);

CREATE TABLE Comptables(
    id_compte INTEGER PRIMARY KEY AUTOINCREMENT,
    eleve FOREIGN KEY (id_eleve) REFERENCES Eleves(id_eleve) ON DELETE CASCADE NOT NULL,
    mois DATE NOT NULL,
    montant DECIMAL(10,2) NOT NULL,
);

CREATE TABLE RelevePresences(
    id_releve INTEGER PRIMARY KEY AUTOINCREMENT,
    niveau FOREIGN key (id_classe) REFERENCES Classe(id_classe) ON DELETE CASCADE NOT NULL,
    date_presence DATE NOT NULL,
    liste_presence FILE NOT NULL,
);


-- Il y'aura une base de donnée centralisée qui n'aura que la table utilisateur et école 
-- maintenant chaque école aura sa propre base de données 

