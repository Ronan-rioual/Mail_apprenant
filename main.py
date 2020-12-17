
import os
import mysql.connector
from apprenants import Apprenant
from traitement_fichier import Traitement
from bdd import Bdd


def definir_mail(liste_mails, pseudo):
	for mail in liste_mails :
		tmp = mail
		tmp = tmp.replace("@isen-ouest.yncrea.fr", "")
		tmp = tmp.replace("-","")
		tmp = tmp.split(".")
		tmp = tmp[0] + tmp[1][:5] 
		if tmp == pseudo :
			return mail

def main() :

	#os.chdir("..\\..\\Mail apprenants")
	monfichier = Traitement("apprenantmail.txt")
	mailing = monfichier.lire_fichier()

	donnees = Bdd()
	donnees_apprenants = donnees.lire_data()

	donnees.ajouter_colonne()
	for ligne in donnees_apprenants :
		ligne.mail = definir_mail(mailing, ligne.pseudo)
		print(ligne.nom_etudiant, ligne.prenom_etudiant, ligne.id_etudiant, ligne.pseudo, ligne.mail)
		donnees.ecrire_mail(ligne.mail, ligne.id_etudiant)
		
	donnees.fermer_bdd()

main()