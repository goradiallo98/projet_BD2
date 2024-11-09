#  Projet_base_de_donnees---------
#    CREATION de la base de donnees------
Create Database Electromenager;
Use Electromenager;

#   creation de la table Produit----
create table Produit(
    idproduit INT NOT NULL,
    nomproduit VARCHAR(25),
    prixUnitaire FLOAT NOT NULL,
    quantite INT NOT NULL,
    PRIMARY KEY (idproduit));
#  Insertion des valeurs dans la table Produit
INSERT INTO Produit(idproduit, nomproduit, prixUnitaire, quantite)
VALUES(10, 'Refrigerateur', 200000.0, 25),
      (20, 'Micro-ondes', 35000.0, 15),
      (30, 'Cuisiniere', 150000.0, 20),
      (40, 'Aspirateurs', 25000.0, 8),
      (50, 'Machine a laver', 180000.0, 7);

SELECT * FROM Produit;

#  Creation de la table Client

create table Client(
   idClient INT NOT NULL,
   nom VARCHAR(30),
   prenom VARCHAR(40),
   ville VARCHAR(25),
   telephone INT NOT NULL,
   email VARCHAR(30),
   PRIMARY KEY(idClient));

# Insertion des valeurs dans la table Client

INSERT INTO Client(idClient, nom, prenom, ville, telephone, email)
VALUES
   (1, 'NDIOGOYE', 'Jean Marcel Waly', 'Mboro', '772452809', 'marcel01@gmail.com'),
   (2, 'DIAO', 'Kalidou Alassane', 'Tamba', '783051784', 'diaokalidou@gmail.com'),
   (3, 'DIALLO', 'Gora', 'Matam', '760186543', 'gora123@gmail.com'),
   (4, 'FALL', 'Khona', 'Dakar', '709865432', 'fallkhona89@gmail.com'),
   (5, 'NDIAYE', 'Sokhna Diarra', 'Bignona', '770274680', 'boussodiarra@gmal.com');

SELECT * FROM Client;

# creation de la table Commande

create table Commande(
       idCommande INT NOT  NULL,
       idClient INT NOT NULL,
       idproduit INT NOT NULL,
       dateCommande DATE,
       PRIMARY KEY(idCommande)
       FOREIGN KEY (idClient) REFERENCES Client(idClient),
       FOREIGN KEY (idproduit) REFERENCES Produit(idproduit));
       
       # Insertion des values dans la table Commande
       
INSERT INTO Commande(idCommande, idClient, idproduit, dateCommande)
VALUES
      (1, 5, 40, '2024-07-15'),
      (2, 2, 20, '2024-07-20'),
      (3, 1, 20, '2024-07-25'),
      (4, 4, 10, '2024-07-30'),
      (5, 1, 50, '2024-08-01'),
      (6, 1, 30, '2024-08-05'),
      (7, 3, 30, '2024-08-10'),
      (8, 3, 10, '2024-09-15'),
      (9, 5, 10, '2024-09-20'),
      (10, 4, 40, '2024-09-30');
      
SELECT * FROM Commande

# CREATION DE LA TABLE CommandeProduit

create table CommandeProduit(
    idCommande INT NOT NULL,
    idproduit INT NOT NULL,
    quantite INT NOT NULL,
    PRIMARY KEY (idCommande, idproduit),
    FOREIGN KEY (idCommande) REFERENCES Commande(idCommande),
    FOREIGN KEY (idproduit) REFERENCES Produit(idproduit));
    
# Insertion des valeurs dans la table CommandeProduit

Insert into CommandeProduit(idCommande, idproduit, quantite)
VALUES
   (1, 40, 4),
   (2, 20, 5),
   (3, 20, 8),
   (4, 10, 3),
   (5, 50, 4),
   (6, 30, 2),
   (7, 30, 5),
   (8, 10, 3),
   (9, 10, 3),
   (10, 40, 2);

SELECT * FROM CommandePrduit      