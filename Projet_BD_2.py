import mysql.connector
from mysql.connector import Error, errorcode

# Connection a la base de donnees
config = {
    'user': 'root',
    'password': '772507082',
    'host': '127.0.0.1',
    'database': 'Electromenager',
    'raise_on_warnings':True
}

try:
    cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("le nom d'utilisateur ou le mot de passe n'est pas correct")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("la base de donnees n'existe pas")
    else:
        print(" erreur non gere",err)
    exit()

#1 affichage des des noms de produits dont les prixUnitaies sont superieur a 25000
paragraphe = 1
cursorSel = cnx.cursor()
cnx.commit()
Aff_query = "SELECT nomproduit FROM Produit WHERE prixUnitaire > 25000"
cursorSel.execute(Aff_query)
resultats = cursorSel.fetchall()
print(resultats)

#2 Affichage des clients ayant commande un refigerateur

kali = "SELECT nom, prenom FROM Client WHERE idClient = 3"
cursorSel.execute(kali)
result = cursorSel.fetchall()
print(result)
#3 Afficher les clients qui n'ont pas encore effectue de commande
kalis = "SELECT C.nom, C.prenom FROM CLIENT C LEFT JOIN COMMANDE COM ON C.idclient = COM.idclient WHERE COM.idcommande IS NULL"
cursorSel.execute(kalis)
result = cursorSel.fetchall()
if result:
  print("Résultats de la requête :")
  for row in result:
         print(f"nom: {row[0]}, prenom: {row[1]}")
else:
     print("Aucun résultat trouvé.")

#4 requetes
pro_com = "select nomproduit,nom,dateCommande from Produit, Client, Commande where Produit.idproduit = Commande.idproduit AND Client.idClient = commande.idClient"
cursorSel.execute(pro_com)
answer = cursorSel.fetchall()
if answer:
    print("les resultats sont:")
    for row in answer:
        print(f"nomproduit: {row[0]}, nom: {row[1]}, dateCommande: {row[2]}")
else:
    print("Pas de resultats")

# 5 Affficher la liste des produits qui n'ont pas ete commande
waly = "select * from Produit where idproduit NOT IN (Select Distinct idproduit from Commande)"
cursorSel.execute(waly)
resultat = cursorSel.fetchall()
print(resultat)

# 6 la liste des clients ayant passe une commande en septembre 2024
gora = "UPDATE Produit SET prixUnitaire = 190000 WHERE nomproduit = 'Machine a laver'"
cursorSel.execute(gora)
diallo = cursorSel.fetchall()
if diallo:
    print("echec")
else:
    print("maj effectue")

# 7 ) Trouver les produits commande par le client "NDIOGOYE Jean Marcel Waly" 
lopez = "SELECT P.nomproduit FROM Produit P JOIN Commande C ON P.idproduit = C.idproduit JOIN Client CL ON C.idclient = CL.idclient WHERE CL.nom = 'NDIOGOYE' AND CL.prenom = 'Jean Marcel Waly')"
cursorSel.execute(waly)
resultat = cursorSel.fetchall()
print(resultat)

# 8 ) trouver les clieents ayant commandess un refigerateur(idproduit= 10)
ref="SELECT C.nom, C.prenom FROM Client C JOIN Commande CO ON C.idClient=CO.idClient WHERE CO.idproduit=10"
cursorSel.execute(ref)
ref_com = cursorSel.fetchall()
print(ref_com)

# 9 ) afficher kes commandes passees en aout 2024
bar="SELECT idproduit, idclient FROM Commande WHERE dateCommande BETWEEN '2024-08-01' AND '2024-08-31'"
cursorSel.execute(bar)
rab= cursorSel.fetchall()
print(rab)

# 10 ) le nombre total de produits commandes par client
fall="SELECT C.nom, C.prenom, COUNT(CP.idproduit) AS nb_prod FROM Client C JOIN Commande C ON C.idClient=CO.idClient JOIN CommandeProduit CP ON CO.idCommande=CP.idCommande GROUP BY C.nom,C.prenom"
cursorSel.execute(fall)
res=cursorSel.fetchall()
print(res)